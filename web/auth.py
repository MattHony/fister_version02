# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/2 21:08
# @Author : '红文'
# @File : auth.py
# @Software: PyCharm
from flask import render_template, request, url_for
# from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        redirect(url_for('web.login'))
        # user.password = generate_password_hash(form.password.data)
    return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
        return render_template('auth/login.html', form=form)
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass
