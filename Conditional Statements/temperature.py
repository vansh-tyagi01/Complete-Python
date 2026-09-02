temp = int(input("Enter current Temperature :"))

if temp < 65 and temp >= 47:
    print("Warning : Very Hot weather pls stay in your Home")
elif temp < 47 and temp >=30:
    print("Hot Weather")
elif temp < 30 and temp >= 20:
    print("Feel's like Good👍")
elif temp < 20 and temp >= 10:
    print("Feel's like Cooling")
elif temp < 10 and temp >= 0:
    print("Very Cool weather🥶")
else:
    print("Invalid Temperature !")