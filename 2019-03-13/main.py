def leaps(first_year, second_year):
    count = 0

    for year in range(first_year, second_year):
        is_leap = False

        if (year % 4 == 0 and year % 100 != 0):
            count += 1
            continue
        
        if (year % 900 in [200, 600]):
            count += 1
            continue
    
    return count

print (leaps(2016, 2017))           # = > 1
print (leaps(2019, 2020))           # = > 0
print (leaps(1900, 1901))           # = > 0
print (leaps(2000, 2001))           # = > 1
print (leaps(2800, 2801))           # = > 0
print (leaps(123456, 123456))       # = > 0
print (leaps(1234, 5678))           # = > 1077
print (leaps(123456, 7891011))      # = > 1881475
