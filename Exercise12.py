def ex12(number):

    tax=0
    if(number<=10000):
        tax=10000*0
    elif(number<=20000):
        tax=10000*0+10000*0.1
    else:
        tax=(10000*0)+(10000*(10/100))+(number-20000)*(20/100)
    return(tax)
a=int(input("enter a number: "))
print("the tax is",ex12(a))