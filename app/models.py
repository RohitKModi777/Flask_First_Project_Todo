from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask_login import UserMixin


# -------------------------------
# User Model
# -------------------------------
class User(UserMixin):
    def __init__(self, username, password_hash=None, _id=None):
        self.username = username
        self.password_hash = password_hash
        self._id = _id

    @property
    def id(self):
        """Flask-Login requires an 'id' property"""
        return str(self._id)

    def set_password(self, password):
        """Hashes the password before saving."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the hashed password."""
        return check_password_hash(self.password_hash, password)

    def save(self):
        """Save user to MongoDB"""
        user_data = {
            'username': self.username,
            'password_hash': self.password_hash
        }
        result = mongo.db.users.insert_one(user_data)
        self._id = result.inserted_id
        return self

    @staticmethod
    def get_by_username(username):
        """Find user by username"""
        user_data = mongo.db.users.find_one({'username': username})
        if user_data:
            return User(
                username=user_data['username'],
                password_hash=user_data['password_hash'],
                _id=user_data['_id']
            )
        return None

    @staticmethod
    def get_by_id(user_id):
        """Find user by ID"""
        try:
            user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
            if user_data:
                return User(
                    username=user_data['username'],
                    password_hash=user_data['password_hash'],
                    _id=user_data['_id']
                )
        except:
            pass
        return None


# -------------------------------
# Task Model
# -------------------------------
class Task:
    def __init__(self, title, status="Pending", user_id=None, _id=None):
        self.title = title
        self.status = status
        self.user_id = user_id
        self._id = _id

    @property
    def id(self):
        return str(self._id)

    def save(self):
        """Save task to MongoDB"""
        task_data = {
            'title': self.title,
            'status': self.status,
            'user_id': ObjectId(self.user_id)
        }
        if self._id:
            mongo.db.tasks.update_one(
                {'_id': ObjectId(self._id)},
                {'$set': task_data}
            )
        else:
            result = mongo.db.tasks.insert_one(task_data)
            self._id = result.inserted_id
        return self

    @staticmethod
    def get_by_user(user_id):
        """Get all tasks for a user"""
        tasks_data = mongo.db.tasks.find({'user_id': ObjectId(user_id)})
        tasks = []
        for task_data in tasks_data:
            tasks.append(Task(
                title=task_data['title'],
                status=task_data['status'],
                user_id=str(task_data['user_id']),
                _id=task_data['_id']
            ))
        return tasks

    @staticmethod
    def get_by_id(task_id):
        """Get task by ID"""
        try:
            task_data = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})
            if task_data:
                return Task(
                    title=task_data['title'],
                    status=task_data['status'],
                    user_id=str(task_data['user_id']),
                    _id=task_data['_id']
                )
        except:
            pass
        return None

    def delete(self):
        """Delete task from MongoDB"""
        mongo.db.tasks.delete_one({'_id': ObjectId(self._id)})