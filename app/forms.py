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

class SignInForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign-In')

class PostForm(FlaskForm):
    year = StringField('year', validators=[DataRequired()])
    type = StringField('type', validators=[DataRequired()])
    grade = StringField('grade', validators=[DataRequired()])
    submit = SubmitField('Publish')