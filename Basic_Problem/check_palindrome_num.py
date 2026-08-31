numbers = int(input("Enter numbers :"))

original = numbers


rev = 0

while(numbers>0):
    digit = numbers % 10
    rev = rev*10 + digit
    numbers//=10

if(original == rev):
    print(f"{original} is a Palindrome Number")
else:
    print(f"{original} is not a Palindrome Number")

    