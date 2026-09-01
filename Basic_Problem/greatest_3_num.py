num_1 = int(input("Enter 1st number :"))
num_2 = int(input("Enter 2nd number :"))
num_3 = int(input("Enter 3rd number :"))

if(num_1 > num_2):

    if(num_1 > num_3):
        print(f"{num_1} is Greatest.")
    else:
        print(f"{num_3} is Greatest.")
else:

    if(num_2 > num_3):
        print(f"{num_2} is Greatest.")
    else:
        print(f"{num_3} is Greatest.")