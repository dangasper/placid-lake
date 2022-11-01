from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)
from flask_login import login_required
from flask_security import roles_required
from app.models.forms import EditUser, AddUser
from app.controllers.admin import get_user_table, delete_user_byID, get_user, update_user, add_user
from app.models.user import User

bp = Blueprint('bp_admin', __name__, url_prefix='/admin')

@bp.route('/users')
@login_required
@roles_required('admin')
def users():
    page = request.args.get('page', 1, type=int)
    count = request.args.get('count', 15, type=int)
    titles, data, pagination = get_user_table(page, count)
    return render_template('admin/users.html', data=data, pagination=pagination, titles=titles, User=User)

@bp.route('/user/new', methods=["GET", "POST"])
@login_required
@roles_required('admin')
def new_user():
    form = AddUser()
    if request.method == 'POST' and form.validate_on_submit():
        message, message_type = add_user(form)
        flash(message, message_type)
        return redirect(url_for('bp_admin.users'))
    return render_template('admin/new_user.html', form=form)

@bp.route('/user/<int:user_id>/edit', methods=["GET", "POST"])
@login_required
@roles_required('admin')
def edit_user(user_id):
    form = EditUser()
    _user = User.query.get(user_id)
    if request.method == 'POST' and form.validate_on_submit():
        edited_user = update_user(user_id, form)
        message = "User " + edited_user + " has been updated."
        flash(message, 'success')
        return redirect(url_for('bp_admin.users'))
    return render_template('admin/edit_user.html', form=form, user=_user)

@bp.route('/user/<int:user_id>/delete', methods=["POST"])
@login_required
@roles_required('admin')
def delete_user(user_id):
    message = delete_user_byID(user_id)
    flash(message, 'danger')
    return redirect(url_for('bp_admin.users'))

@bp.route('/user/<int:user_id>/view')
@login_required
@roles_required('admin')
def view_user(user_id):
    _user = User.query.get(user_id)
    return render_template('admin/view_user.html', view_user=_user)