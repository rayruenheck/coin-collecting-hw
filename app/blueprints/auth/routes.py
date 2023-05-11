from flask import render_template, flash, redirect, url_for
from flask_login import login_user

from app.models import User
from app import db

from . import bp
from app.forms import RegisterForm, SignInForm

@bp.route('/signin', methods=['GET','POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):            
            flash(f'{form.username.data} signing in', 'success')
            login_user(user)
            return redirect(url_for('main.home'))
        
        else:
            flash(f'{form.username.data} does not exist or incorrect password', 'warning')


    return render_template('signin.j2', form=form)


@bp.route('/createaccount', methods=['GET', 'POST'])
def createaccount():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=form.username.data, email=form.email.data, first_name= form.first_name.data, last_name=form.last_name.data)
            u.password = u.hash_password(form.password.data)
            u.commit()
            flash(f'{form.username.data} created')
            return redirect(url_for('main.home'))
        if user:
            flash(f'{form.username.data} already exists')
        else:
            flash(f'{form.email.data} already exists')
    return render_template('createaccount.j2', form=form)

