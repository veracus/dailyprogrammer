def check(word):
    if (word.find('ei') > -1 and word.find('cei') == -1):
        return False

    if (word.find('cie') > -1):
        return False

    return True

def check_wordlist():
    fh = open('enable1.txt')

    total = 0
    count = 0

    for line in fh:
        total = total + 1
        if check(line.strip()):
            count = count + 1

    fh.close()

    print "Exceptions: " + str(total - count)

def main():
    print check("a") # = > true
    print check("zombie") # = > true
    print check("transceiver") # = > true
    print check("veil") # = > false
    print check("icier") # = > false

    check_wordlist()  # => 2169

main()
