import math

def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def isprime(n):
    k = int(math.sqrt(n))
    if n==1:
        return False
    for i in range(2,k+1):
        if (n%i)==0:
            return False
        else:
            continue
    return True

if __name__ == '__main__':
    n = int(input())
    llst = []
    flst = []
    llst2 = []
    for i in range(n):
        llst.append(0)
        flst.append(0)
        llst2.append(0)

    x = 0

    for i in range(1, n):
        if(isprime(i)):
            llst[i-1] = i

    for i in range(1, n):
        x = fibonacci(i)
        llst2[i-1] = x

    j = 0
    k = 0

    print(llst)
    print(llst2)

    for i in range(0,n):
        if i%2==0:
            flst[i]=(llst[j])
            j+=1
        else:
            flst[i]=(llst2[k])
            k+=1
    print(flst)




