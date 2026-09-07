def Count_Vowels(s):
    count = 0
    for v in s:
        if v in 'aeiou':
            count+=1
    return count

s = input("Enter any string :")

print(f"Count of vowels in {s} :",Count_Vowels(s))

