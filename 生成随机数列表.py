def random_function(total=0, num=1, mini=0, maxi=0, accuracy_requirement=2):
    """
    随机生成num个在指定区间的小数，使其总和为total
    :param total: 总和
    :param num: 个数
    :param mini: 最小值
    :param maxi: 最大值（不会随机到）
    :param accuracy_requirement: 浮点数保留位数
    :return: 生成的随机数列表
    """
    def func(decimal_num, ar=accuracy_requirement):
        """
        浮点数按要求的精度进行四舍五入
        :param decimal_num: 原浮点数
        :param ar: 精度要求
        :return: 四舍五入后的浮点数
        """
        decimal_num += float("0." + "0" * (ar + 1) + "1")
        return round(decimal_num, ar)

    if total < 0:
        raise Exception("个数必须为不小于0的数！")
    if num <= 0 or not isinstance(num, int):
        raise Exception("个数必须为大于0的整数！")
    if total / float(num) < mini:
        raise Exception("最小值不能大于平均数！")
    if total / float(num) > maxi:
        raise Exception("最小值不能小于平均数！")
    if num == 1:
        return [total]

    from random import random
    lave = total - mini * num
    result_list = []
    for i in range(num - 1):
        r = lave * random()
        result_list.append(r)
        lave -= r
    result_list = map(lambda x: func(x + mini, accuracy_requirement), result_list)
    result_list.append(func(total - sum(result_list), accuracy_requirement))
    return result_list


if __name__ == '__main__':
    print random_function(100, 5, 15, 35)
