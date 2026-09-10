units = int(input("Enter units :"))


if units <= 100 and units >= 0:
    bill = 0
    bill = bill + (units * 5)
    print("Bill :",bill)

elif units >= 101 and units <= 200:
    bill = 0
    bill = bill + (100 * 5) + (units - 100) * 7
    print("Bill :",bill)

elif units > 200:
    bill = 0
    bill = bill + (100 * 5) + (100 * 7) + (units - 200) * 10
    print("Bill :",bill)