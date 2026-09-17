s = input("Enter any String :").lower()

count_vowels = 0
count_Consonents = 0


for v in s:
    if v in "aeiou":
        count_vowels+=1
    else:
        count_Consonents+=1

print(f"Vowels : {count_vowels}")
print(f"Consonents : {count_Consonents}")