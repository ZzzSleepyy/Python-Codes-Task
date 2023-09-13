import time

sleep = time.sleep
print("1.Coke","2.Milk","3.Oishi","4.Vitamins")
money = int(input("How much do you have?: "))
balance = 0
balance = balance + money 
number_range = int(input("How many items do you want in a single item?: "))
list_cart = []
item_price = {"1": 20, "2": 35, "3": 15, "4": 30}

try:
    if balance > 14:
        for i in range(number_range):
            i = i + 1
            item_add = input("Enter the Item you want to add in your cart: ")
            list_cart.append(item_add)
            print(f"You have added {i} in your cart. \n Added: {list_cart}")
            if item_add == "1":
                print("COKE\nPrice: 20")
            elif item_add == "2":
                print("MILK\nPrice: 35")
            elif item_add == "3":
                print("OISHI\nPrice: 15")
            elif item_add == "4":
                print("VITAMINS\nPrice: 30")
    elif balance < 15:
        print("You dont have enough Credits.")
        raise
    else:
        pass
except ValueError or RuntimeError:
    print("Error")
    
    
total_price = sum(item_price[item] for item in list_cart)
balance_calculate = balance - total_price
print(f"Total price for items in your cart: {total_price}P")
sleep(1)
print("CALCULATING TOTAL")
sleep(2)
print(f"CHANGE: {balance_calculate}")    
    
    
    
    
        