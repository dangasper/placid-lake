from flask import (
    Blueprint, render_template, request, flash, Markup, redirect, url_for
)

from app.controllers.poams import get_dashboard

bp = Blueprint('bp_dashboard', __name__, url_prefix='/')

@bp.route('/')
@bp.route('/index')
def index():
    return redirect(url_for('bp_dashboard.dashboard'))

@bp.route('/dashboard')
def dashboard():
    page = request.args.get('page', 1, type=int)
    highs, meds, lows, highs_sla, meds_sla, lows_sla, titles, recent_poams, pagination, months, chartHigh, chartMed, chartLow = get_dashboard(page)
    return render_template('dashboard/dashboard.html', highs=highs, meds=meds, lows=lows, hsla=highs_sla, msla=meds_sla, lsla=lows_sla, titles=titles, recent_poams=recent_poams, pagination=pagination, months=months, chartHigh=chartHigh, chartMed=chartMed, chartLow=chartLow)