from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)

from app.controllers.poams import get_poam_table, delete_poam_byID, get_poam, update_poam, add_poam
from app.models.forms import EditPoam, AddPoam
from flask_login import login_required
from flask_security import roles_accepted
from app.models.poam import Poam

bp = Blueprint('bp_poams', __name__, url_prefix='/')

@bp.route('/poams')
@login_required
def poams():
    page = request.args.get('page', 1, type=int)
    count = request.args.get('count', 15, type=int)
    titles, data, pagination, select = get_poam_table(page, count)
    return render_template('poams/poams.html', data=data, pagination=pagination, titles=titles, Poams=select, Poam=Poam)

@bp.route('/poams/new', methods=["GET", "POST"])
@login_required
@roles_accepted('admin', 'editor')
def new_poam():
    form = AddPoam()
    if request.method == 'POST' and form.validate_on_submit():
        message, message_type = add_poam(form)
        flash(message, message_type)
        return redirect(url_for('bp_poams.poams'))
    return render_template('poams/new_poam.html', form=form)

@bp.route('/poams/<int:poam_id>/edit', methods=["GET", "POST"])
@login_required
@roles_accepted('admin', 'editor')
def edit_poam(poam_id):
    form = EditPoam()
    _poam = get_poam(poam_id)
    if request.method == 'POST' and form.validate_on_submit():
        edited_poam = update_poam(_poam, form)
        message = "Poam " + edited_poam + " has been updated."
        flash(message, 'success')
        return redirect(url_for('bp_poams.poams'))
    return render_template('poams/edit_poam.html', form=form, poam=_poam)

@bp.route('/poams/<int:poam_id>/delete', methods=["POST"])
@login_required
@roles_accepted('admin', 'editor')
def delete_poam(poam_id):
    message = delete_poam_byID(poam_id)
    flash(message, 'danger')
    return redirect(url_for('bp_poams.poams'))

@bp.route('/poams/<int:poam_id>/view')
@login_required
@roles_accepted('admin', 'editor')
def view_poam(poam_id):
    _poam = get_poam(poam_id)
    return render_template('poams/view_poam.html', view_poam=_poam)