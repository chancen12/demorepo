def ex1(x, y):
    
    if (x*y) <= 1000:
        return x * y
    else:
        return x+y

a=int(input())
b=int(input())

z = ex1(a, b)
print("answer:", z)
