shoping_amount = int(input("Enter shoping amount :"))

if shoping_amount >= 5000:
    print("We are offer to you 10% Discount")
    discount = (shoping_amount * 10) / 100
    print(f"Discount : {discount} Rs")

elif shoping_amount >= 3000 and shoping_amount <= 4999:
    discount = (shoping_amount * 7) / 100
    print(f"Discount : {discount} Rs")

elif shoping_amount >= 1000 and shoping_amount <= 2999:
    discount = (shoping_amount * 5) / 100
    print(f"Discount : {discount} Rs")

elif shoping_amount > 0 and shoping_amount <= 999:
    print("No Discount")
    
else:
    print("Pls you want to Shopping")