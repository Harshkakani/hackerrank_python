if __name__ == '__main__':
    s = input()
    a = []
    b = []
    c = []
    d = []
    e = []

    for x in s:
        if x.isalnum():
            a.append(1)

    for x in s:
        if x.isalpha():
            b.append(1)

    for x in s:
        if x.isdigit():
            c.append(1)

    for x in s:
        if x.islower():
            d.append(1)

    for x in s:
        if x.isupper():
            e.append(1)

    print(len(a)!=0)
    print(len(b)!=0)
    print(len(c)!=0)
    print(len(d)!=0)
    print(len(e)!=0)