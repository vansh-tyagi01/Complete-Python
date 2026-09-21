n = int(input("Enter a number :"))

count = 1

for row in range(1,n+1):
    for col in range(1,row+1):
        print(count,end=" ")
        count+=1
    print()

# Output:
    # Enter a number :4

    #    1
    #    2 3
    #    4 5 6
    #    7 8 9 10