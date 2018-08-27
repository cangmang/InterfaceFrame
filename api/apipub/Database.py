# -*- coding: utf-8 -*-

__author__ = 'xujianbo'
__data__ = '2018-03-20'
"""
"""
from api.apiconfig.apiset import apiset
import pymssql

import pymysql

from api.apipub.PyApiLog import log


class apisql(object):
    def __init__(self, host=None, port=None, user=None, password=None):
        config = apiset().getConfigItems("mysql_db")
        if host == None:
            self.host = config[0][1]
        else:
            self.host = host
        if port == None:
            self.port = int(config[1][1])
        else:
            self.port = port
        if user == None:
            self.user = config[2][1]
        else:
            self.user = user
        if password == None:
            self.password = config[3][1]
        else:
            self.password = password

    """
    执行SQLserver查询
    @:param database 所查询的数据库
    @:param sql 查询语句
    """

    def execMssql(self, database, sql):
        self.database = database
        try:
            conn = pymssql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset="utf8")
            cur = conn.cursor()
            if cur:
                log().info(u"执行SQL语句|%s|" % sql)
                cur.execute(sql)
                rows = cur.fetchall()
                if len(rows) == 0:
                    log().warning(u"没有查询到数据")
                return rows
            else:
                log().error(u"数据库连接不成功")
            conn.close()
        except Exception, e:
            log().error(e.message)
        finally:
            conn.close()

    """
    执行SQLserver查询
    @:param database 所查询的数据库
    @:param sql 查询语句
    """

    def execMysql(self, database, sql):
        self.database = database
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   passwd=self.password,
                                   db=self.database,
                                   )
            cur = conn.cursor()
            print cur
            if cur:
                log().info(u"执行SQL语句|%s|" % sql)
                cur.execute(sql)
                result = cur.fetchall()
                # return result
                return map(list, list(result))
        except Exception, e:
            log().error(e)
        finally:
            conn.close()

        # 执行sql语句返回结果
        # def execsql(sql):
        # config = apiset().getConfigItems("mysql_db")
        # host = config[1][1]
        # port = config[2][1]
        # user = config[3][1]
        # password = config[4][1]
        # database = config.get("DATABASE")
        # if driver == "MYSQL":
        #         try:
        #             sql_result = sqldriver(
        #                 host=host,
        #                 port=port,
        #                 user=user,
        #                 password=password,
        #                 database=database
        #             ).exec_mysql(sql)
        #             return sql_result
        #         except Exception, e:
        #             log().error(e)
        #
        #     elif driver == "MSSQL":
        #         try:
        #             sql_result = sqldriver(
        #                 host=host,
        #                 port=port,
        #                 user=user,
        #                 password=password,
        #                 database=database
        #             ).exec_mssql(sql)
        #             return sql_result
        #         except Exception, e:
        #             log().error(e)
        #
        #     else:
        #         log().error(u"[%s]数据库配置支持MYSQL、MSSQL、ORACLE" % driver)