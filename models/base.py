# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/30 20:45
# @Author : '红文'
# @File : base.py
# @Software: PyCharm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    # create_time = Column('create_time', Interger)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
