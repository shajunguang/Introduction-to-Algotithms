# 选择排序


def selection_sort(a):
    n = len(a)
    for i in range(0, n-1):
        smallest = i
        for j in range(i+1, n):
            if a[j] < a[smallest]:
                smallest = j
        t = a[i]
        a[i] = a[smallest]
        a[smallest] = t
    return a


A = eval(input('Please input a list:'))  # eval去掉输入的字符串的引号，数字就是数字，变量就是变量，列表就是列表
print(selection_sort(A))
