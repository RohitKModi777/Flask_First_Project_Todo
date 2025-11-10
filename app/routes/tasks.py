from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models import Task

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/')
def view_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    # Show only tasks of the logged-in user
    tasks = Task.get_by_user(session['user_id'])
    return render_template('tasks.html', tasks=tasks)


@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title:
        # Create new task with current user's ID
        new_task = Task(title=title, status='Pending', user_id=session['user_id'])
        new_task.save()
        flash('Task added successfully!', 'success')
    else:
        flash('Task title cannot be empty.', 'error')

    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/toggle/<task_id>', methods=['POST'])
def toggle_status(task_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    task = Task.get_by_id(task_id)
    if task and str(task.user_id) == session['user_id']:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        task.save()
    
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/clear', methods=['POST'])
def clear_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    # Delete all tasks for current user
    from app import mongo
    from bson.objectid import ObjectId
    
    mongo.db.tasks.delete_many({'user_id': ObjectId(session['user_id'])})
    flash('All your tasks cleared!', 'info')
    
    return redirect(url_for('tasks.view_tasks'))