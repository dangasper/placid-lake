# Models

## forms.py

Create FlaskForm input fields for form rendering.

### LoginForm

Provides username, Password, Remember Me data input for login form.

### EditPoam

Provides Vuln ID, Poam Description, Threat selection, and change identified date data input for edit poam form.

### AddPoam

Provides Vuln ID, Poam Description, and Threat selection for add poam form.

### ChangePass

Provides Current password, New Password, Repeat Password data input for change password form.

### EditUser

Provides Username, role selection, and active selection data input for edit user form.

### AddUser

Provides Username, Password, role selection and active selection for add user form.

## logging.py

Creates LogSetup class to provide log configuration and basic log features

## poam.py

Creates schema for poams:

**id** - Integer, Primary key

**poamid** - String, Identifier for POAM

**description** - Text, Description of POAM

**threat** - String, High, Medium, Low rating

**created** - Date, the date the POAM was created

## role.py

Creates schema for roles:

**id** - Integer, Primary key

**name** - String, Name of role

**description** - String, description of role

## rolesuser.py

Creates database table for many to many association between roles and users

**user_id** - foreignkey relation to user.id

**role_id** = foreignkey relation to role.id

## user.py

Creates schema for users:

**id** - Integer, Primary Key

**username** - String, Username of user

**password** - String, password hash of user

**active** - Boolean, Active user flag

**last_login_at** - DateTime, Last user login date/time

**current_login_at** - DateTime, Current user login date/time

**last_login_ip** - String, Last known ip of user login

**current_login_ip** - String, Current known ip of user login

**login_count** - Integer, number of user logins

**roles** - Relationship to roles_users table 