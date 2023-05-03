number = int(input("Please enter the number1 to validate: "))
number2 = int(input("Please enter the number2 to validate: "))
if number < 0 or number2 < 0:
    print(f"The numbers {number} and {number2} are not friends")

else:
    aux1 = number - 1
    acum1 = 0
    while aux1 > 0:
        if number % aux1 == 0:
            acum1 += aux1
        aux1 -=1

    aux2 = number2 - 1
    acum2 = 0
    while aux2 > 0:
        if number2 % aux2 == 0:
            acum2 += aux2
        aux2 -=1

    if acum1 == number2 and acum2 == number:
        print(f"The numbers {number} and {number2} are friends")

    else:
        print(f"The numbers {number} and {number2} are not friends")
