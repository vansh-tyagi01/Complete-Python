# 1st Method
def Max3Numbers(a, b, c):
    return max(a,b,c)

print("Maximum :",Max3Numbers(22,3,5))


# 2nd Method
def Max3Num(d, e, f):
    if d>e:
        if d>f:
            return f"{d} is greater"
        else:
            return f"{f} is greater"
    else:
        if e>f:
            return f"{e} is greater"
        else:
            return f"{f} is greater"


print("Maximum :",Max3Num(88,97,54))

