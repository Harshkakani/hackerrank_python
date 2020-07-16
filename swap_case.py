def swap_case(s):
    a = []
    for i in list(s):
        j = ''
        if i.isupper():
            j = i.lower()
        elif i.islower():
            j = i.upper()
        else:
            a.append(i)
        a.append(j)


    return ''.join(a)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)