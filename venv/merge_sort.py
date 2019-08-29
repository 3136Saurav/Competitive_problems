import math

def merge_sort(A):
    merge_sort2(A,0,len(A)-1)

def merge_sort2(A, first, last):
    if first < last:
        mid = (first+last)//2
        merge_sort2(A,first,mid)
        merge_sort2(A,mid+1,last)
        merge(A,first,mid,last)

def merge(A,first,mid,last):
    L = A[first:mid]
    R = A[mid:last+1]
    L.append(999999)
    R.append(999999)

    i = j = 0

    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

if __name__ == '__main__':
    A = [8,7,5,9,4]
    merge_sort(A)
    print(A)