from flask import current_app
from app.models.user import User
from app.models.rolesusers import roles_users
from app.models.role import Role
from flask_login import current_user
from flask_security.utils import hash_password

def get_user_table(page, count):
    session = current_app.db.session
    db = current_app.db

    page = page
    count = count
    select = session.query(User).order_by(User.username)
    pagination = db.paginate(select, page=page, per_page=count, max_per_page=50, error_out=True, count=True)
    users = pagination.items
    titles = [('username', 'Username'), ('role', 'Role'), ('active', 'active')]
    data = []
    for user in users:
        role = [role.name for role in user.roles]
        data.append({'userid': user.id, 'username': user.username, 'role': role[0], 'active': user.active})
    return titles, data, pagination

def update_user(user_id, form):
    session = current_app.db.session

    _user = User.query.get(user_id)
    tmp_active = form.active.data == 'True'
    if _user:
        _user.username = form.username.data
        _user.role = form.role.data
        _user.active = tmp_active
        session.commit()
        return f'User {_user.username} has been updated.'
    return f'User {_user.username} did not exist and could therefore not be edited.'

def add_user(form):
    session = current_app.db.session

    security = current_app.extensions.get('security')

    _active = form.active.data == 'True'
    try:
        new_user = security.datastore.create_user(
        username=form.username.data,
        password=hash_password(form.password.data),
        roles=[form.role.data,],
        active=_active
        )
        session.add(new_user)
        session.commit()

        return f'User {new_user.username} has been created.', 'success'
    except:
        return f'User could not be created.', 'danger'

def get_user(user_id):
    db = current_app.db

    _user = db.get_or_404(User, user_id),
    description=f"No user id '{user_id}'."

    return _user

def delete_user_byID(user_id):
    session = current_app.db.session

    _user = User.query.get(user_id)

    if _user:
        session.delete(_user)
        session.commit()
        return f'user {_user.username} has been deleted.'
    return f'user {_user.username} did not exist and could therefore not be deleted.'