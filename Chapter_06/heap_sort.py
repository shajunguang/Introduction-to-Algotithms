# 堆排序 O(nlgn)
# 值得注意的是： 之前为了省略堆长度的n形参变量，在29行更新最大堆采用切片的形式，认为
# 对len(A)会变成切片的长度，其实他只是A的部分复制。


def max_heapify(A, i, n):
    l = 2*i + 1
    r = 2*i + 2
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, n)


def build_max_heapify(A, n):
    for i in range(n//2, -1, -1):
        max_heapify(A, i, n)


def heap_sort(A, n):
    build_max_heapify(A, n)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        n = n-1
        max_heapify(A, 0, n)


A = eval(input('Please input a list:'))  # eval去掉输入的字符串的引号，数字就是数字，变量就是变量，列表就是列表
print('Before sort:', A)
heap_sort(A, len(A))
print('After sort:', A)
