from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email
class RegisterForm(FlaskForm):
    first_name = StringField('first name',validators=[DataRequired()])
    last_name = StringField('last name',validators=[DataRequired()])
    username = StringField('username',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')