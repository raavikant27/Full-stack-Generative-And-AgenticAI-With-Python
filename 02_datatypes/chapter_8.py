# Chapter 8: Lists - Mutable Data Types

# Lists are mutable sequences that can be changed after creation
# They are similar to arrays in other languages

# Basic List Creation
ingredients = ["water", "milk", "black tea"]
print(f"Ingredients are: {ingredients}")

# Append - adds element at the end
ingredients.append("sugar")
print(f"After append: {ingredients}")

# Remove - removes specific element
ingredients.remove("water")
print(f"After remove: {ingredients}")

# Basic Ingredients and Spice Options
chai_ingredients = ["water", "milk"]
spice_options = ["ginger", "cardamom"]

# Extend - combines two lists
chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")

# Insert - adds element at specific position (index)
# Position 0 = water, Position 1 = milk, Position 2 = will be black tea
chai_ingredients.insert(2, "black tea")
print(f"After insert: {chai_ingredients}")

# Pop - removes and returns the last element
last_added = chai_ingredients.pop()
print(f"Last added: {last_added}")
print(f"After pop: {chai_ingredients}")

# Reverse - reverses the list in place
chai_ingredients.reverse()
print(f"After reverse: {chai_ingredients}")

# Sort - sorts the list in place (alphabetically for strings)
chai_ingredients.sort()
print(f"After sort: {chai_ingredients}")

# Max and Min functions
sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

# Operator Overloading
# Plus operator combines lists
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]
liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {liquid_mix}")

# Multiply operator repeats list elements
strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")

# Byte Array (rarely used but exists)
# Converts string to byte array for manipulation
raw_spice_data = bytearray(b"cinnamon")
print(f"Bytes: {raw_spice_data}")

# Replace in byte array - returns new array
raw_spice_data = raw_spice_data.replace(b"cinna", b"cardamom")
print(f"After replace: {raw_spice_data}")
