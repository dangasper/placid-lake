from flask import current_app

def init_db():
    from flask import current_app
    from app.models.role import Role
    from flask_security.utils import hash_password

    current_app.db.create_all()

    session = current_app.db.session

    security = current_app.extensions.get('security')

    user_role = Role(name='user')
    editor_role = Role(name='editor')
    admin_role = Role(name='admin')
    session.add_all([user_role, editor_role, admin_role])
    session.commit()

    _admin_user = security.datastore.create_user(
        username='admin',
        password=hash_password('admin'),
        roles=[admin_role],
    )
    session.add(_admin_user)
    session.commit()

def init_test_load():
    from flask import current_app
    from faker import Faker
    from flask_security.utils import hash_password
    import random
    import string
    from app.models.poam import Poam
    from app.models.role import Role

    fake = Faker()

    current_app.db.drop_all()
    init_db()

    session = current_app.db.session

    security = current_app.extensions.get('security')

    test_editor_user = security.datastore.create_user(
        username='editor',
        password=hash_password('editor'),
        roles=[editor_role]
    )
    session.add(test_editor_user)

    test_user = security.datastore.create_user(
        username='user',
        password=hash_password('user'),
        roles=[user_role]
    )
    session.add(test_user)

    for x in range(0, 25):
        tmp_pass = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
        tmp_username = fake.first_name().lower() + "." + fake.last_name().lower()
        security.datastore.create_user(
            username=tmp_username,
            password=hash_password(tmp_pass),
            roles=[user_role, ],
        )
    session.commit()

    threatlist = [ 'High', 'Medium', 'Low' ]
    issues = [
        'AlmaLinux 8 : git-lfs (ALSA-2022:7129)',
        'Slackware Linux 14.0 / 14.1 / 14.2 / 15.0 / current expat Vulnerability (SSA:2022-298-01)',
        'Ubuntu 16.04 ESM : Open vSwitch vulnerability (USN-5698-2)',
        'Amazon Linux 2 : kernel (ALASKERNEL-5.15-2022-009)',
        'Ubuntu 18.04 LTS / 20.04 LTS / 22.04 LTS : Barbican vulnerability (USN-5697-1)',
        'RHEL 8 : gnutls (RHSA-2022:7105)',
        'RHEL 8 : device-mapper-multipath (RHSA-2022:7192)',
        'Google Chrome < 107.0.5304.62 Multiple Vulnerabilities'
    ]

    for x in range(41, 1, -1):
        # y variable to start oldest vulnerabilities at earlier poamid
        y = ((42-x))
        tmp_poamid = "VLN-" + str(y)
        tmp_description = random.choice(issues)
        tmp_threat = random.choice(threatlist)
        # Add some vulnerabilities past SLA marks
        if x > 7:
            mixer = (x*3)
        else:
            mixer = 0
        startdate = '-' + str((x+1)+mixer) + 'd'
        enddate = '-' + str((x)) + 'd'
        tmp_datetime = fake.date_time_between(start_date=startdate, end_date=enddate)
        _poams = Poam(
            poamid = tmp_poamid,
            description = tmp_description,
            threat = tmp_threat,
            created = tmp_datetime

        )
        session.add(_poams)
    session.commit()