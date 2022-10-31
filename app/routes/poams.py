from flask import (
    Blueprint, render_template, request
)

from app.controllers.poams import get_poam_table

bp = Blueprint('bp_poams', __name__, url_prefix='/')

@bp.route('/poams')
def poams():
    page = request.args.get('page', 1, type=int)
    count = request.args.get('count', 15, type=int)
    titles, data, pagination = get_poam_table(page, count)
    return render_template('poams/poams.html', data=data, pagination=pagination, titles=titles)
