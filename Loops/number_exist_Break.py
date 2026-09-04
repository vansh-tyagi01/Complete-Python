nums = [10,20,25,30,50]

# Using for loop

for num in nums:
    if 20 == num:
        break
    print(num)


# Using while loop

i = 0
while(i < 5):
    if 25 == nums[i]:
        break
    print(nums[i])
    i+=1
