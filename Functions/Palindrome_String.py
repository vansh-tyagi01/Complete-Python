# 1 Method
def Check_Palindrome(s):
    if s == s[::-1]:
        return f"{s} is Palindrome"
    else:
        return f"{s} is not Palindrome"

print(Check_Palindrome('madam'))


# 2 Method
def Chek_Plindrome(s):
    rev = ""
    original = s
    for char in s:
        rev = char + rev

    if(original == rev):
        return f"{s} is Palindrome"
    else:
        return f"{s} is not Palindrome"

print(Chek_Plindrome('vansh'))