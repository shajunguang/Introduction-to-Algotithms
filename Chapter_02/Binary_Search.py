# 二分法在有序数组进行查询，迭代和递归两种方法


def iterative_binary_search(A, v):
    n = len(A)
    i = int((n-1)/2)
    j = 0
    while -2 < j < 2:
        if v == A[i]:
            return i
        elif v > A[i]:
            i = int((n+i)/2)
            if i == n-1:
                j += 1
        else:
            i = int(i/2)
            if i == 0:
                j -= 1
    return -1


def recursive_binary_search(A, v, low, high):
    if low > high:
        return -1
    mid = int((low+high)/2)
    if v == A[mid]:
        return mid
    elif v > A[mid]:
        return recursive_binary_search(A, v, mid+1, high)
    else:
        return recursive_binary_search(A, v, low, mid-1)


# A = eval(input('Please input a sorted list: '))  # eval去掉输入的字符串的引号，数字就是数字，变量就是变量，列表就是列表
# v = int(input('Please input a  needed number: '))
# print('The answer of Iterative: %d' % iterative_binary_search(A, v))
# print('The answer of Recursive: %d' % recursive_binary_search(A, v, 0, len(A)-1))
