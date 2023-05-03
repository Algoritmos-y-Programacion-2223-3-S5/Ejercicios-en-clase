age = input("Please enter your age: \n->")

if age.isnumeric():
    age = int(age)
    if age >= 18:
        print("Mayor")
    else: 
        print("Menor")