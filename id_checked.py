"""
主要用于推算出类似 6221261980****3456 或 622126********3456
以及上述两种格式最后一位是 x 的身份证号的所有排列组合情况
"""

import datetime
PLACE_WEIGHT = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1)


def check_one(id_str_18="000000000000000000"):
    if id_str_18.endswith("x") or id_str_18.endswith("X"):
        id_place_tuple = [int(i) for i in id_str_18[:-1]]
        id_place_tuple.append(10)
        id_place_tuple = tuple(id_place_tuple)
    else:
        id_place_tuple = tuple(int(i) for i in id_str_18)
    result = 0
    for j in range(18):
        result += PLACE_WEIGHT[j] * id_place_tuple[j]
    a = result % 11
    if a == 1:
        return True
    else:
        return False


def ymd_str():
    year_now = int(str(datetime.datetime.now())[:4])
    i = 1900
    while i <= year_now:
        flag_year = False
        if i % 100 != 0 and i % 4 == 0:
            flag_year = True
        if i % 400 == 0:
            flag_year = True
        j = 1
        while j <= 12:
            month_days = 0
            if j in (1, 3, 5, 7, 8, 10, 12):
                month_days = 31
            elif j in (4, 6, 9, 11):
                month_days = 30
            elif j == 2 and flag_year:
                month_days = 29
            elif j == 2 and (not flag_year):
                month_days = 28
            k = 1
            while k <= month_days:
                if j < 10:
                    j_str = "0" + str(j)
                else:
                    j_str = str(j)
                if k < 10:
                    k_str = "0" + str(k)
                else:
                    k_str = str(k)

                yield str(i) + j_str + k_str

                k += 1
            j += 1
        i += 1


def md_str(id_str_18="000000000000000000"):
    flag_year = False
    year = int(id_str_18[6:10])
    if year % 100 != 0 and year % 4 == 0:
        flag_year = True
    if year % 400 == 0:
        flag_year = True
    j = 1
    while j <= 12:
        month_days = 0
        if j in (1, 3, 5, 7, 8, 10, 12):
            month_days = 31
        elif j in (4, 6, 9, 11):
            month_days = 30
        elif j == 2 and flag_year:
            month_days = 29
        elif j == 2 and (not flag_year):
            month_days = 28
        k = 1
        while k <= month_days:
            if j < 10:
                j_str = "0" + str(j)
            else:
                j_str = str(j)
            if k < 10:
                k_str = "0" + str(k)
            else:
                k_str = str(k)

            yield j_str + k_str

            k += 1
        j += 1


def main():
    id_str = input("请输入一个已知的或像 123456********123x 或 1234562019****1234 这样的18位身份证号码：")
    if "*" in id_str:
        # print(id_str[id_str.find("*"):id_str.rfind("*") + 1])
        if len(id_str[id_str.find("*"):id_str.rfind("*") + 1]) == 4:
            m = 0
            for i in md_str(id_str):
                new_id_str = id_str[:id_str.find("*")] + i + id_str[id_str.rfind("*") + 1:]
                if check_one(new_id_str):
                    print(f"{new_id_str} 可能是一个正确的身份证号")
                    m += 1
            print(f"共有 {m} 种可能。")
        elif len(id_str[id_str.find("*"):id_str.rfind("*") + 1]) == 8:
            m = 0
            for i in ymd_str():
                new_id_str = id_str[:id_str.find("*")] + i + id_str[id_str.rfind("*") + 1:]
                if check_one(new_id_str):
                    print(f"{new_id_str} 可能是一个正确的身份证号")
                    m += 1
            print(f"共有 {m} 种可能。")
        else:
            print("输入格式不正确")
    else:
        if check_one(id_str):
            print(f"{id_str} 可能是一个正确的身份证号")
        else:
            print("这不是一个正确的身份证号。")


if __name__ == '__main__':
    main()