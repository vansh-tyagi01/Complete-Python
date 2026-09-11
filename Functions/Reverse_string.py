# 1 Method using Slicing

def Rev_string(s):
    rev_string = s[::-1]
    return rev_string

print("Reverse String :",Rev_string('vansh'))


# 2 Method

def Reverse_String(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

print("Reverse String :",Reverse_String('Kanhaiya'))