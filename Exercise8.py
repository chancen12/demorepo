def ex8(a):
    for x in range(a):
        for i in range(x):
            print (x, end=" ") 
        print("\n")
n=int(input("enter a number"))
z=ex8(n)
print(z)
