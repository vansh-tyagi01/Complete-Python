s = input("Enter any String :").lower()

if s == s[::-1]:
    print(f"{s} is Palindrome")
else:
    print(f"{s} is not Palindrome")