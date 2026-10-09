try:
    item_price = int(input("Enter item Price :"))
    item_sell = int(input("How much did you sell it for? :"))

    if(item_sell > item_price):
        profit = item_sell - item_price
        print(f"Profit : {profit} Rs")

    else:
        loss = item_price - item_sell
        print(f"Loss : {loss} Rs")
    
except:
    print("Please enter only integers as input")