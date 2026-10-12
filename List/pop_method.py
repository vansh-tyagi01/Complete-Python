nums = [10,20,30,40]
print("Before pop :",nums)

nums.pop()   #  if we are apply pop method without indexing so last element delete.

print("After pop :",nums)


print(" ")
#______________________________________

y = [10,20,30,40]

z = y.pop()

print(y)   #   [10, 20, 30]
print(z)   #   40

print(" ")
# ______________________________________

# remove through indexing

nums_lst = [100,200,300,400,500]
print("Before Remove :",nums_lst)

nums_lst.pop(2)   # 300 remove

print("After Remove :",nums_lst)

print(" ")
# ______________________________________

names = ['kanhaiya','vansh','Avi']
print("Before Remove :",names)

names.pop(2)  #  Avi remove

print("After Remove :",names)
