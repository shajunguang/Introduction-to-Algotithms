
# 插入排序


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:  # 升序就改成大于(大的往右移)，降序就改成小于(小的往右移)
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a
    # return 0


# A = eval(input('Please input a list:'))  # eval去掉输入的字符串的引号，数字就是数字，变量就是变量，列表就是列表
# a = A[0:2]  # 切片时开辟新空间
# insertion_sort(a)
# print(A[0:2])
# print(a)
