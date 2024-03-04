"""

"""

numerator = int(input("Please input numerator: "))
denominator = int(input("Please input denominator: "))

num_factors = [x for x in range(1, numerator + 1) if numerator % x == 0]
denom_factors = [y for y in range(1, denominator + 1) if denominator % y == 0]

max_factor = 0

for x in num_factors:
    for y in denom_factors:
        if x == y and x > max_factor:
            max_factor = x

print(num_factors)
print(denom_factors)
print("Orignial fraction: ", numerator, "/", denominator)
if max_factor == 0:
    print("Fraction cannot be simplified.")
else:
    print("Simplified fraction: ", int(numerator / max_factor), "/", int(denominator / max_factor))