def ex8(a):
    for x in range(a):
        for i in range(x):
            print (x, end=" ") 
        print(sep="\n")

b=int(input("enter a number: "))   
ex8(b)

