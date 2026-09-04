nums = [2,58,77,9,48,100]

# Using for loop

for num in nums:
    if num == 77:
        #print("skip",num)
        continue
    print(num,end=" ")


# Using while loop

length = len(nums)

i = 0
while(i < length):
    if nums[i] == 9:
        i+=1
        continue
    print(nums[i],end=" ")
    i+=1
