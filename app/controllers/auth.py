from flask import current_app, flash, redirect, url_for, request
from flask_security.utils import verify_password
from app.models.user import User
from app.configs.loginmanager import login_manager
from urllib.parse import urlparse, urljoin

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

def get_user(username):
    existing_user = User.query.filter_by(username=username).first()
    return existing_user

def check_password(user, password):
    return verify_password(password, user.password)

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect(url_for("bp_auth.login"))