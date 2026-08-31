name = input("Enter a String :")

if(name == name[::-1]):
    print(f"{name} is Palindrome.")
else:
    print(f"{name} is not a Palindrome.")