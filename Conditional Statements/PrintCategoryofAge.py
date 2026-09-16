age = int(input("Enter your Age :"))

if age <= 13 and age > 0:
    print("Child")
elif age > 13 and age <= 19:
    print("Teenager")
elif age > 19 and age <= 59:
    print("Adult")
elif age > 59 and age <= 120:
    print("Senior Citizen")
else:
    print("Invalid age")
