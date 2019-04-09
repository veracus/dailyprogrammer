def fit3(crate_x, crate_y, crate_z, box_x, box_y, box_z):
    max_x_y_config = fit2(crate_x, crate_y, box_x, box_y)
    max_depth = (crate_z // box_z)

    return(max_x_y_config * max_depth)

def fit2(crate_x, crate_y, box_x, box_y):
    not_rotated = fit1(crate_x, crate_y, box_x, box_y)
    rotated = fit1(crate_x, crate_y, box_y, box_x)

    return (max(not_rotated, rotated))

def fit1(crate_x, crate_y, box_x, box_y):
    return ((crate_x // box_x) * (crate_y // box_y))

print(fit1(25, 18, 6, 5)) # = > 12
print(fit1(10, 10, 1, 1)) # = > 100
print(fit1(12, 34, 5, 6)) # = > 10
print(fit1(12345, 678910, 1112, 1314)) # = > 5676
print(fit1(5, 100, 6, 1)) # = > 0
print(fit2(25, 18, 6, 5)) # = > 15
print(fit2(12, 34, 5, 6)) # = > 12
print(fit2(12345, 678910, 1112, 1314)) # = > 5676
print(fit2(5, 5, 3, 2)) # = > 2
print(fit2(5, 100, 6, 1)) # = > 80
print(fit2(5, 5, 6, 1)) # = > 0
