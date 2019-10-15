def sub_sum(arr, total):
    n = len(arr)
    result = 0
    found = False
    for i in range(n):
        sum = 0
        for e in range(i,n):
            sum+=arr[e]
            #print(e, 'SUM--> ',sum)
            if sum == total:
                found = True
                return i+1, e+1
    if found == False:
        return -1
    return

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        NS = input().split()
        N = int(NS[0])
        S = int(NS[1])
        A = list(map(int, input().split()))
        result = sub_sum(A,S)
        if result != -1:
            i, j = result[0], result[1]
            print(i, j)
        else:
            print(str('-1'))

'''
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
'''
