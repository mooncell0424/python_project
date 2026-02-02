# 作者:moon cell
# 2026年01月13日11时22分55秒
# 2912480050@qq.com

# 实现从1到100之间的奇数求和
def sum_odd_numbers():
    total = 0
    for number in range(1, 101):
        if number % 2 != 0:
            total += number
    print("1到100之间的奇数和为:", total)


sum_odd_numbers()
#帮我写个快排

