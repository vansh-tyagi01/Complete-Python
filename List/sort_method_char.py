# 1st Case

ch = [1,"a",2]
ch.sort()
print(ch)     #  TypeError : not supported between instances of 'str' and 'int'



# 2nd Case

# Ascending

ch = ["s","d","a","e"]
ch.sort()
print(ch)    #   ['a', 'd', 'e', 's']

# ________________________________

# Descending

ch = ["s","d","a","e"]
ch.sort(reverse=True)
print(ch)          #   ['s', 'e', 'd', 'a']