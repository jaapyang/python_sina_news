#! /usr/bin/env python3
# -*-coding:utf-8-*-

from peewee import *
import datetime

db = MySQLDatabase(database='test', host="127.0.0.1", port=3306, user="root", password="root")
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class UserInfo(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(UserInfo, related_name="tweets")
    message = TextField()
    create_date = DateField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)



