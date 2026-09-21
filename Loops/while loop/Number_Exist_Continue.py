# Using while loop

nums = [10,20,25,35,45]

i = 0
while(i < 5):
    if 25 == nums[i]:
        i+=1
        continue
    print(nums[i])
    i+=1