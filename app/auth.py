from contextlib import redirect_stderr
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .forms import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm(request.form)
    # email = request.form.get('email')
    # password = request.form.get('password')

    # if form.validate_on_submit():
    #     # flash(f"{email} - {password}")
    #     flash("Login realizado com sucesso!", "success")
    #     return redirect(url_for('main.admin'))
    # #     return redirect(url_for('auth.login'))

    # else:
    #     flash("Usuário ou senha inválidos!", "error")
    return render_template('account/login.html', form=form)


@auth.route('/signup')
def signup():
    return render_template('account/signup.html')
