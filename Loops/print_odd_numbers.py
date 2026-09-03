# Using for loop

# 1 method
for i in range(1,101,2):
    print(i,end=" ")

# 2nd method
for i in range(1,101):
    if i%2!=0:
        print(i,end=" ")


# Using while loop

i = 1
while(i <= 100):
    if i%2!=0:
        print(i,end=" ")
    i+=2