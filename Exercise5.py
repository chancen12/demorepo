def ex7(a):
    print("the numbers are: ",a) 
    x = a[0]
    y = a[-1]
    if (x == y):
        return True
    else:
        return False

b= [14, 20, 33, 60, 40]
print("result: ", ex7(b))