def ex2(a):
    x = 0
    for i in range(a):
        sum = x + i
        print("Current", i, "Previous ", x," Sum: ", sum)
        x = i

res=int(input("Type a number"))

ex2(res)