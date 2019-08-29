import math

def primeN(n):
    n = n//2
    i = 2
    prime = [2]
    flag=0
    count = 1
    if n==1:
        return 2
    else:
        i = prime[len(prime)-1] + 1
        while count < n:
            k = int(math.floor((math.sqrt(i))))

            flag = 0
            for j in range(len(prime)):
                if prime[j]<=k:
                    if i%prime[j]==0:
                        flag = 1
                        break
                    else:
                        continue

            if flag==0:
                prime.append(i)

                count+=1
            i+=1

    return i-1

def fibonacci(n):
    n = n//2+1
    if n == 0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__=='__main__':
    n = int(input())
    c = []
    c = primeN(n)
    if n%2==0:
        print(primeN(n))
    else:
        print(fibonacci(n))




