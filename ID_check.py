import datetime

PLACE_WEIGHT = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1)


def date_str(id_str):
    year_now = int(str(datetime.datetime.now())[:4])
    id_str1 = id_str[:id_str.find("*")]
    id_str2 = id_str[id_str.rfind("*") + 1:]
    x = len(id_str1)
    y = len(id_str2)
    if x <= 6:
        y_number = year_now - 1900
    elif x == 7:
        if int(id_str1[6]) == 1:
            # year = int(id_str1[6] + "900")
            y_number = 99
        elif int(id_str1[6]) == 2:
            # year = int(id_str1[6] + "000")
            y_number = year_now - int(id_str1[6] + "000")
        else:
            print("请按正确的格式输入。")
            return
    elif x == 8:
        if int(id_str1[6]) == 1 and int(id_str1[7]) == 9:
            # year = int(id_str1[6:] + "00")
            y_number = 99
        elif int(id_str1[6]) == 2 and int(id_str1[7]) <= int(str(year_now)[1]):
            # year = int(id_str1[6:] + "00")
            y_number = year_now - int(id_str1[6:] + "00")
        else:
            print("请按正确的格式输入")
            return
    elif x == 9:
        if int(id_str1[6]) == 1 and int(id_str1[7]) == 9:
            # year = int(id_str1[6:] + "0")
            y_number = 9
        elif int(id_str1[6]) == 2 and int(id_str1[7]) <= int(str(year_now)[1]) \
                and int(id_str1[8]) <= int(str(year_now)[2]):
            # year = int(id_str1[6:] + "0")
            y_number = year_now - int(id_str1[6:] + "0")
        else:
            print("请按正确的格式输入")
            return
    else:
        if 1900 <= int(id_str1[6:10]) <= year_now:
            y_number = 0
        else:
            print("请按正确的格式输入")
            return
    i = 0
    while i <= y_number:
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
                if x <= 6 and y <= 4:
                    ymd_str = id_str1 + str(1900 + i)
                elif x > 6 and y <= 4:
                    ymd_str = (str(i) + j_str + k_str)[x - 6:]
                elif x <= 6 and y > 4:
                    ymd_str = (str(i) + j_str + k_str)[:y - 4]
                elif x > 6 and y > 4:
                    ymd_str = (str(i) + j_str + k_str)[x - 6:y - 4]
                yield ymd_str
                k += 1
            j += 1
        i += 1


def check_one(id_str="000000000000000000"):
    if id_str.endswith("x") or id_str.endswith("X"):
        id_place_tuple = [int(i) for i in id_str[:-1]]
        id_place_tuple.append(10)
        id_place_tuple = tuple(id_place_tuple)
    else:
        id_place_tuple = tuple(int(i) for i in id_str)
    result = 0
    for j in range(18):
        result += PLACE_WEIGHT[j] * id_place_tuple[j]
    a = result % 11
    if a == 1:
        return True
    else:
        return False


# def id_check(id_str="000000000000000000"):
#
#     if "*" in id_str:
#         id_str1 = id_str[:6]
#         id_str2 = id_str[-4:]
#         m = 0
#         for i in date_str:
#             id_str = id_str1 + i + id_str2
#             if check_one(id_str):
#                 print(f"{id_str} 可能是一个真正的身份证号")
#                 m += 1
#         print(f"共有 {m} 种可能。")
#     else:
#         if check_one(id_str):
#             print(f"{id_str} 可能是一个真正身份证号。")


if __name__ == '__main__':
    id_str = input("请输入一个像 123456********1234 或 1234567890****1234 这样的18位身份证号码：")
    if "*" in id_str:
        date_str_obj = date_str(id_str)
        m = 0
        for i in date_str_obj:
            if check_one(i):
                print(f"{i} 可能是一个真正的身份证号")
                m += 1
        print(f"共有 {m} 种可能。")

    else:
        if check_one(id_str):
            print(f"{id_str} 可能是一个真正身份证号。")
