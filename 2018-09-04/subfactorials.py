# https://en.wikipedia.org/wiki/Derangement

def get_subfactorial(n):
    if (n == 0):
        return (1)
    if (n == 1):
        return (0)
    return ((n-1) * (get_subfactorial(n-1) + get_subfactorial(n-2)))


print (get_subfactorial(6))   #-> 265
print (get_subfactorial(9))   #-> 133496
print (get_subfactorial(14))  #-> 32071101049
