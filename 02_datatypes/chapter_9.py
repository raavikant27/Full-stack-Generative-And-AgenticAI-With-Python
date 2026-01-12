# Chapter 9: Sets - Unique Collections

# Sets are mathematical collections that store UNIQUE elements only
# No duplicates allowed - that's the key feature!

# Basic Set Creation - using curly braces {}
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

print(f"Essential spices: {essential_spices}")
print(f"Optional spices: {optional_spices}")

# UNION (|) - Combines all unique elements from both sets
# Gets everything from both, but no duplicates
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")
# Notice: ginger appears only once, not twice!

# INTERSECTION (&) - Only common elements between sets
# What exists in BOTH sets
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")
# Only ginger is common

# DIFFERENCE (-) - Elements in first set but NOT in second
# What's unique to essential spices
only_in_essential = essential_spices - optional_spices
print(f"Only in essential: {only_in_essential}")
# cardamom and cinnamon (ginger removed because it's common)

# MEMBERSHIP TESTING - Check if element exists
print(f"Is cloves in essential spices? {'cloves' in essential_spices}")
print(f"Is cloves in optional spices? {'cloves' in optional_spices}")
print(f"Is ginger in essential spices? {'ginger' in essential_spices}")

# Additional Set Operations
print("\n--- Additional Set Operations ---")

# Symmetric Difference (^) - Elements in either set, but NOT in both
unique_spices = essential_spices ^ optional_spices
print(f"Unique to each (not common): {unique_spices}")

# Add elements to set
essential_spices.add("turmeric")
print(f"After adding turmeric: {essential_spices}")

# Remove elements from set
essential_spices.remove("turmeric")
print(f"After removing turmeric: {essential_spices}")

# Discard (like remove, but doesn't raise error if not found)
essential_spices.discard("saffron")  # Won't error even if not present
print(f"After discard: {essential_spices}")

# Clear all elements
test_set = {"a", "b", "c"}
test_set.clear()
print(f"Cleared set: {test_set}")

# FROZENSET - Immutable version of set
frozen_spices = frozenset(["cardamom", "ginger", "cinnamon"])
print(f"\nFrozen set: {frozen_spices}")
# frozen_spices.add("cloves")  # This would cause ERROR - can't modify!

# Set from list (automatically removes duplicates!)
numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers_list)
print(f"\nOriginal list: {numbers_list}")
print(f"Unique numbers: {unique_numbers}")

# Checking subset and superset relationships
small_set = {"ginger", "cardamom"}
large_set = {"ginger", "cardamom", "cinnamon", "cloves"}

print(f"\nIs small_set subset of large_set? {small_set.issubset(large_set)}")
print(f"Is large_set superset of small_set? {large_set.issuperset(small_set)}")
print(f"Are they disjoint (no common elements)? {small_set.isdisjoint(large_set)}")
