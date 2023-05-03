number1 = input("Please enter number 1: \n->")
number2 = input("Please enter number 2: \n->")

if number1.isnumeric() and number2.isnumeric():
    number1 = int(number1)
    number2 = int(number2)
    if number2 == 0:
        print("Number 2 can´t be 0")
    else:
        print(f"The result is {number1/number2}")
        
else:
    print("Error in input")