from flask import render_template
from . import bp
from flask_login import current_user
from app.models import Post
from app.forms import PostForm

@bp.route('/post', methods=['GET','POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(year=form.year.data, type=form.type.data, grade=form.grade.data)
        p.user_id = current_user.user_id
        p.commit()        
    return render_template('post.j2', form=form)