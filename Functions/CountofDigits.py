def CountofDigits(n):
    count = 0
    cnvrt_n_str = str(n)
    for num in cnvrt_n_str:
        count+=1
    return count

print("Total Count :",CountofDigits(12369))


