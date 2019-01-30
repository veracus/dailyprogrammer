def read_from_file():
    lines = []
    lengths = []

    fh = open('input.txt', 'r')

    for line in fh:
        word = line.strip()
        lengths.append(len(word))
        lines.append(word)

    fh.close()

    return lines, max(lengths)


def print_correctly(lines, max_len, perc_variance):
    paragraphs = []

    paragraph = ''
    for line in lines:
        paragraph += ' ' + line

        if (len(line) < (max_len * perc_variance)) and (line[-1] == '.'):
            paragraphs.append(paragraph)
            paragraph = ''

    if (len(paragraph) > 0):
        paragraphs.append(paragraph)

    print '\n\n'.join(paragraphs)

def main():
    lines, max_len = read_from_file()

    print_correctly(lines, max_len, 0.90)

main()
