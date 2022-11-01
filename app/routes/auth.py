from flask import (
    Blueprint, render_template, request, flash, redirect, url_for
)
from flask_login import current_user, login_user, login_required, logout_user
from app.models.forms import LoginForm
from app.controllers.auth import get_user, check_password, is_safe_url

bp = Blueprint('bp_auth', __name__, url_prefix='/auth')

@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("bp_dashboard.dashboard"))  # Bypass if user is logged in

    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.username.data)  # Validate Login Attempt
        if user and check_password(user,form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            if not is_safe_url(next_page):
                return flask.abort(400)
            return redirect(next_page or url_for("bp_dashboard.dashboard"))
        flash("Invalid username/password combination")
        return redirect(url_for("bp_auth.login"))
    return render_template(
        "auth/login.html",
        form=form,
    )

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("bp_dashboard.dashboard"))