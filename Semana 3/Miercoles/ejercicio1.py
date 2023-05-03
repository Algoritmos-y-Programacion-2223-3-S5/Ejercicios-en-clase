number = int(input("Please enter the number to validate: "))
if number < 2:
    print(f"The number {number} is prime")

else:
    aux = number - 1
    isPrime = True
    while aux > 1:
        print(f"prueba {aux}")
        if number % aux == 0:
            isPrime = False
            #break
        aux -=1

    if isPrime:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")