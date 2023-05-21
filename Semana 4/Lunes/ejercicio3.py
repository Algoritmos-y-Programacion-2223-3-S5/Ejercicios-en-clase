"""
table = int(input("Table: "))
for num in range(1,11):
    print(num,table,sep=" x ", end=" = ")
    print(num*table)
    """

for num1 in range(1,11):    
    print(f"****** TABLE {num1}******")
    for num2 in range(1,13):
        print(num1,num2,sep=" x ", end=" = ")
        print(num2*num1)