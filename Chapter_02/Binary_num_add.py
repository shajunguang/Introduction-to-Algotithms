# 两个二进制数相加


def sum_binary(a, b, n):
    t = 0
    c = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        s = a[i]+b[i]+t
        if s >= 2:
            c[i+1] = s % 2
            t = 1
        else:
            c[i+1] = s % 2
            t = 0
    c[0] = t
    return c


A = [0, 1, 1, 0, 1]
B = [1, 1, 1, 1, 0]

print('A数组保存的二进制数是: %s' % A)
print('B数组保存的二进制数是: %s' % B)
print('数组二进制数之和为: %s' % sum_binary(A, B, len(A)))
