def load_list():
    words = []

    fh = open('enable1.txt', 'r')
    
    for line in fh:
        words.append(line.strip())

    fh.close()

    return words 

def generate_possible_words(word):
    possibilities = []
    word_list = list(word)

    if (len(word)) > 1:
        for x in range(0, len(word_list)):
            possibilities.append(''.join(word_list[:x] + word_list[x+1:]))
    
    return possibilities

def funnel2(word, depth = 1):
    dictionary = load_list()
    possibilities = generate_possible_words(word)

    count = 0

    for possibility in dictionary:
        if possibility in possibilities:
            count += 1
            return funnel2(possibility, depth + 1)
    
    if (count == 0):
        return depth   

def main():
    print funnel2("gnash") # = > 4
    print funnel2("princesses") # = > 9
    print funnel2("turntables") # = > 5
    print funnel2("implosive") # = > 1
    print funnel2("programmer") # = > 2

main()
