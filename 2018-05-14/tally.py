def score(series):
    scores = {}

    for letter in list(series):
        if (letter.isupper()):
            if (letter.lower() in scores):
                scores[letter.lower()] = scores[letter.lower()] - 1
            else:
                scores[letter.lower()] = -1
        else:
            if (letter.lower() in scores):
                scores[letter.lower()] = scores[letter.lower()] + 1
            else:
                scores[letter.lower()] = 1

    output = []
    
    for key in sorted(scores, key=scores.get, reverse=True):
        output.append(key + ":" + str(scores[key]))

    print ', '.join(output)

def main():
    score('abcde')  # => a: 1, c: 1, b: 1, e: 1, d: 1
    score('dbbaCEDbdAacCEAadcB')  # => b: 2, d: 2, a: 1, c: 0, e: -2
    score('EbAAdbBEaBaaBBdAccbeebaec')  # => c: 3, d: 2, a: 1, e: 1, b: 0

main()
