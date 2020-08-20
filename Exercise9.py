def ex9(number):
    print("original number", number)
    og = number
    reversen = 0
    while (number > 0):
        reminder = number % 10
        reversen = (reversen * 10) + reminder
        number = number // 10
    if (og == reversen):
        return True
    else:
        return False

print("The original and reverse number is the same:", ex9(131))