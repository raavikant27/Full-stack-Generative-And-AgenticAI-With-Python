# ============================================
# REAL NUMBERS (FLOATING POINT) - Decimal Precision
# ============================================

import sys

# Floating point precision issues
ideal_temp = 95.5
current_temp = 95.49999999999
difference_temp = ideal_temp - current_temp
print(f"Ideal temp is: {ideal_temp}")
print(f"Current temperature: {current_temp}")
print(f"Difference temperature: {difference_temp}")

# More manageable precision
current_temp = 95.49
difference_temp = ideal_temp - current_temp
print(f"\nWith less precision:")
print(f"Difference temperature: {difference_temp}")

# System float information
print(f"\nFloat info: {sys.float_info}")

# ============================================
# ADVANCED: Fractions and Decimal (optional)
# ============================================

# Fractions - for exact rational numbers
from fractions import Fraction
pizza_slices = Fraction(3, 8)  # 3/8 of a pizza
print(f"\nPizza slices (fraction): {pizza_slices}")

# Decimal - for high precision decimal calculations
from decimal import Decimal
price = Decimal("19.99")
tax_rate = Decimal("0.08")
total_price = price + (price * tax_rate)
print(f"Total price with tax: {total_price}")

# Note: Complex numbers exist (2+3j) but rarely used in general programming
complex_num = 2 + 3j
print(f"\nComplex number: {complex_num}")
