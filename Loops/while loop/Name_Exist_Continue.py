# Using while loop

names = ['kanhaya','vansh','payal']

length = len(names)

i = 0
while(i < length):
    if 'vansh' == names[i]:
        i+=1
        continue
    print(names[i])
    i+=1