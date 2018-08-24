# -*- coding: utf-8 -*-
__author__ = 'xujianbo'
__data__ = '2018-07-18'

from api.apiconfig.apiset import apiset
import redis


class Redis:
    def __init__(self):
        self.redis_items = apiset().getConfigItems("redis_db")
        pool = redis.ConnectionPool(host=self.redis_items[0][1], port=self.redis_items[1][0],
                                    password=self.redis_items[2][1])
        self.con = redis.Redis(connection_pool=pool)


    def set(self, key, value):
        self.con.set(key, value)


    def get(self, key):
        return self.con.get(key)
