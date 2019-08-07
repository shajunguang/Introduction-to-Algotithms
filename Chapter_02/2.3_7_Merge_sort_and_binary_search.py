# 合并排序+二分查找 O(nlgn)+O(nlgn)=O(nlgn)
from Merge_Sort import merge_sort
from Binary_Search import recursive_binary_search


def check_sums(S, p, r, x):
    ans = list()
    merge_sort(S, p, r)
    for i in range(p, r+1):
        y = recursive_binary_search(S, x-S[i], i+1, r)
        if y != -1:
            ans.append([S[i], S[y]])
    return ans


A = [1, 2, 3, 4, 7, 6, 5]
print(check_sums(A, 0, len(A)-1, 11))
