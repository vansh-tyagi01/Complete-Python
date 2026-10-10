#******************************** APPEND ****************************************

#  Append --> In any existing data add new data using .append() method in the last.

# 1. Numbers Append

num = [10,20,30]

num.append(40)
print(num)

# 2. String Appned

name = ['kanhiaya','payal']
name.append('Arun')
print(name)

# List inside List

lst = [1,2,3]
new = [4,5,6]

lst.append(new)

print(lst)   #  [1,2,3,[4,5,6]]