marks = int(input("Enter marks :"))

if marks<0:
    print("Invalid marks")

if marks>=90:
    print("Passed")
    print("Performance :","Excellent")
elif marks<90 and marks>=60:
    print("Passed")
    print("Performance :","Good")
elif marks<60 and marks>=33:
    print("Passed")
    print("Performance :","Poor")
else:
    if marks<33 and marks>=0:
        print("Failed")
        print("Performance :","Very Bad")
