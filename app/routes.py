from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, \
    ResetPasswordRequestForm, ResetPasswordForm
from app.models import User, Post

from flask_mail import Mail, Message

#instead of top one 
# from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, \
#     ResetPasswordRequestForm, ResetPasswordForm, ContactForm

# from .emails import email_activation

   

@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
# @login_required
def index():
    page = request.args.get('page', 1, type=int)

    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE2'], True)

    first = Post.query.order_by(Post.timestamp.desc()).first()

    next_url = url_for('blog', page=posts.next_num) \
        if posts.has_next else None

    prev_url = url_for('blog', page=posts.prev_num) \
        if posts.has_prev else None

    
    return render_template('index.html', title='Home', posts=posts.items, first=first,
                           next_url=next_url, prev_url=prev_url)


@app.route('/blog')
# @login_required
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('blog', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('blog', page=posts.prev_num) \
        if posts.has_prev else None
   
    return render_template('blog.html', title='Blog', posts=posts.items,
                           next_url=next_url, prev_url=prev_url)

@app.route('/termsandconditions')
def tandc():
    return render_template('tandc.html', title='Terms and conditions')

@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html', title='Monitoring')





@app.route('/ind_posts/<my_id>', methods=['GET'])
def ind_posts(my_id):
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    single = Post.query.filter_by(id=my_id).first_or_404()
    return render_template('ind_posts.html', title='ind_posts', my_id=my_id, posts=posts.items, single=single)





@app.route('/our_team')
# @login_required
def our_team():
    page = request.args.get('page', 1, type=int)
   
    return render_template('our_team.html', title='Our Team')

@app.route('/off-grid')
# @login_required
def off_grid():
    page = request.args.get('page', 1, type=int)
  
    return render_template('off_grid.html', title='Off-Grid')

@app.route('/solar_systems')

def solar_systems():
    page = request.args.get('page', 1, type=int)
  
    return render_template('solar_systems.html', title='Solar Systems')


@app.route('/contact_us')
# @login_required
def contact_us():
    page = request.args.get('page', 1, type=int)
   
    return render_template('contact_us.html', title='Contact Us')


@app.route('/our_customers')
# @login_required
def our_customers():
    page = request.args.get('page', 1, type=int)
   
    return render_template('our_customers.html', title='Our Customers')

# logic for the site login ... 


@app.route('/my_posts', methods=['GET', 'POST'])
@login_required
def my_posts():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))

    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('my_posts.html', title='My Posts', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('my_posts'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('my_posts')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)



# login for the site logout

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



# logicfor registering an account 


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# login for password reset

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)

# logic for reset password

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))