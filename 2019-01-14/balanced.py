def getSideScore(side):
    score = 0
    
    for letter in side:
        if (letter == 'x'):
            score = (score - 1)
        else:
            score = (score + 1)

    return score

def balanced(balanceInput):
    length = len(balanceInput)

    if (length == 0):
        return True

    if (length % 2 != 0):
        return False

    left = getSideScore(balanceInput[:(length/2)])
    right = getSideScore(balanceInput[(length/2):])

    total = left + right

    if (total == 0):
        return True

    return False

def main():
    print balanced("xxxyyy")
    print balanced("yyyxxx")
    print balanced("xxxyyyy")
    print balanced("yyxyxxyxxyyyyxxxyxyx")
    print balanced("xyxxxxyyyxyxxyxxyy")
    print balanced("")
    print balanced("x")

main()
