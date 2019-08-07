import datetime


def linear_find_max_subarray(A, low, high):
    max_sum = A[0]
    pre_sum = 0
    left = low
    right = low
    sub_left = low
    for i in range(low, high+1):
        if pre_sum < 0:
            pre_sum = A[i]
            sub_left = i
        else:
            pre_sum += A[i]
        if pre_sum > max_sum:
            max_sum = pre_sum
            left = sub_left
            right = i
    return left, right, max_sum


A = eval(input('Please input a list:'))  # eval去掉输入的字符串的引号，数字就是数字，变量就是变量，列表就是列表
start = datetime.datetime.now()
low, high, max_sum = linear_find_max_subarray(A, 0, len(A)-1)
end = datetime.datetime.now()
print('Run time is %d ms.' % (end-start).microseconds)
print("The maximum sub array's low is %d. \n" % low)
print("The maximum sub array's high is %d. \n" % high)
print("The maximum sub array's sum is %d \n" % max_sum)
