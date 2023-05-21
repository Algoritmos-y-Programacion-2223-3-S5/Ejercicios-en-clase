number = int(input("Please enter a number"))
for num in range(number+1):
    if(num == number):
        print(num)
    else:
        print(num, end=",")