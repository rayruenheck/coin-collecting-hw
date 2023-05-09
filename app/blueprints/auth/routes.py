from flask import render_template, flash, redirect, url_for

from app.models import User
from app import db

from . import bp
from app.forms import RegisterForm

@bp.route('/signin')
def signin():
    return render_template('signin.j2')

@bp.route('/createaccount', methods=['GET', 'POST'])
def createaccount():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=username, email=form.email.data, password=form.password.data)
            u.commit()
            flash(f'{username} created')
            return redirect(url_for('main.home'))
        if user:
            flash(f'{form.username.data} already exists')
        else:
            flash(f'{form.email.data} already exists')
    return render_template('createaccount.j2', form=form)