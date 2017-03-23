import random


def area(base, side, height):
    return base * side + base * height / 2


area1 = area(5, 3, 2)  # should be approx.
print(area1)
area2 = area(2, 5, 1)  # should be approx.
print(area2)
area3 = area(3, 3, 3)  # should be approx.
print(area3)

random_side = random.randint(2, 5)
random_base = random.randint(random_side, 5)  # Constraint
random_height = random.randint(1, 3)  # Small roof

print(area(random_base, random_side, random_height))
