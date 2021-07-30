#coding=utf-8
def select_sort(alist):
    n=len(alist)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if alist[min_index]>alist[j]:
                min_index=j
        alist[i],alist[min_index]=alist[min_index],alist[i]
        print(alist)
    return alist
alist=[42,20,17,13,28,14,23,15]
select_sort(alist)