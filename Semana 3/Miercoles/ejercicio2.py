number = int(input("Please enter the number to validate: "))
if number < 0:
    print(f"The number {number} is not perfect")

else:
    aux = number - 1
    acum = 0
    while aux > 0:
        if number % aux == 0:
            acum += aux
        aux -=1

    if acum == number:
        print(f"The number {number} is perfect")
    else:
        print(f"The number {number} is not perfect")