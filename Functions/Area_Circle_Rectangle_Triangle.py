# For Circle

def Area_circle():
    radius = float(input("Enter circle Radius :"))

    result = 3.14 * radius * radius

    print(f"Area of Circle : {result}")


# For Rectangle

def Area_Rectangle():
    length = float(input("Enter length of Rectangle :"))
    width = float(input("Enter width of Rectangle :"))

    result = length * width

    print(f"Area of Rectangle : {result}")


# For Triangle

def Area_Triangle():
    base = float(input("Enter base of Triangle :"))
    height = float(input("Enter height of Triangle :"))

    result = 0.5 * base * height

    print(f"Area of Triangle : {result}")


while(True):
    print("1. Area of Circle\n2. Area of Rectangle\n3. Area of Triangle")
    choice = int(input("Enter your choice ?:"))

    if choice == 1:
        Area_circle()
    elif choice == 2:
        Area_Rectangle()
    elif choice == 3:
        Area_Triangle()
    else:
        print("Invalid Choice !")