def ex10(m, n):
    print("1st List ", m)
    print("2nd List ", n)
    p = []
    
    for c in m:
        if (c % 2 != 0):
            p.append(c)
    for c in n:
        if (c % 2 == 0):
            p.append(c)
    return p

x = [11, 14, 13, 19, 22]
y = [13, 26, 24, 33, 10]

print("result List is", ex10(x, y))