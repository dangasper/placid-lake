from flask import (
    Blueprint, render_template, request, flash
)
from flask_security import login_required
from app.models.forms import ChangePass
from app.controllers.user import validate_and_updatePass

bp = Blueprint('bp_user', __name__, url_prefix='/user')

@bp.route('/profile')
@login_required
def profile():
    return render_template('user/profile.html')

@bp.route('/password', methods=["GET", "POST"])
@login_required
def password():
    form = ChangePass()
    if request.method == 'POST' and form.validate_on_submit():
        message, message_type = validate_and_updatePass(form.currentpass.data, form.newpassword.data)
        flash(message, message_type)
    return render_template('user/password.html', form=form)