def substring(s, k):
    j = 0
    i = 0
    word = ''
    lst = []
    m = 0
    for i in range(len(s)//k):
        while j < k:
            word += s[m]
            m += 1
            j += 1
        lst.append(word)
        j = 0
        word = ''
        i += 1
    return lst

def merge_the_tools(string, k):
    sub = substring(string, k)
    lst1 = []
    word = ''
    final_list = []
    for i in sub:
        lst1 = list(i)
        for j in lst1:
            if j not in word:
                word += j
        final_list.append(word)
        word = ''
    print(final_list)
    print('\n'.join(final_list))

if __name__ == '__main__':

    string, k = input(), int(input())
    l = []
    l = substring(string, k)
    print(l)
    merge_the_tools(string, k)
