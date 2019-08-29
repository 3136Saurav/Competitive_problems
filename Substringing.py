def count_substring(string, sub_string):
    n = len(sub_string)
    length = len(string)
    words = ""
    i = 0
    j = 0
    k = 0
    m = 0
    lst = []
    while i < length - (n-1):
        for j in range(n):
            words += string[k]
            j += 1
            k += 1
        lst.append(words)
        k -= j
        k += 1
        j = 0
        i += 1
        words = ""
    for i in lst:
        if i == sub_string:
            m += 1
        else:
            continue
    return lst


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

