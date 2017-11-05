#! /usr/bin/env python3
import unittest

# -*-coding:utf-8-*-
from unittest import TestCase

from repositories.mysql import Mysql


class TestMysql(unittest.TestCase):
    # def test___init__(self):
    #     db = Mysql()
    #     host = db.get_host()
    #     self.assertEquals(host, "127.0.0.1")

    def test_open_connection(self):
        db = Mysql()
        host = db.open_connection()
        self.assertEquals(host, '127.0.0.1')


if __name__ == '__main__':
    unittest.main()
