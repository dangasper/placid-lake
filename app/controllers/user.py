from flask import current_app, flash
from flask_security.utils import verify_password, hash_password
from app.models.user import User
from app.configs.loginmanager import login_manager
from flask_login import current_user

def validate_and_updatePass(old, new):
    session = current_app.db.session

    if verify_password(old, current_user.password):
        current_user.password = hash_password(new)
        session.commit()
        return 'Password has been updated', 'success'
    return 'Password change failed.', 'danger'
