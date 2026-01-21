# 作者:moon cell
# 2026年01月12日15时43分16秒
# 2912480050@qq.com
def use_sum():
    """
    学习算术运算符
    :return:
    """
    a = 5 / 2
    print(a)
    a = 5 // 2
    print(a)


def use_compare():
    print(3 > 5)


def use_logic():
    """
    使用逻辑运算符
    :return:
    """
    print(3 and 5)
    print(0 or 3)


def use_logic2():
    """
    短路运算目的是不想写if
    :return:
    """
    a = False

    a and print('hello')
    a = True
    a or print('你可以看到or')


def use_bit():
    """
    位运算练习
    :return:
    """
    print(5 & 7)
    print(5 | 7)
    print(~5)
    print(5 ^ 7)
    # 左移永远是乘2
    print(5 << 1)
    print(-5 << 1)
    print('-' * 50)
    # 右移正数高位补0，负数高位补1,低位丢弃
    print(5 >> 1)
    print(-6 >> 1)  # 减1除2
    # 异或特点
    print(5 ^ 0) # 5
    print(5 ^ 5) # 0


# use_sum()
# use_compare()
# use_logic()
# use_logic2()
use_bit()
# 帮我写个快排


