def show_welcome():
    print("***** Welcome to the Store *****")

def show_menu():
    option = input("Please enter a option \n1-Show Inventory\n2-Purchase\n3-Apply Discount\n4-Exit\n-->")
    return option

def show_inventory(products,product_class):
    aux = ""
    if product_class == "1":
        aux = "mobiles"
    else:
        aux = "laptops"
    for brand, product_list in products.get(aux).items():
        print()
        print(brand)
        for product in product_list:
            for key, value in product.items():
                if key == "id":
                    print()
                    print(f"{value} ",end= "-")
                else:
                    print(f" {value} ", end =" ")
        

def main():
    products = {
        "mobiles": {
            "Apple": [
                {
                    "id": 1,
                    "name": "iPhone 7",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "iPhone 8",
                    "price": 350
                },
                {
                    "id": 3,
                    "name": "iPhone Xr",
                    "price": 450
                },
                {
                    "id": 4,
                    "name": "iPhone Xs",
                    "price": 460
                },
                {
                    "id": 5,
                    "name": "iPhone 11",
                    "price": 900
                },
                {
                    "id": 6,
                    "name": "iPhone 12",
                    "price": 1100
                },
                {
                    "id": 7,
                    "name": "iPhone 13",
                    "price": 1300
                },
            ],
            "Samsung": [
                {
                    "id": 8,
                    "name": "Samsung Galaxy Beam",
                    "price": 150
                },
                {
                    "id": 9,
                    "name": "Samsung Galaxy S6",
                    "price": 200
                },
                {
                    "id": 10,
                    "name": "Samsung Galaxy S7",
                    "price": 300
                },
            ],
            "Xiaomi": [
                {
                    "id": 11,
                    "name": "Xiaomi Redmi Note 8",
                    "price": 250
                },
                {
                    "id": 12,
                    "name": "Xiaomi Redmi Note 8 Pro",
                    "price": 300
                },
            ]
        },
        "laptops": {
            "DELL": [
                {
                    "id": 13,
                    "name": "Dell Inspiron 15",
                    "price": 600
                },
                {
                    "id": 14,
                    "name": "Dell Latitude 14",
                    "price": 650
                },
            ],
            "MAC": [
                {
                    "id": 15,
                    "name": "MacBook Pro 13",
                    "price": 900
                },
                {
                    "id": 16,
                    "name": "MacBook M1",
                    "price": 1500
                },
            ]
        },
    }


    show_welcome()
    while True:
        option_main = show_menu()

        if option_main == "1":
            
            product_class = input("What do you want to see \n1-Mobiles\n2-Laptops\n->")
            show_inventory(products,product_class)
        elif option_main == "2":
            pass
        elif option_main == "3":
            pass
        elif option_main == "4":
            print("Thank you!!")
            break
        else:
            print("Please enter a valid option")



main()