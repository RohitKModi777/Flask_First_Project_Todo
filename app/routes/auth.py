from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models import User

auth_bp = Blueprint('auth', __name__)

# Register Route
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validation checks
        if not username or not password:
            flash('Please fill in both username and password.', 'error')
            return redirect(url_for('auth.register'))

        # Check if user already exists
        existing_user = User.get_by_username(username)
        if existing_user:
            flash('Username already exists. Please choose another.', 'error')
            return redirect(url_for('auth.register'))

        # Create new user
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


# Login Route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Find user by username
        user = User.get_by_username(username)

        if user and user.check_password(password):
            session['user_id'] = str(user._id)  # Store MongoDB ObjectId as string
            session['username'] = user.username
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid username or password.', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')


# Logout Route
@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('auth.login'))