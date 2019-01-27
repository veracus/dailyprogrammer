def funnel(word, sub_word):
    for x in range(0, len(word)):
        test_word = word[:x] + word[x+1:]

        if (test_word == sub_word):
            return True
    
    return False

def main():
    print funnel("leave", "eave")
    print funnel("reset", "rest")
    print funnel("dragoon", "dragon")
    print funnel("eave", "leave")
    print funnel("sleet", "lets")
    print funnel("skiff", "ski")

main()
