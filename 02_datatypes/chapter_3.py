# ============================================
# INTEGERS - Whole Numbers
# ============================================

# Basic arithmetic operations
black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is: {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is: {remaining_tea}")

# True division (/) - gives decimal result
milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(f"Milk per serving is: {milk_per_serving}")

# Floor division (//) - removes decimal, gives whole number
total_teabags = 7
pots = 4
bags_per_pot = total_teabags // pots
print(f"Whole tea bags per pot: {bags_per_pot}")

# Modulo operator (%) - gives remainder of division
total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods: {leftover_pods}")

# Exponentiation (**) - power operation
base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"Scaled flavor strength is: {powerful_flavor}")

# Underscore for readability (ignored by Python)
total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")

