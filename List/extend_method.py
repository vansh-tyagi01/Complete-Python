lst = [10,20]

print("Before :",lst)

lst.extend([30,40])

print("After :",lst)


print(" ")
# ___________________________________
print(" ")


fruits = ['Apple' , 'Mango' , 'Orange']

print("Before :",fruits)

fruits.extend(['Pineapple' , 'Banana'])

print("After :",fruits)


print(" ")
# ___________________________________
print(" ")

# Empty list

empty_lst = []

empty_lst.extend("ABC")

print("After :",empty_lst)  # ['A', 'B', 'C']
