'''def gcd(a, b):
    p = a % b
    if p == 0:
        return b
    else:
        return gcd(b, p)

def lcm(a, b):
    t = (a*b)//gcd(a, b)
    return t

def getTotalX(a, b):
    count = 0
    flag = 0
    x = a[0]
    for i in range(len(a) - 1):
        x = lcm(x, a[i + 1])

    while True:
        for j in range(len(b)):
            if b[j] % x == 0:
                continue
            else:
                flag = 1
                break
        if flag != 1:
            count = count + 1
        if x <= min(b):
            x = x + x
        else:
            break

    return count

if __name__ == '__main__':
    n = 2
    m = 3
    arr = [2,4]
    brr = [176,32,96]

    total = getTotalX(arr, brr)
    #print('--> ',total)
'''
import math

k = int(math.sqrt(10))
print(k)






