def solve(row):
    newRow = []

    for position in range(0, len(row)):
        if position == (len(row) - 1):
            newRow.append(abs(row[position] - row[0]))
        else:
            newRow.append(abs(row[position] - row[position + 1]))

    if row != newRow:
        print newRow
        solve(newRow)


def main():
    tuple = (10, 12, 41, 62, 31)

    solve(list(tuple))


if __name__ == '__main__':
    main()
