from flask import (
    Blueprint, render_template, request, flash, Markup, redirect, url_for
)

bp = Blueprint('bp_dashboard', __name__, url_prefix='/')

@bp.route('/')
@bp.route('/index')
def index():
    return redirect(url_for('bp_dashboard.dashboard'))

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')