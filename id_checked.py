#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
主要用于推算出类似 6221261980****3456 或 622126********3456
以及上述两种格式最后一位是 x 的身份证号的所有排列组合情况
"""
from datetime import datetime, timedelta
import re


class ParseID:

    def __init__(self, id_str):
        if re.match(r"(^\d{6}[\d]{4}[*]{4}\d{3}[\dxX]$)|(^\d{6}[*]{8}\d{3}[\dxX]$)|(^\d{17}[\dxX]$)", id_str):
            self.__id = id_str
        else:
            raise Exception("ID的格式错误")

    @staticmethod
    def __check(id_str):
        place_weight = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1)
        result = 0
        for i in range(18):
            result += place_weight[i] * tuple(int(i) if i.isdigit() else 10 for i in id_str)[i]
        if result % 11 == 1:
            return True
        else:
            return False

    def check(self):
        if re.match('^\d{17}[\dxX]$', self.__id):
            result = self.__check(self.__id)
        else:
            result = False
        if result:
            print(f'{self.__id} 可能是一个真实的ID。')
        else:
            print(f'{self.__id} 不可能是一个真实的ID。')

    def search_possible(self, start_day='19200101'):
        if re.match(r"^\d{6}[\d]{4}[*]{4}\d{3}[\dxX]$", self.__id):
            start_day = self.__id[6:10] + "0101"
            end_day = self.__id[6:10] + "1231"
        else:
            end_day = '{0:%Y%m%d}'.format(datetime.now())
        result = []
        for day in self.date_range(start_day, end_day):
            id_str = self.__id[:6] + day + self.__id[-4:]
            if self.__check(id_str):
                result.append(id_str)
        return result

    @staticmethod
    def date_range(start_date, end_date, step=1, date_format="%Y%m%d"):
        start_date = datetime.strptime(start_date, date_format)
        end_date = datetime.strptime(end_date, date_format)
        days = (end_date - start_date).days
        return [datetime.strftime(start_date + timedelta(i), date_format) for i in range(0, days, step)]

    def parse(self):
        address = self.__id[:6]
        if int(self.__id[-2]) & 1:
            print("男性")
        else:
            print("女性")

        
if __name__ == '__main__':
    pid = ParseID("411302********4238")
    pid.check()
    print(pid.search_possible())
