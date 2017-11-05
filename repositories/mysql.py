#! /usr/bin/env python3
# -*-coding:utf-8-*-
import configparser

import pymysql


class Mysql:
    __config__ = {}

    """Mysql 数据访问类"""

    def __init__(self):
        # 读取配置文件
        cf = configparser.ConfigParser()
        cf.read('config.ini')
        self.__config__ = {
            'host': cf.get("db", "db_host"),
            'port': cf.get("db", "db_port"),
            'user': cf.get("db", "db_user"),
            'password': cf.get("db", "db_password"),
            'db': cf.get("db", "db_dbName"),
            'charset': cf.get("db", "db_charset")
        }

    def open_connection(self):
        cursor = pymysql.connect(self.__config__)
        cursor.open()
        print(cursor)
        return cursor.host
