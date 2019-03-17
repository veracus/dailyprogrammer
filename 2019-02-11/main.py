def generate_output(numbers):
    final = []

    for number in numbers:
        final.append(str(int(number)+1))

    return (''.join(final))

print (generate_output('998'))
