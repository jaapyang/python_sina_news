#! /usr/bin/env python3
# -*-coding:utf-8-*-
from repositories.orm import UserInfo


class UserInfoService:
    def add_user(self, username):
        UserInfo.create(username=username)

    def get_users(self):
        return UserInfo.select()
