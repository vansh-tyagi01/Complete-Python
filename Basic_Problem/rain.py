humidity = int(input("Enter Humidity :"))
wind = int(input("Enter wind speed in km :"))

if(humidity >= 80):
    if(wind >= 20):
        print("High possibility of Rain")
    else:
        print("Wind speed is low so less possibility of Rain")
else:
    print("Humidity is less so low possibility of Rain")