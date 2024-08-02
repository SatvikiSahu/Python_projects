#define the menu of restaruant
menu ={
 'pizza': 40,
 'burger': 30,
 'pasta': 50,
 'salad': 20,
 'coffee': 15,

}
print("Welcome to the Restaurant!")
print("Our menu:")
print(" pizza: rs40 \n burger: rs30 \n pasta: rs50 \n salad: rs20 \n coffee: rs15")
order_total=0
item_1=input("Enter the first item: ")

if item_1 in menu:
    order_total+=menu[item_1]
    print("You have added", item_1)

     
    another_item=input("Do you want to add another item? (yes/no): ")
    if another_item=='yes':
        item_2=input("Enter the second item: ")
        if item_2 in menu:
            order_total+=menu[item_2]
            print("You have added", item_2)
        else:
            print("Item not found in menu")
print("Your total bill is: Rs", order_total)