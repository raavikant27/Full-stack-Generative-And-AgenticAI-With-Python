# Chapter 10: Dictionaries - Key-Value Pairs

# Dictionary provides NAMED indexing instead of numeric (0, 1, 2...)
# Syntax: {key: value} or dict(key=value)

# Method 1: Using dict() function
chai_order = dict(type="masala chai", size="large", sugar=2)
print(f"Chai order: {chai_order}")

# Method 2: Using empty dictionary and adding items
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# Accessing data by key
print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")

# Deleting items using del
del chai_recipe["liquid"]
print(f"After deletion: {chai_recipe}")

# Membership testing - check if key exists
print(f"Is sugar in order? {'sugar' in chai_order}")

print("\n--- Keys, Values, and Items ---")
# Redefining order for demonstration
chai_order = dict(type="ginger chai", size="medium", sugar=1)

# Get all keys
print(f"Order details (keys): {chai_order.keys()}")

# Get all values
print(f"Order details (values): {chai_order.values()}")

# Get all items as key-value pairs (returns list of tuples)
print(f"Order details (items): {chai_order.items()}")

print("\n--- Pop and PopItem Methods ---")
# popitem() - removes and returns last inserted key-value pair
last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")
print(f"After popitem: {chai_order}")

print("\n--- Update Method ---")
# Adding base back for update demo
chai_recipe = {"base": "black tea"}

# Update dictionary with another dictionary
spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(spices)
print(f"Updated chai recipe: {chai_recipe}")

print("\n--- Safe Access with get() Method ---")
# Redefine order
chai_order = dict(type="ginger chai", size="medium", sugar=1)

# Direct access (crashes if key doesn't exist)
chai_size = chai_order["size"]
print(f"Chai size: {chai_size}")

# Safe access with get() - doesn't crash if key missing
customer_note = chai_order.get("customer_note", "No note was given by the customer")
print(f"Customer note: {customer_note}")

# get() with existing key
size_safe = chai_order.get("size", "default")
print(f"Size (using get): {size_safe}")

print("\n--- Nested Dictionaries ---")
# Dictionary can contain other dictionaries
tea_shop = {
    "chai": {
        "Masala": {"price": 30, "available": True},
        "Ginger": {"price": 25, "available": True},
        "Plain": {"price": 20, "available": False}
    },
    "location": "Mumbai",
    "rating": 4.5
}
print(f"Tea shop: {tea_shop}")
print(f"Masala chai price: {tea_shop['chai']['Masala']['price']}")
print(f"Shop rating: {tea_shop['rating']}")

print("\n--- Looping Through Dictionary ---")
# Loop through keys
print("Types of chai:")
for chai_type in chai_order.keys():
    print(f"  - {chai_type}")

# Loop through values
print("\nOrder values:")
for value in chai_order.values():
    print(f"  - {value}")

# Loop through key-value pairs
print("\nComplete order:")
for key, value in chai_order.items():
    print(f"  {key}: {value}")

print("\n--- Dictionary Methods Summary ---")
# setdefault() - get value, or set if key doesn't exist
chai_order.setdefault("customer_name", "Anonymous")
print(f"After setdefault: {chai_order}")

# copy() - create shallow copy
order_copy = chai_order.copy()
print(f"Order copy: {order_copy}")

# clear() - remove all items
test_dict = {"a": 1, "b": 2}
test_dict.clear()
print(f"Cleared dictionary: {test_dict}")

# fromkeys() - create dictionary from sequence of keys
keys = ["Masala", "Ginger", "Green"]
default_stock = dict.fromkeys(keys, 10)
print(f"Default stock: {default_stock}")

print("\n--- Dictionary Comprehension ---")
# Create dictionary using comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print(f"Squared numbers: {squared_numbers}")

# Filter dictionary
prices = {"Masala": 30, "Ginger": 25, "Green": 20, "Black": 15}
affordable = {k: v for k, v in prices.items() if v <= 25}
print(f"Affordable chai (<=25): {affordable}")

print("\n--- Union Operations (Python 3.9+) ---")
# Merge dictionaries using | operator
default_order = {"type": "plain", "size": "medium"}
custom_order = {"size": "large", "sugar": 2}
final_order = default_order | custom_order
print(f"Merged order: {final_order}")

# Update in place using |=
default_order |= {"extra": "milk"}
print(f"Updated with |=: {default_order}")


print(f"Is sugar in the order?{'sugar' in chai_order}")


chai_order={"type":"Ginger chai","Size":"Medium","sugar":1}
print(f"Order details(keys):{chai_order.keys() }")
print(f"Order details(values):{chai_order.values() }")
print(f"Order details(item):{chai_order.items() }")

last_item=chai_order.popitem()
print(f"Removed last itme:{last_item}")


extra_spices={"cardamom":"cloves","ginger":"sliced"}
chai_recipe.update(extra_spices)


print(f"updated chai recipe:{chai_recipe}")
chai_size=chai_order["Size"]
print(f"Chai size:{chai_size}")

