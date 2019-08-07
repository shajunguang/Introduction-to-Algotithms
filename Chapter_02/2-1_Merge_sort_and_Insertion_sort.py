# 合并排序和插入排序的合体
from Insertion_Sort import insertion_sort


def merge(a, p, q, r):
    L = a[p:q+1]  # 这里直接利用列表切片赋值，比c中的循环复制方便
    R = a[q+1:r+1]
    L.append(4399)
    R.append(4399)
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i = i+1
        else:
            a[k] = R[j]
            j = j+1
    return 0   # return 是函数结束的标志，因此def函数要记得有返回类型，如果进行处理，就返回0之类的


def merge_sort(a, p, r, k):  # k表示需要做插入排序的数组的长度
    if r-p+1 > k:
        q = int((p+r)/2)
        merge_sort(a, p, q, k)
        merge_sort(a, q+1, r, k)
        merge(a, p, q, r)
    else:
        # 这里需要注意一点，如果使用插入排序，形参是数组的切片时，开辟新的空间，
        # 即新的列表，操作影响的新的列表，即原来的不受影响
        a[p:r+1] = insertion_sort(a[p:r+1])  # 切片 L[0：N]是值0到N-1的元素
    return 0


A = eval(input('Please input a list:'))  # eval去掉输入的字符串的引号，数字就是数字，变量就是变量，列表就是列表
print('Before sort:', A)
merge_sort(A, 0, len(A)-1, 2)
print('After sort:', A)
