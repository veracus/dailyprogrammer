import random


def readFromFile(fileName):
    with open(fileName) as fileHandler:
        content = fileHandler.readlines()

    return [line.strip() for line in content]


def roll(shortHand):
    pieces = shortHand.split('d')

    numberOfRolls = int(pieces[0])
    numberOfSides = int(pieces[1])

    rolls = []

    for index in range(0, numberOfRolls):
        rolls.append(random.randint(1, numberOfSides))

    generateOutput(rolls)


def generateOutput(rolls):
    total = str(sum(rolls))
    eachRolls = ', '.join(str(roll) for roll in rolls)

    print total + ": " + eachRolls


def main():
    lines = readFromFile('input.txt')

    for shortHand in lines:
        roll(shortHand)


main()
