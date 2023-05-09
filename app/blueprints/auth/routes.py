from flask import render_template

from . import bp

@bp.route('/signin')
def signin():
    return render_template('signin.j2')

@bp.route('/createaccount')
def createaccount():
    return render_template('createaccount.j2')