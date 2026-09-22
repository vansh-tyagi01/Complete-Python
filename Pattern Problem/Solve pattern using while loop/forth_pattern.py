num = int(input("Enter row of pattern :"))

row = 1
count = 1
while(row <= num):
    col = 1
    while(col <= row):
        print(count,end=" ")
        count+=1
        col+=1
    print()
    row+=1



# Output:
        #  Enter row of pattern : 4

        #  1
        #  2 3
        #  4 5 6
        #  7 8 9 10
