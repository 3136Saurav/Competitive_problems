def check(s):
    for i in range(len(s)):

        if s[i].isalnum():
            print("True")
            break
        else:
            print("False")
            break
    for i in range(len(s)):
        if s[i].isalpha():
            print("True")
            break
        else:
            print("False")
            break
    for i in range(len(s)):
        if s[i].isdigit():
            print("True")
            break
        else:
            print("False")
            break
    for i in range(len(s)):
        if s[i].islower():
            print("True")
            break
        else:
            print("False")
            break
    for i in range(len(s)):
        if s[i].isupper():
            print("True")
            break
        else:
            print("False")
            break



if __name__ == '_q_main__':
    s = input()
    check(s)