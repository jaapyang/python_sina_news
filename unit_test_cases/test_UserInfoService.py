#! /usr/bin/env python3
# -*-coding:utf-8-*-

import unittest
from unittest import TestCase

import datetime

from repositories.UserInfoService import UserInfoService


class TestUserInfoService(TestCase):
    # def test_add_user(self):
    #     with UserInfoService() as service:
    #         service.add_user("jack" + str(datetime.datetime.now))

    def test_get_users(self):
        with UserInfoService() as service:
            u_list = service.get_users()
            for u in u_list:
                print(u.username)


if __name__ == '__main__':
    unittest.main()
