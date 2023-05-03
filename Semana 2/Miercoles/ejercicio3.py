number = input("Please enter the number to validate: \n->")

if number.isnumeric():
    number = int(number)
    if number % 2 == 0:
        print("Even")
    else: 
        print("Odd")