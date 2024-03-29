# 合并排序+滑窗法查找 O(nlgn)+O(n)=O(nlgn)  解决找出数组两个数求和为某数的问题：先用归并排序，再使用滑窗法查找
from Merge_Sort import merge_sort


def check_sums(S, p, r, x):
    ans = list()
    merge_sort(S, p, r)
    # 滑窗法 给定初始锚 和大了移动右边 和小了移动左边 因此为O(n)
    i = p
    j = r
    while i < j:
        a = S[i]+S[j]
        if a == x:
            if [S[i], S[j]] not in ans:  # 输出不同解
                ans.append([S[i], S[j]])
            i = i+1
        elif a > x:
            j = j-1
        else:
            i = i+1
    return ans


A = [1, 2, 3, 4, 4, 7, 7, 6, 5, 8]
print(check_sums(A, 0, len(A)-1, 11))
