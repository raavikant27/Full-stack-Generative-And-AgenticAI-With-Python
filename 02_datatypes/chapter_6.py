# ============================================
# STRINGS - Immutable Text Data
# ============================================

# Basic string definition
chai_type = "Ginger Chai"
customer_name = "Priya"

# String formatting
print(f"Order for {customer_name}: {chai_type} please!")

# ============================================
# STRING INDEXING & SLICING
# ============================================

chai_description = "Aromatic and bold"

# Indexing: Each character has a position (starts at 0)
# A r o m a t i c   a n d   b o l d
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

# Slicing syntax: string[start:end:step]
# - start: starting index (inclusive)
# - end: ending index (exclusive - not included!)
# - step: how many characters to skip

# Get first word "Aromatic" (positions 0-7, but 8 to include 7)
first_word = chai_description[0:8]
print(f"First word: {first_word}")

# Pythonic way - omit 0 if starting from beginning
first_word = chai_description[:8]
print(f"First word (Pythonic): {first_word}")

# Step parameter - every 2nd character
first_word_skip = chai_description[0:8:2]
print(f"Every 2nd character: {first_word_skip}")  # Aoai

# Get last word "bold" (starts at position 12, go to end)
last_word = chai_description[12:]
print(f"Last word: {last_word}")

# Adding more text - slicing still works
chai_description = "Aromatic and bold more"
last_word = chai_description[12:]
print(f"Last word with more text: {last_word}")

# ============================================
# REVERSING STRINGS - [::-1] trick
# ============================================

# Step of -1 reverses the entire string
chai_description = "Aromatic and bold"
reversed_chai = chai_description[::-1]
print(f"Reversed string: {reversed_chai}")  # dlob dna citamorA

# ============================================
# ENCODING & DECODING - Special Characters
# ============================================

# String with special character (é)
label_text = "Chai é special"

# Encode to UTF-8 (converts to bytes)
encoded_label = label_text.encode('utf-8')
print(f"Encoded label: {encoded_label}")  # b'Chai \xc3\xa9 special'

# Decode back to string
decoded_label = encoded_label.decode('utf-8')
print(f"Decoded label: {decoded_label}")  # Chai é special

# Why encoding matters:
# - Handles special characters (accents, tildes, etc.)
# - Essential for international languages (Hindi, Japanese, Chinese, etc.)
# - Ensures characters display correctly across systems
# - Use UTF-8 as standard encoding

# ============================================
# NEGATIVE INDEXING
# ============================================

chai = "Masala Chai"
# Negative indices start from the end
# M  a  s  a  l  a     C  h  a  i
# 0  1  2  3  4  5  6  7  8  9  10
#-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1

print(f"Last character: {chai[-1]}")      # i
print(f"Second last: {chai[-2]}")         # a
print(f"Last 4 chars: {chai[-4:]}")       # Chai

# ============================================
# STRING IMMUTABILITY
# ============================================

# Strings are IMMUTABLE - cannot be changed in place
original = "Tea"
print(f"Original ID: {id(original)}")

# This creates a NEW string, doesn't modify original
new_string = original + " Time"
print(f"New string ID: {id(new_string)}")  # Different ID!

# This would cause an error:
# original[0] = "C"  # TypeError: 'str' object does not support item assignment
