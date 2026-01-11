# ============================================
# BOOLEANS - True/False Values
# ============================================

# Basic boolean values
is_boiling = True
temperature_hot = False

# Boolean arithmetic - True = 1, False = 0 (upcasting)
stir_count = 5
total_actions = stir_count + is_boiling  # 5 + 1 = 6
print(f"Total actions: {total_actions}")

# Converting to boolean with bool()
milk_present = 0
print(f"Is there milk? {bool(milk_present)}")  # False

milk_present = 1
print(f"Is there milk? {bool(milk_present)}")  # True

milk_present = 11
print(f"Is there milk? {bool(milk_present)}")  # True (any non-zero is True)

milk_present = "Hitesh"
print(f"Is there milk? {bool(milk_present)}")  # True (non-empty string is True)

milk_present = None
print(f"Is there milk? {bool(milk_present)}")  # False (None is False)

# ============================================
# LOGICAL OPERATIONS - and, or, not
# ============================================

# AND operator - both conditions must be True
water_hot = True
tea_added = False
can_serve_chai = water_hot and tea_added
print(f"Can serve chai: {can_serve_chai}")  # False

tea_added = True
can_serve_chai = water_hot and tea_added
print(f"Can serve chai: {can_serve_chai}")  # True

# OR operator - at least one condition must be True
has_tea = False
has_coffee = True
can_serve_beverage = has_tea or has_coffee
print(f"Can serve beverage: {can_serve_beverage}")  # True

# NOT operator - reverses the boolean value
is_raining = True
go_outside = not is_raining
print(f"Can go outside: {go_outside}")  # False
