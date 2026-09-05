def Add(a,b):
    return a + b

def Sub(a,b):
    return a - b

def Mul(a,b):
    return a * b

def Div(a,b):
    try:
        return a / b
    except:
        return "Not Divisible by zero"

while(True):
    
    print("1. Add\n2. Subtract\n3. Multiplication\n4. Division")

    choice = int(input("Enter your choice ?:"))

    num_1 = int(input("Enter 1st Number :"))

    num_2 = int(input("Enter 2nd Number :"))

    if choice == 1:
        print("Result :",Add(num_1,num_2))

    elif choice == 2:
        print("Result :",Sub(num_1,num_2))

    elif choice == 3:
        print("Result :",Mul(num_1,num_2))

    elif choice == 4:
        print("Result :",int(Div(num_1,num_2)))

    else:
        print("Invalid Choice !")
    