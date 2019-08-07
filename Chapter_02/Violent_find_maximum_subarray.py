# 暴力求解最大子数组
import numpy as np
import datetime


def violent_find_max_subarray(A):
    n = len(A)
    max = np.iinfo(np.int32).min
    low = 0
    high = 0
    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum += A[j]
            if sum > max:
                max = sum
                low = i
                high = j
    return low, high, max


A = eval(input('Please input a list:'))  # eval去掉输入的字符串的引号，数字就是数字，变量就是变量，列表就是列表
start = datetime.datetime.now()
low, high, max_sum = violent_find_max_subarray(A)
end = datetime.datetime.now()
print('Run time is %d ms.' % (end-start).microseconds)
print("The maximum sub array's low is %d. \n" % low)
print("The maximum sub array's high is %d. \n" % high)
print("The maximum sub array's sum is %d \n" % max_sum)
