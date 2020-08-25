def ex11(number):
    print("original number", number)
    og = number
    reversen = 0
    i=0
    while (number > 0):
        reminder = number % 10
        reversen = (reversen * 10) + reminder
        number = number // 10
    print("the reverse is:",reversen,end=" ")

  
b=int(input("enter a number: "))

ex11(b)