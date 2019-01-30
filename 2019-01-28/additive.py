def sum_digits(number, count=0):
    if (len(list(str(number))) == 1):
        return count
    
    sum = 0
    numbers = list(str(number))

    for value in numbers:
        sum += int(value)

    return sum_digits(sum, count + 1)


def main():
    print sum_digits(13) # -> 1
    print sum_digits(1234) # -> 2
    print sum_digits(9876) # -> 2
    print sum_digits(199) # -> 3

main()
