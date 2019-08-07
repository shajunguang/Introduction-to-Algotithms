本章介绍了插入排序，利用循环不变式证明算法的正确性。  
插入排序:  
  Insertion_sort(A)  
    for j = 2 to A.length  
      key = A[j]  //当前需要插入的关键位置，A[1,2,...,j-1]已经排好序  
      i = j-1  
        while i > 0 and A[i] > key  
          A[i+1] = A[i]  
          i = i-1  
        A[i+1] = key  
