from flask import current_app
from datetime import datetime as dt, date, timedelta
import calendar
from app.models.poam import Poam


def get_poam_table(page, count):
    session = current_app.db.session
    db = current_app.db

    page = page
    count = count
    select = session.query(Poam).order_by(Poam.created.desc())
    pagination = db.paginate(select, page=page, per_page=count, max_per_page=50, error_out=True, count=True)
    poams = pagination.items
    titles = [('vulnid', 'Vuln ID'), ('description', 'Vulnerability'), ('threat', 'Threat Level'), ('created', 'Date Created'), ('age', 'Age')]
    data = []
    for poam in poams:
        #determine age between opened and now
        age = date.today() - poam.created
        data.append({'poamid': poam.id, 'vulnid': poam.poamid, 'description': poam.description, 'threat': poam.threat, 'created': poam.created.strftime('%m/%d/%Y'), 'age': age.days })
    return titles, data, pagination, select

def delete_poam_byID(poam_id):
    session = current_app.db.session

    _poam = Poam.query.get(poam_id)

    if _poam:
        session.delete(_poam)
        session.commit()
        return f'Poam {_poam.poamid} has been deleted.'
    return f'Poam {_poam.poamid} did not exist and could therefore not be deleted.'

def get_dashboard(page):

    highs = get_poam_count_byThreat('High')
    meds = get_poam_count_byThreat('Medium')
    lows = get_poam_count_byThreat('Low')
    
    # Highs past 30 days, Mediums past 90 days, Lows past 180 days
    highs_sla = get_poam_count_pastSla('High', 30)
    meds_sla = get_poam_count_pastSla('Medium', 90)
    lows_sla = get_poam_count_pastSla('Low', 180)

    # Total poams last 7 days
    days = 7
    titles, recent_poams, pagination = get_poams_rangeToNow(page, days)

    # Get chart data for past 6 months
    months = get_chart_months()
    chartHigh = get_total_poams_byMonth(months, 'High')
    chartMed = get_total_poams_byMonth(months, 'Medium')
    chartLow = get_total_poams_byMonth(months, 'Low')

    return highs, meds, lows, highs_sla, meds_sla, lows_sla, titles, recent_poams, pagination, months, chartHigh, chartMed, chartLow

def get_poam_count_byThreat(threat_level):
    session = current_app.db.session
    db = current_app.db

    selection = session.execute(db.select(Poam).filter_by(threat=threat_level)).all()
    
    return len(selection)

def get_poam_count_pastSla(threat_level, sla_days):
    session = current_app.db.session
    db = current_app.db

    selection = session.execute(db.select(Poam).filter(Poam.threat == threat_level, Poam.created <= date.today()-timedelta(days=sla_days))).all()

    return len(selection)

def get_poams_rangeToNow(page, days):
    session = current_app.db.session
    db = current_app.db

    page = page
    titles = [('vulnid', 'Vuln ID'), ('description', 'Issue'), ('threat', 'Threat Level')]
    select = db.select(Poam).filter(Poam.created >= date.today()-timedelta(days=days))
    pagination = db.paginate(select, page=page, per_page=5, max_per_page=5, error_out=True, count=True)
    latest_poams = pagination.items
    recent_poams = []
    for latest_poam in latest_poams:
        recent_poams.append({ 'vulnid': latest_poam.poamid, 'description': latest_poam.description, 'threat': latest_poam.threat })

    return titles, recent_poams, pagination

def get_chart_months():
    chartlabels = list()
    for i in range(5, -1, -1):
        chartmonth = calendar.month_name[date.today().month - i]
        chartlabels.append(chartmonth)
    return chartlabels

def get_total_poams_byMonth(months, threat_level):
    session = current_app.db.session
    db = current_app.db

    poams = list()
    for month in months:
        monthconv = dt.strptime(month, "%B")
        query = session.execute(db.select(Poam.id, Poam.created).filter_by(threat=threat_level)).all()
        poam_total = 0
        for row in query:
            if int(row.created.month) == monthconv.month:
                poam_total += 1
        poams.append(poam_total)
    return poams

def get_poam(poam_id):
    db = current_app.db

    _poam = db.get_or_404(Poam, poam_id),
    description=f"No poam id '{poam_id}'."

    return _poam

def update_poam(poam, form):
    session = current_app.db.session

    if poam:
        poam.poamid = form.poamid.data
        poam.description = form.description.data
        poam.threat = form.threat.data
        poam.created = form.created.data
        session.commit()
        return f'Poam {poam.poamid} has been updated.'
    return f'Poam {poam.poamid} did not exist and could therefore not be edited.'

def add_poam(form):
    session = current_app.db.session

    try:
        _poam = Poam(
        poamid = form.poamid.data,
        description = form.description.data,
        threat = form.threat.data,
        )
        session.add(_poam)
        session.commit()

        return 'Poam {_poam.poamid} has been created.', 'success'
    except:
        return 'Poam could not be created.', 'danger'