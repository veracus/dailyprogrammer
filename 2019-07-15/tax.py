def tax(income):
    totalTax = 0

    limit = [100000, 30000, 10000]
    taxation = [0.40, 0.25, 0.10]

    if (income <= 0):
        return totalTax

    for bracket in range(len(limit)):
        if (income > limit[bracket]):
            totalTax += (income - limit[bracket]) * taxation[bracket]
            income = limit[bracket]

    return int(totalTax)


print(tax(-500))  # = > 0
print(tax(0))  # = > 0
print(tax(10000))  # = > 0
print(tax(10009))  # = > 0
print(tax(10010))  # = > 1
print(tax(12000))  # = > 200
print(tax(56789))  # = > 8697
print(tax(1234567))  # = > 473326
