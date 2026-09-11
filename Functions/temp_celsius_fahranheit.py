# Celsius to fahrenheit

def Cel_Fahrnheit(c):
    f = (c * 9/5) + 32
    return f
celsius = int(input("Enter Celsius :"))
print("Celsius to Fahrenheit :",int(Cel_Fahrnheit(celsius)),"F")


# fahrenheit to celsius

def Fah_Cel(f):
    c = (f - 32) * 5/9
    return c
fahrenheit = int(input("Enter Fahrenheit :"))
print("Fahrenheit to Celsius :",int(Fah_Cel(fahrenheit)),"C")