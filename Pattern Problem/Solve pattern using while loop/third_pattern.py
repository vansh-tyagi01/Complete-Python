num = int(input("Enter row of pattern :"))

row = 1
while(row <= num):
    col = 1
    while(col <= row):
        print(col,end=" ")
        col+=1
    print()
    row+=1


# Output:
        #  Enter row of pattern : 4

        #   1
        #   1 2
        #   1 2 3
        #   1 2 3 4