# ============================================
# TUPLES - Immutable Ordered Collections
# ============================================

# Creating a tuple with parentheses
masala_spices = ("cardamom", "clove", "cinnamon")
print(f"Main masala spices: {masala_spices}")

# ============================================
# UNPACKING TUPLES
# ============================================

# Extract values into individual variables
spice_one, spice_two, spice_three = masala_spices
print(f"Spice 1: {spice_one}")
print(f"Spice 2: {spice_two}")
print(f"Spice 3: {spice_three}")

# ============================================
# TUPLE WITHOUT PARENTHESES (Python Magic!)
# ============================================

# You can create tuples without parentheses
# Python automatically treats comma-separated values as tuples
ginger_ratio, cardamom_ratio = 2, 1
print(f"\nRatio is for ginger: {ginger_ratio} and cardamom: {cardamom_ratio}")

# ============================================
# SWAPPING VARIABLES (Python Superpower!)
# ============================================

# Swap values without needing a third variable
# This is only possible because of tuples!
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio after swap - ginger: {ginger_ratio} and cardamom: {cardamom_ratio}")

# ============================================
# MEMBERSHIP TESTING
# ============================================

# Check if item exists in tuple using 'in' keyword
print(f"\nIs 'ginger' in masala_spices? {'ginger' in masala_spices}")  # False
print(f"Is 'cinnamon' in masala_spices? {'cinnamon' in masala_spices}")  # True

# Case sensitive - be careful!
print(f"Is 'Cinnamon' in masala_spices? {'Cinnamon' in masala_spices}")  # False

# ============================================
# TUPLE IMMUTABILITY
# ============================================

# Tuples CANNOT be changed after creation
tea_types = ("masala", "ginger", "cardamom")
print(f"\nOriginal tea types: {tea_types}")

# This would cause an ERROR:
# tea_types[0] = "green"  # TypeError: 'tuple' object does not support item assignment

# You can only create a new tuple
tea_types = ("green", "black", "white")
print(f"New tea types (new tuple created): {tea_types}")

# ============================================
# TUPLE WITH ONE ELEMENT (Tricky!)
# ============================================

# Need a trailing comma for single element tuple
single_spice = ("cardamom",)  # This is a tuple
not_a_tuple = ("cardamom")     # This is just a string!

print(f"\nSingle spice type: {type(single_spice)}")  # <class 'tuple'>
print(f"Not a tuple type: {type(not_a_tuple)}")     # <class 'str'>

# ============================================
# TUPLE INDEXING & SLICING (Like Strings!)
# ============================================

spices = ("cardamom", "clove", "cinnamon", "black pepper", "bay leaf")

# Indexing
print(f"\nFirst spice: {spices[0]}")    # cardamom
print(f"Last spice: {spices[-1]}")      # bay leaf

# Slicing
print(f"First three: {spices[:3]}")     # ('cardamom', 'clove', 'cinnamon')
print(f"Last two: {spices[-2:]}")       # ('black pepper', 'bay leaf')

# ============================================
# TUPLE PACKING & UNPACKING (Advanced)
# ============================================

# Packing - creating tuple
ingredients = "tea", "milk", "sugar", "water"
print(f"\nPacked ingredients: {ingredients}")

# Unpacking with * (rest operator)
main_ingredient, *others = ingredients
print(f"Main: {main_ingredient}")       # tea
print(f"Others: {others}")              # ['milk', 'sugar', 'water']

# ============================================
# TUPLE METHODS (Only 2!)
# ============================================

numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - count occurrences
print(f"\nCount of 2: {numbers.count(2)}")  # 3

# index() - find first occurrence
print(f"First index of 2: {numbers.index(2)}")  # 1

# ============================================
# WHY USE TUPLES?
# ============================================

# 1. Immutable - Data protection
coordinates = (28.6139, 77.2090)  # Delhi coordinates - shouldn't change

# 2. Faster than lists
import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print(f"\nList size: {sys.getsizeof(my_list)} bytes")
print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")  # Smaller!

# 3. Can be used as dictionary keys (lists can't!)
location_data = {
    (28.6139, 77.2090): "Delhi",
    (19.0760, 72.8777): "Mumbai"
}
print(f"\nLocation lookup: {location_data[(28.6139, 77.2090)]}")
