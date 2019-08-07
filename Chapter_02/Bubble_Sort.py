# 冒泡排序


def bubble_sort(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(n-1, i+2, -1):
            if a[j] < a[j-1]:
                t = a[j]
                a[j] = a[j-1]
                a[j-1] = t
    return a


A = eval(input('Please input a list:'))  # eval去掉输入的字符串的引号，数字就是数字，变量就是变量，列表就是列表
print('Before sort:', A)
bubble_sort(A)
print('After sort:', A)
