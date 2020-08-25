def exponent():
    exp=1
    b=int(input("enter base"))
    ex=int(input("enter exponent:"))
    for _ in range(ex):
        exp=exp*b
    print("the exponent is: ",exp)


exponent()