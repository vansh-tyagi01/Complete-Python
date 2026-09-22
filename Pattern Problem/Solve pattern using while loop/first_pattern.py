num = int(input("Enter row of pattern :"))

row = 1
while(row <= num):
    col = 1
    while(col <= num):
        print("*",end=" ")
        col+=1
    print()
    row+=1
    

# Output:
        # Enter row of pattern : 4

        #   * * * *
        #   * * * *
        #   * * * * 
        #   * * * *