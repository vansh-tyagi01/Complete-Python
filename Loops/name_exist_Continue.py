names = ['kanhaiya','vansh','payal','arun','ritika']

# Using for loop

for name in names:
    if 'kanhaiya' == name:
        continue
    print(name)


# Using while loop

length = len(names)

i = 0
while(i < length):
    if 'vansh' == names[i]:
        i+=1
        continue
    print(names[i])
    i+=1
