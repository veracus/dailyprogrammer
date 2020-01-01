codes = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split(
    ' ')
letters = list('abcdefghijklmnopqrstuvwxyz')

cipher = dict(zip(letters, codes))


def smorse(word):
    encoded = []

    for character in word:
        encoded.append(cipher[character])

    print(''.join(encoded))


def main():
    smorse("sos")  # = > "...---..."
    smorse("daily")  # = > "-...-...-..-.--"
    smorse("programmer")  # = > ".--..-.-----..-..-----..-."
    smorse("bits")  # = > "-.....-..."
    smorse("three")  # = > "-.....-..."


main()
