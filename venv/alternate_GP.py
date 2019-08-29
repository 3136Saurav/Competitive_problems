def gp(n,r1,r2):
    list1=[1,1]
    a=1
    b=1
    if n==1:
        return [1]
    elif n==2:
        return list1
    else:
        for i in range(3,n+1):
            if i%2!=0:
                list1.append(a*r1)
                a*=r1
            else:
                list1.append(b * r2)
                b *= r2

    return list1

if __name__ == '__main__':
    n = int(input())
    r1 = int(input())
    r2 = int(input())
    c = gp(n, r1, r2)
    print(c)