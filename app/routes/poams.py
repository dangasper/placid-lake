from flask import (
    Blueprint, render_template, request, flash, Markup, redirect, url_for
)

bp = Blueprint('bp_poams', __name__, url_prefix='/')

@bp.route('/poams')
def poams():
    return render_template('poams/poams.html')