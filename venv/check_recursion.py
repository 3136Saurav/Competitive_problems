def less(a,b):
    if a<b:
        return True
    else:
        return False

def insertion_sort(A):
    for i in range(len(A)):
        item = A[i]
        j = i-1
        while(j>=0 and A[j]>item):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = item

    return A

if __name__ == '__main__':
    A = [5,4,3,2,1,12,0,]
    B = insertion_sort(A)
    print(B)