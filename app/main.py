from flask import Blueprint, render_template, url_for, redirect
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('auth.login'))

@main.route('/admin')
def admin():
    return render_template('admin/scheduler.html')

