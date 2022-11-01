from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, InputRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField("Log In")

class EditPoam(FlaskForm):
    poamid = StringField('Vuln ID:', validators=[DataRequired()])
    description = TextAreaField('Poam Description:', validators=[DataRequired()])
    threat = SelectField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], validators=[DataRequired()])
    created = DateField(description="Date Identified:", validators=[DataRequired()])
    submit = SubmitField("Update Poam")

class AddPoam(FlaskForm):
    poamid = StringField('Vuln ID:', validators=[DataRequired()])
    description = TextAreaField('Poam Description:', validators=[DataRequired()])
    threat = SelectField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], validators=[DataRequired()])
    submit = SubmitField("Create Poam")

class ChangePass(FlaskForm):
    currentpass = PasswordField('Current Password', [InputRequired()])
    newpassword = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit = SubmitField("Update Password")

class EditUser(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    role = SelectField(choices=[('admin', 'Admin'), ('editor', 'Editor'), ('user', 'User')], validators=[DataRequired()])
    active = SelectField(choices=[('True', 'True'), ('False', 'False')], validators=[DataRequired()])
    submit = SubmitField("Update User")

class AddUser(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password', [InputRequired()])
    role = SelectField(choices=[('admin', 'Admin'), ('editor', 'Editor'), ('user', 'User')], validators=[DataRequired()])
    active = SelectField(choices=[('True', 'True'), ('False', 'False')], validators=[DataRequired()])
    submit = SubmitField("Add User")