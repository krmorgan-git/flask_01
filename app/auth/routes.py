from urllib.parse import urlsplit
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.auth import auth_bp
from app.auth.forms import RegistrationForm, LoginForm
from app.models import User
from app.extensions import db

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data.lower()
        )
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Account created! Please log in.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html', title='Register', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(
            db.select(User).filter_by(email=form.email.data.lower())
        ).scalar_one_or_none()

        if user and user.check_password(form.password.data):
            # Logs user in and manages session cookie
            login_user(user, remember=getattr(form, 'remember_me', None) and form.remember_me.data)
            flash(f'Welcome back, {user.username}!', 'success')
            
            # Safe redirect: handle ?next=/protected_page parameter
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                next_page = url_for('main.index')
            return redirect(next_page)
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('auth/login.html', title='Log In', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))