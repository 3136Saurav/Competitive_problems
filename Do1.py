def print_formatted(number):
    n = len(bin(number)) - 2
    i = 1
    for i in range(number + 1):
        o = oct(i)
        o = o[2:]
        h = hex(i)
        h = h[2:]
        b = bin(i)
        b = b[2:]
        i = str(i)
        args = (i, o, h, b)
        padded_args = zip([n] * len(args), args)
        print("%*s %*s %*s %*s" %(int(i),int(o),int(h),int(b)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
'''width = 20
args = ("Python", "Very Good")
padded_args = zip([width] * len(args), args)
# Flatten the padded argument list.
print ("%*s : %*s" % tuple([item for list in padded_args for item in list]))'''
