name = "vvkkann"

for i in range(len(name)):
    count = 0

    for j in range(len(name)):
        if(name[i] == name[j]):
            count+=1

    if(count == 1):
        print(name[i])
        break



        