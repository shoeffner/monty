import math

level = 31
strength = 20

damage = math.floor(5 + 1.15 * strength + 0.1 * level)

print(damage)
# Or: (5 + 1.15 * strength + 0.1 * level) // 1
