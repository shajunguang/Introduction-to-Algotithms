# 寻找最大子数组 分治
import numpy as np
import datetime


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = np.iinfo(np.int32).min
    sum = 0
    max_left = 0
    for i in range(mid, low-1, -1):  # 需要注意一点，下降序列时最后一个要-1,才能取到本身，和升序相反
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = np.iinfo(np.int32).min
    sum = 0
    max_right = 0
    for j in range(mid+1, high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    ans = list()
    if high == low:
        return low, high, A[low]
    else:
        mid = int((low + high)/2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


A = eval(input('Please input a list:'))  # eval去掉输入的字符串的引号，数字就是数字，变量就是变量，列表就是列表
start = datetime.datetime.now()
low, high, max_sum = find_maximum_subarray(A, 0, len(A)-1)
end = datetime.datetime.now()
print('Run time is %d ms.' % (end-start).microseconds)
print("The maximum sub array's low is %d. \n" % low)
print("The maximum sub array's high is %d. \n" % high)
print("The maximum sub array's sum is %d \n" % max_sum)
