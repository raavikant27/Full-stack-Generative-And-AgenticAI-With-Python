# Python Data Types & Objects - Complete Interview Guide

## 📚 Table of Contents
1. [Objects in Python](#objects-in-python)
2. [Mutability vs Immutability](#mutability-vs-immutability)
3. [Numbers - Integers](#numbers---integers)
4. [Numbers - Booleans](#numbers---booleans)
5. [Numbers - Floats](#numbers---floats)
6. [Quick Interview Cheat Sheet](#quick-interview-cheat-sheet)

---

## 1. Everything is an Object in Python

In Python, **everything is an object**. Every object has three fundamental properties:

### Object Properties:
1. **Identity** - A unique ID (like a fingerprint)
2. **Type** - What kind of object it is (number, string, list, etc.)
3. **Value** - The actual data it holds

```
┌─────────────┐
│   OBJECT    │
├─────────────┤
│ Identity    │ → Unique ID
│ Type        │ → Data type
│ Value       │ → Actual data
└─────────────┘
```

---

## 2. Mutability vs Immutability

### Mutable = Changeable ✅
- The object's value CAN be changed in memory
- Same identity after modification
- Examples: Lists, Sets, Dictionaries

### Immutable = Not Changeable ❌
- The object's value CANNOT be changed in memory
- Different identity after "modification" (actually creates new object)
- Examples: Numbers, Strings, Tuples

---

## 3. **CRITICAL RULE**: Check with Identity, NOT Value ⚠️

### ❌ WRONG WAY:
```python
# Never check mutability by comparing values
sugar = 2
sugar = 12  # Value changed, so it's mutable? NO!
```

### ✅ CORRECT WAY:
```python
# Always check mutability using id()
sugar = 2
print(id(sugar))  # e.g., 140234567890680

sugar = 12
print(id(sugar))  # e.g., 140234567893360 (DIFFERENT ID!)
```

**If ID changes → Immutable (new object created)**  
**If ID stays same → Mutable (same object modified)**

---

## 4. Immutable Example: Numbers

```python
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")
print(f"ID of 2: {id(2)}")

sugar_amount = 12  # Creates NEW object, changes reference
print(f"Final sugar: {sugar_amount}")
print(f"ID of 12: {id(12)}")  # Different ID!
```

### What Happens Behind the Scenes:

```
Step 1: sugar_amount = 2
Memory: [2] ← sugar_amount points here
        ID: xxx680

Step 2: sugar_amount = 12
Memory: [2] (still exists, unchanged)
        ID: xxx680
        
        [12] ← sugar_amount NOW points here
        ID: xxx360

Result: Reference changed, NOT the value!
```

**Key Point**: The number `2` never changed in memory. Python created a new object `12` and changed the reference.

---

## 5. Mutable Example: Sets

```python
spice_mix = set()
print(f"Initial ID: {id(spice_mix)}")  # e.g., 140234567890944

spice_mix.add("ginger")
spice_mix.add("cardamom")
print(f"After adding ID: {id(spice_mix)}")  # Same: 140234567890944

print(f"Spice mix: {spice_mix}")  # {'ginger', 'cardamom'}
```

### What Happens Behind the Scenes:

```
Step 1: spice_mix = set()
Memory: [{}] ← spice_mix points here
        ID: xxx944

Step 2: spice_mix.add("ginger")
Memory: [{'ginger'}] ← SAME object, modified
        ID: xxx944 (SAME!)

Step 3: spice_mix.add("cardamom")
Memory: [{'ginger', 'cardamom'}] ← SAME object, modified
        ID: xxx944 (SAME!)
```

**Key Point**: The set itself is modified in memory. The ID stays the same.

---

## 6. Common Data Types by Mutability

### Immutable Types:
- `int` - Numbers (1, 2, 100)
- `float` - Decimals (3.14, 2.5)
- `str` - Strings ("hello", "python")
- `tuple` - Fixed collections ((1, 2, 3))
- `bool` - Boolean (True, False)

### Mutable Types:
- `list` - Lists ([1, 2, 3])
- `set` - Sets ({1, 2, 3})
- `dict` - Dictionaries ({"key": "value"})

---

## 7. Interview Key Points 📝

### Q: What makes something mutable or immutable?
**A**: Whether the object can be changed in memory after creation.

### Q: How do you check if something is mutable?
**A**: Check the `id()` before and after modification. If ID stays same → Mutable. If ID changes → Immutable.

### Q: Why can't we change numbers in Python?
**A**: Numbers are immutable. When you "change" a number variable, Python creates a new number object and updates the reference.

### Q: What's the difference between changing a value and changing a reference?
**A**: 
- **Changing value**: Modifying the object in memory (mutable)
- **Changing reference**: Pointing to a different object (immutable)

---

## 8. Practical Code Examples

### Example 1: Checking Identity
```python
# Immutable (Number)
x = 5
print(id(x))  # 123456789
x = 10
print(id(x))  # 987654321 (Different!)

# Mutable (List)
my_list = [1, 2, 3]
print(id(my_list))  # 555555555
my_list.append(4)
print(id(my_list))  # 555555555 (Same!)
```

### Example 2: Why Identity Matters
```python
# This looks like it changed, but did it really?
name = "Chai"
print(id(name))  # 111111111

name = "Tea"
print(id(name))  # 222222222 (New object!)

# Strings are immutable - new object created each time
```

---

## 9. Memory Visualization

### Immutable (Numbers):
```
sugar = 2          sugar = 12
┌───┐              ┌───┐
│ 2 │ ← sugar     │ 2 │ (unchanged)
└───┘              └───┘
ID: 680            
                   ┌────┐
                   │ 12 │ ← sugar (new reference)
                   └────┘
                   ID: 360
```

### Mutable (Sets):
```
spices = {}        spices.add("ginger")    spices.add("cardamom")
┌────┐             ┌────────────┐          ┌──────────────────────┐
│ {} │ ← spices   │ {'ginger'} │← spices  │ {'ginger','cardamom'}│← spices
└────┘             └────────────┘          └──────────────────────┘
ID: 944            ID: 944 (SAME!)         ID: 944 (SAME!)
```

---

## 10. Summary for Interviews 🎯

1. **Everything in Python is an object** with identity, type, and value
2. **Mutable** = Can change in memory (lists, sets, dicts)
3. **Immutable** = Cannot change in memory (numbers, strings, tuples)
4. **Always check mutability with `id()`, never with value**
5. **Immutable objects create new objects when "modified"**
6. **Mutable objects modify the same object in memory**

---

# 🔢 Numbers in Python - Complete Guide

## 1. Types of Numbers

Python supports 4 types of numbers:

1. **Integers** (`int`) - Whole numbers
2. **Booleans** (`bool`) - True/False values
3. **Floats** (`float`) - Real numbers (decimals)
4. **Complex** (`complex`) - Imaginary numbers (rarely used)

---

## 2. INTEGERS - Whole Numbers

### Basic Arithmetic Operations

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `14 + 3` | `17` |
| `-` | Subtraction | `14 - 3` | `11` |
| `*` | Multiplication | `14 * 3` | `42` |
| `/` | True Division | `7 / 4` | `1.75` |
| `//` | Floor Division | `7 // 4` | `1` |
| `%` | Modulo (Remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### True Division vs Floor Division

```python
# True Division (/) - Always returns float
milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(milk_per_serving)  # 1.75

# Floor Division (//) - Removes decimal, returns whole number
total_teabags = 7
pots = 4
bags_per_pot = total_teabags // pots
print(bags_per_pot)  # 1 (not 1.75)
```

### Modulo Operator (%) - Finding Remainders

```python
# Perfect for finding leftovers
total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(leftover_pods)  # 1

# Common use: Check if number is even/odd
number = 10
if number % 2 == 0:
    print("Even")  # This prints
else:
    print("Odd")
```

### Exponentiation (**)

```python
# Power operation
base = 2
scale = 3
result = base ** scale
print(result)  # 8 (2 * 2 * 2)
```

### Underscore for Readability

```python
# Python ignores underscores in numbers
total_leaves = 1_000_000_000
print(total_leaves)  # 1000000000

# Improves readability, doesn't affect value
price = 99_999
population = 7_800_000_000
```

---

## 3. BOOLEANS - True/False Values

### Basic Concepts

```python
# Only two values: True or False (capital first letter)
is_boiling = True
is_cold = False
```

### Boolean Arithmetic (Upcasting)

```python
# True = 1, False = 0
stir_count = 5
is_boiling = True
total_actions = stir_count + is_boiling
print(total_actions)  # 6 (5 + 1)
```

### Converting to Boolean with bool()

```python
# Falsy values (convert to False)
print(bool(0))         # False
print(bool(""))        # False
print(bool([]))        # False
print(bool({}))        # False
print(bool(None))      # False

# Truthy values (convert to True)
print(bool(1))         # True
print(bool(11))        # True
print(bool("Hitesh"))  # True
print(bool([1, 2]))    # True
```

### Logical Operators

#### AND - Both conditions must be True
```python
water_hot = True
tea_added = False
can_serve_chai = water_hot and tea_added
print(can_serve_chai)  # False (both must be True)

tea_added = True
can_serve_chai = water_hot and tea_added
print(can_serve_chai)  # True (both are True)
```

#### OR - At least one condition must be True
```python
has_tea = False
has_coffee = True
can_serve_beverage = has_tea or has_coffee
print(can_serve_beverage)  # True (one is True)
```

#### NOT - Reverses the boolean value
```python
is_raining = True
go_outside = not is_raining
print(go_outside)  # False
```

### Truth Table for Logical Operators

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| T | T | T | T | F |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

---

## 4. FLOATS - Real/Decimal Numbers

### Basic Usage

```python
# Numbers with decimal precision
ideal_temp = 95.5
current_temp = 95.49
difference = ideal_temp - current_temp
print(difference)  # 0.010000000000005116
```

### Precision Issues

```python
# Binary representation causes precision issues
current_temp = 95.49999999999
difference = ideal_temp - current_temp
print(difference)  # 1.000444171950221e-11 (not exactly 0)
```

### System Float Information

```python
import sys
print(sys.float_info)
# Shows max, min, precision limits of your system
```

### Advanced: Decimal for Precision

```python
from decimal import Decimal

# Use for financial calculations
price = Decimal("19.99")
tax_rate = Decimal("0.08")
total = price + (price * tax_rate)
print(total)  # 21.5892 (exact)

# DON'T use float for money!
price = 19.99
tax_rate = 0.08
total = price + (price * tax_rate)
print(total)  # 21.5892 (may have precision errors)
```

### Advanced: Fractions for Exact Ratios

```python
from fractions import Fraction

# Exact rational numbers
pizza_slice = Fraction(3, 8)  # 3/8 of a pizza
print(pizza_slice)  # 3/8

half = Fraction(1, 2)
third = Fraction(1, 3)
result = half + third
print(result)  # 5/6
```

---

## 5. Quick Interview Cheat Sheet

### Common Questions

**Q1: What are all numeric types in Python?**  
✅ `int`, `float`, `complex`, `bool` (technically numeric)

**Q2: Difference between `/` and `//`?**  
✅ `/` = true division (returns float: `7/4 = 1.75`)  
✅ `//` = floor division (returns int: `7//4 = 1`)

**Q3: What is modulo `%` used for?**  
✅ Finding remainders: `10 % 3 = 1`  
✅ Check even/odd: `n % 2 == 0`  
✅ Cycling through values: `index % length`

**Q4: What's Boolean upcasting?**  
✅ `True` converts to `1`, `False` converts to `0` in arithmetic

**Q5: What values are Falsy in Python?**  
✅ `0`, `None`, `""`, `[]`, `{}`, `False`

**Q6: Why `0.1 + 0.2 != 0.3` in Python?**  
✅ Binary representation of decimals isn't exact. Use `Decimal` for precision.

**Q7: When to use `Decimal` vs `float`?**  
✅ `Decimal` - Money, finance, exact calculations  
✅ `float` - Scientific computing, speed matters

**Q8: What's the difference between `and` and `&`?**  
✅ `and` - Logical operator for booleans  
✅ `&` - Bitwise operator for binary operations

---

## 6. Code Templates for Interviews

### Template 1: Division Operations
```python
# True division
result = 7 / 4      # 1.75

# Floor division
result = 7 // 4     # 1

# Get both quotient and remainder
quotient = 7 // 4   # 1
remainder = 7 % 4   # 3
```

### Template 2: Boolean Logic
```python
# Check multiple conditions
if user_logged_in and has_credit_card and is_paid_user:
    allow_checkout()

# Check at least one condition
if has_tea or has_coffee:
    serve_beverage()
```

### Template 3: Precision Handling
```python
from decimal import Decimal

# Financial calculations
def calculate_total(price, tax_rate):
    price = Decimal(str(price))
    tax_rate = Decimal(str(tax_rate))
    return price + (price * tax_rate)
```

---

## 7. Pro Tips 💡

1. **Use `//` for integer division** - Faster than `int(a/b)`
2. **Use `_` in large numbers** - `1_000_000` is more readable
3. **Use `Decimal` for money** - Avoid float precision errors
4. **Use `%` for cycling** - `index % length` keeps values in range
5. **Booleans are integers** - `True + True = 2`
6. **Short-circuit evaluation** - `and`/`or` stop early
   ```python
   # If first is False, second isn't evaluated
   if False and expensive_function():
       pass  # expensive_function() never runs
   ```

---

## 8. Common Mistakes to Avoid ❌

1. **Using `==` for float comparison**
   ```python
   # ❌ Wrong
   if 0.1 + 0.2 == 0.3:  # False!
   
   # ✅ Correct
   import math
   if math.isclose(0.1 + 0.2, 0.3):  # True
   ```

2. **Using floats for money**
   ```python
   # ❌ Wrong
   total = 0.1 + 0.2  # 0.30000000000000004
   
   # ✅ Correct
   from decimal import Decimal
   total = Decimal("0.1") + Decimal("0.2")  # 0.3
   ```

3. **Confusing `/` and `//`**
   ```python
   # ❌ Wrong assumption
   result = 7 / 4  # Expecting 1, get 1.75
   
   # ✅ Use floor division
   result = 7 // 4  # 1
   ```

---

## 9. Interview Code Challenges

### Challenge 1: Check if number is even
```python
def is_even(n):
    return n % 2 == 0

print(is_even(10))  # True
print(is_even(7))   # False
```

### Challenge 2: Calculate bill with tip
```python
from decimal import Decimal

def calculate_bill(subtotal, tip_percentage):
    subtotal = Decimal(str(subtotal))
    tip = Decimal(str(tip_percentage))
    tip_amount = subtotal * (tip / 100)
    return subtotal + tip_amount

total = calculate_bill(50.00, 15)
print(total)  # 57.50
```

### Challenge 3: Check access permissions
```python
def can_access(is_logged_in, has_permission, is_active):
    return is_logged_in and has_permission and is_active

access = can_access(True, True, False)
print(access)  # False
```

---

## 10. Final Summary 🎯

| Type | Example | Mutable? | Common Use |
|------|---------|----------|------------|
| `int` | `42` | No | Counting, indexing |
| `float` | `3.14` | No | Measurements, calculations |
| `bool` | `True` | No | Conditions, flags |
| `Decimal` | `Decimal("19.99")` | No | Money, precision |
| `Fraction` | `Fraction(1, 3)` | No | Exact ratios |

**Remember:**
- All numbers are **immutable**
- Use `//` for integer division, `/` for float division
- Use `%` for remainders
- Use `Decimal` for money
- `True = 1`, `False = 0`
- Master `and`, `or`, `not` for logic

---

# 📝 Strings in Python - Complete Guide

## 1. String Basics

### What are Strings?
- **Immutable** sequence of characters
- Anything in quotes is a string: `"text"` or `'text'`
- Cannot be changed in place (creates new object)

```python
chai_type = "Ginger Chai"
customer_name = 'Priya'

# String formatting
print(f"Order for {customer_name}: {chai_type} please!")
```

---

## 2. String Indexing

### Understanding Indexing
- Each character has a position (index)
- **Indexing starts at 0** (not 1!)
- Negative indices count from the end

```python
text = "Aromatic"
# Positions: 0 1 2 3 4 5 6 7

print(text[0])   # 'A' - first character
print(text[7])   # 'c' - last character
print(text[-1])  # 'c' - last character (negative index)
print(text[-2])  # 'i' - second last
```

### Positive vs Negative Indexing

```
String:  M  a  s  a  l  a     C  h  a  i
Positive: 0  1  2  3  4  5  6  7  8  9  10
Negative:-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1
```

---

## 3. String Slicing

### Syntax: `string[start:end:step]`

| Parameter | Description | Default |
|-----------|-------------|---------|
| `start` | Starting index (inclusive) | `0` |
| `end` | Ending index (exclusive) | `len(string)` |
| `step` | How many to skip | `1` |

**CRITICAL: The `end` index is NOT included!**

### Common Slicing Patterns

```python
text = "Aromatic and bold"

# Get first word (positions 0-7, need 8 to include position 7)
first = text[0:8]      # "Aromatic"
first = text[:8]       # Same (0 is default)

# Get last word (from position 12 to end)
last = text[12:]       # "bold"

# Every 2nd character
skip = text[0:8:2]     # "Aoai"

# Every character (step=1 is default)
all_chars = text[0:8:1]  # "Aromatic"
```

### Visual Example

```python
text = "Aromatic and bold"
#       01234567890123456

text[0:8]    → "Aromatic"  (positions 0-7)
text[9:12]   → "and"       (positions 9-11)
text[12:]    → "bold"      (position 12 to end)
text[:8]     → "Aromatic"  (start to position 7)
text[:]      → entire string (copy)
```

---

## 4. Reversing Strings

### The `[::-1]` Trick

```python
chai = "Masala Chai"
reversed_chai = chai[::-1]
print(reversed_chai)  # "iahC alasaM"
```

**How it works:**
- `start` = omitted (default: start from end)
- `end` = omitted (default: go to beginning)  
- `step` = `-1` (go backwards)

### Interview Question: Reverse a String
```python
# Method 1: Slicing (fastest)
text = "Python"
reversed_text = text[::-1]  # "nohtyP"

# Method 2: Using reversed() and join()
reversed_text = "".join(reversed(text))

# Method 3: Loop (slowest)
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
```

---

## 5. String Encoding & Decoding

### Why Encoding Matters
- Handles special characters: é, ñ, ü, etc.
- Essential for international languages (Hindi, Japanese, Chinese)
- Ensures correct display across systems

### UTF-8 Encoding

```python
# String with special character
text = "Chai é special"

# Encode to bytes
encoded = text.encode('utf-8')
print(encoded)  # b'Chai \xc3\xa9 special'

# Decode back to string
decoded = encoded.decode('utf-8')
print(decoded)  # "Chai é special"
```

### Common Encodings

| Encoding | Use Case |
|----------|----------|
| `utf-8` | **Most common**, supports all languages |
| `utf-16` | Used in Windows internally |
| `ascii` | English only (limited) |
| `latin-1` | Western European languages |

---

## 6. String Immutability

### Strings Cannot Be Changed

```python
chai = "Tea"
print(id(chai))  # 123456789

# This creates a NEW string
chai = chai + " Time"
print(id(chai))  # 987654321 (Different!)

# This would cause an ERROR
chai[0] = "C"  # TypeError: 'str' object does not support item assignment
```

### Why Strings are Immutable
1. **Performance** - Can be optimized in memory
2. **Security** - Cannot be accidentally modified
3. **Hashable** - Can be used as dictionary keys

---

## 7. Quick Interview Cheat Sheet

### Common Questions

**Q1: How do you reverse a string in Python?**  
✅ `text[::-1]` (fastest method)

**Q2: What's the difference between indexing and slicing?**  
✅ Indexing: Single character `text[0]`  
✅ Slicing: Substring `text[0:5]`

**Q3: Are strings mutable or immutable?**  
✅ **Immutable** - cannot be changed in place

**Q4: What does `text[2:5]` return?**  
✅ Characters at positions 2, 3, 4 (position 5 NOT included)

**Q5: How to get last character of a string?**  
✅ `text[-1]`

**Q6: What's the difference between `'` and `"`?**  
✅ No difference - both create strings. Use one inside the other:  
   `"He said 'hello'"` or `'She said "hi"'`

**Q7: How to handle special characters?**  
✅ Use `.encode('utf-8')` and `.decode('utf-8')`

**Q8: What's the step parameter in slicing?**  
✅ How many characters to skip. `text[::2]` gets every 2nd character

---

## 8. Common String Operations

### Length
```python
text = "Masala Chai"
length = len(text)  # 11
```

### Concatenation
```python
first = "Masala"
last = "Chai"
full = first + " " + last  # "Masala Chai"
```

### Repetition
```python
laugh = "ha" * 3  # "hahaha"
```

### Checking Membership
```python
text = "Masala Chai"
"Chai" in text     # True
"Coffee" in text   # False
```

---

## 9. Code Templates for Interviews

### Template 1: Extract First and Last Word
```python
sentence = "The quick brown fox"
words = sentence.split()
first = words[0]   # "The"
last = words[-1]   # "fox"
```

### Template 2: Check Palindrome
```python
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("racecar"))     # True
print(is_palindrome("A man a plan a canal Panama"))  # True
```

### Template 3: Count Characters
```python
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)  # {'h':1, 'e':1, 'l':3, 'o':2, ' ':1, 'w':1, 'r':1, 'd':1}
```

---

## 10. Common Mistakes to Avoid ❌

### Mistake 1: Forgetting End is Exclusive
```python
text = "Python"
# ❌ Wrong: Expecting "Pyth" but positions 0-3 give only 0,1,2
result = text[0:3]  # "Pyt" (not "Pyth")

# ✅ Correct: Need 4 to include position 3
result = text[0:4]  # "Pyth"
```

### Mistake 2: Trying to Modify String
```python
text = "Hello"
# ❌ Wrong: Strings are immutable
text[0] = "h"  # TypeError!

# ✅ Correct: Create new string
text = "h" + text[1:]  # "hello"
```

### Mistake 3: Not Using UTF-8 for Special Characters
```python
text = "Café"
# ❌ Wrong: May cause issues on different systems
encoded = text.encode('ascii')  # UnicodeEncodeError!

# ✅ Correct: Use UTF-8
encoded = text.encode('utf-8')  # Works!
```

---

## 11. Pro Tips 💡

1. **Use `[::-1]` to reverse strings** - Fastest method
2. **Always use UTF-8 encoding** for international text
3. **Remember: end index is exclusive** - `text[0:5]` gives positions 0-4
4. **Negative indices are powerful** - `text[-3:]` gets last 3 characters
5. **Strings are immutable** - Every modification creates a new string
6. **Use f-strings for formatting** - `f"Hello {name}"` (Python 3.6+)
7. **Slicing never raises IndexError** - `text[100:200]` returns `""` if too long

---

## 12. Interview Code Challenges

### Challenge 1: Extract File Extension
```python
def get_extension(filename):
    return filename[filename.rfind('.')+1:]

print(get_extension("document.pdf"))  # "pdf"
```

### Challenge 2: Title Case
```python
def to_title_case(text):
    return " ".join(word.capitalize() for word in text.split())

print(to_title_case("hello world"))  # "Hello World"
```

### Challenge 3: Remove Vowels
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

print(remove_vowels("hello"))  # "hll"
```

---

## 13. Final Summary 🎯

| Operation | Syntax | Example | Result |
|-----------|--------|---------|--------|
| **Index** | `s[i]` | `"Chai"[0]` | `'C'` |
| **Slice** | `s[i:j]` | `"Chai"[0:2]` | `'Ch'` |
| **Slice with step** | `s[i:j:k]` | `"Chai"[::2]` | `'Ca'` |
| **Reverse** | `s[::-1]` | `"Chai"[::-1]` | `'iahC'` |
| **Length** | `len(s)` | `len("Chai")` | `4` |
| **Concat** | `s1 + s2` | `"Tea" + " Time"` | `'Tea Time'` |
| **Repeat** | `s * n` | `"Ha" * 3` | `'HaHaHa'` |
| **Encode** | `s.encode()` | `"Café".encode('utf-8')` | `b'Caf\xc3\xa9'` |

**Key Takeaways:**
- Strings are **immutable** - cannot change in place
- Indexing starts at **0**
- End index in slicing is **exclusive** (not included)
- Use **UTF-8** for international characters
- **`[::-1]`** reverses strings
- Negative indices count from the end

---

# 🔒 Tuples in Python - Complete Interview Guide

## 1. What are Tuples?

### Definition
- **Immutable** ordered collection of items
- Defined using **parentheses** `( )`
- Cannot be changed after creation (data protection)
- Faster and more memory-efficient than lists

```python
# Creating a tuple
masala_spices = ("cardamom", "clove", "cinnamon")
```

### Tuples vs Lists - Quick Comparison

| Feature | Tuple | List |
|---------|-------|------|
| **Syntax** | `(1, 2, 3)` | `[1, 2, 3]` |
| **Mutable** | ❌ No | ✅ Yes |
| **Speed** | ⚡ Faster | 🐌 Slower |
| **Memory** | 💾 Less | 💾 More |
| **Use Case** | Fixed data | Dynamic data |
| **Dict Key** | ✅ Yes | ❌ No |

---

## 2. Creating Tuples

### Method 1: With Parentheses
```python
spices = ("cardamom", "clove", "cinnamon")
```

### Method 2: Without Parentheses (Tuple Packing)
```python
# Python automatically creates tuple with comma separation
spices = "cardamom", "clove", "cinnamon"
```

### Method 3: Using tuple() Constructor
```python
spices = tuple(["cardamom", "clove", "cinnamon"])
```

### ⚠️ Single Element Tuple (TRICKY!)
```python
# ✅ Correct - need trailing comma
single = ("cardamom",)
type(single)  # <class 'tuple'>

# ❌ Wrong - this is just a string!
not_tuple = ("cardamom")
type(not_tuple)  # <class 'str'>
```

---

## 3. Tuple Unpacking (Python Superpower!)

### Basic Unpacking
```python
masala_spices = ("cardamom", "clove", "cinnamon")

# Extract into individual variables
spice1, spice2, spice3 = masala_spices

print(spice1)  # "cardamom"
print(spice2)  # "clove"
print(spice3)  # "cinnamon"
```

### Variable Assignment (Behind the Scenes)
```python
# This works because Python uses tuples internally!
ginger_ratio, cardamom_ratio = 2, 1
# Behind the scenes: (ginger_ratio, cardamom_ratio) = (2, 1)
```

### Advanced Unpacking with * (Rest Operator)
```python
ingredients = ("tea", "milk", "sugar", "water", "cardamom")

# Get first and rest
main, *others = ingredients
print(main)    # "tea"
print(others)  # ['milk', 'sugar', 'water', 'cardamom']

# Get first, last, and middle
first, *middle, last = ingredients
print(first)   # "tea"
print(middle)  # ['milk', 'sugar', 'water']
print(last)    # "cardamom"
```

---

## 4. Variable Swapping (Unique Python Feature!)

### The Traditional Way (Other Languages)
```python
# Need a temporary variable
a = 5
b = 10
temp = a
a = b
b = temp
# a=10, b=5
```

### The Python Way (Using Tuples!)
```python
a = 5
b = 10

# Swap in one line!
a, b = b, a
# a=10, b=5

# What Python does: (a, b) = (b, a) = (10, 5)
```

### Real Example
```python
ginger_ratio = 2
cardamom_ratio = 1
print(f"Before: {ginger_ratio}:{cardamom_ratio}")  # 2:1

# Swap ratios
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"After: {ginger_ratio}:{cardamom_ratio}")   # 1:2
```

---

## 5. Tuple Immutability

### Cannot Modify Tuples
```python
tea_types = ("masala", "ginger", "cardamom")

# ❌ This causes ERROR
tea_types[0] = "green"  # TypeError: 'tuple' object does not support item assignment

# ✅ Can only create new tuple
tea_types = ("green", "black", "white")  # New tuple, different id
```

### Why Immutability Matters
1. **Data Protection** - Prevents accidental changes
2. **Performance** - Faster than lists
3. **Hashable** - Can be dictionary keys
4. **Thread-Safe** - Safe in multi-threading

```python
# Immutable data examples
coordinates = (28.6139, 77.2090)  # GPS coordinates shouldn't change
rgb_color = (255, 0, 0)           # Red color definition
date = (2026, 1, 11)              # Date values are fixed
```

---

## 6. Tuple Indexing & Slicing

### Indexing (Same as Strings/Lists)
```python
spices = ("cardamom", "clove", "cinnamon", "black pepper", "bay leaf")
#          0           1        2           3              4
#         -5          -4       -3          -2             -1

# Positive indexing
print(spices[0])   # "cardamom"
print(spices[2])   # "cinnamon"

# Negative indexing
print(spices[-1])  # "bay leaf"
print(spices[-2])  # "black pepper"
```

### Slicing: `tuple[start:end:step]`
```python
spices = ("cardamom", "clove", "cinnamon", "black pepper", "bay leaf")

spices[:3]      # ('cardamom', 'clove', 'cinnamon')
spices[2:]      # ('cinnamon', 'black pepper', 'bay leaf')
spices[-2:]     # ('black pepper', 'bay leaf')
spices[::2]     # ('cardamom', 'cinnamon', 'bay leaf') - every 2nd
spices[::-1]    # Reversed tuple
```

---

## 7. Membership Testing

### Using 'in' Keyword
```python
masala_spices = ("cardamom", "clove", "cinnamon")

# Check if item exists
"cinnamon" in masala_spices     # True
"ginger" in masala_spices       # False

# Negation
"pepper" not in masala_spices   # True

# ⚠️ Case sensitive!
"Cinnamon" in masala_spices     # False (capital C)
"cinnamon" in masala_spices     # True (lowercase)
```

### Use Cases
```python
# User authentication
allowed_users = ("admin", "moderator", "user")
if username in allowed_users:
    grant_access()

# Valid options
valid_colors = ("red", "green", "blue")
if color in valid_colors:
    apply_color()
```

---

## 8. Tuple Methods (Only 2!)

### Method 1: count()
```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# Count occurrences
numbers.count(2)    # 3
numbers.count(5)    # 1
numbers.count(10)   # 0 (not found)
```

### Method 2: index()
```python
spices = ("cardamom", "clove", "cinnamon", "clove")

# Find first occurrence
spices.index("clove")      # 1
spices.index("cinnamon")   # 2

# Specify search range
spices.index("clove", 2)   # 3 (start searching from index 2)

# ⚠️ ValueError if not found
spices.index("pepper")     # ValueError: tuple.index(x): x not in tuple
```

---

## 9. Why Use Tuples Over Lists?

### Reason 1: Immutability (Data Protection)
```python
# Configuration that shouldn't change
DATABASE_CONFIG = ("localhost", 5432, "mydb")

# GPS coordinates - fixed values
location = (28.6139, 77.2090)
```

### Reason 2: Performance (Faster & Smaller)
```python
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# Memory comparison
sys.getsizeof(my_list)   # 104 bytes
sys.getsizeof(my_tuple)  # 80 bytes (24% smaller!)

# Tuples are also faster to create and iterate
```

### Reason 3: Dictionary Keys (Hashable)
```python
# ✅ Tuples can be dict keys
location_names = {
    (28.6139, 77.2090): "Delhi",
    (19.0760, 72.8777): "Mumbai"
}

# ❌ Lists cannot be dict keys
# location_names = {
#     [28.6139, 77.2090]: "Delhi"  # TypeError: unhashable type: 'list'
# }
```

### Reason 4: Function Returns
```python
def get_user_info():
    return "Hitesh", 30, "India"  # Returns tuple

name, age, country = get_user_info()  # Unpacking
```

---

## 10. Interview Questions & Answers

### Q1: What is a tuple in Python?
**Answer (30 seconds):**
"A tuple is an immutable ordered collection in Python, defined using parentheses. Unlike lists, tuples cannot be modified after creation. For example, `colors = ('red', 'green', 'blue')` creates a tuple of three colors. Tuples are faster and use less memory than lists, making them ideal for fixed data like coordinates or configurations."

### Q2: How do you create a single-element tuple?
**Answer:**
"You need a trailing comma: `single = ('item',)`. Without the comma, Python treats it as a string in parentheses: `not_tuple = ('item')` is just a string."

### Q3: What's tuple unpacking?
**Answer:**
"Tuple unpacking extracts tuple values into variables in one line:
```python
spices = ('cardamom', 'clove', 'cinnamon')
spice1, spice2, spice3 = spices
```
This is why Python can swap variables easily: `a, b = b, a` works because it's actually `(a, b) = (b, a)`."

### Q4: Difference between tuple and list?
**Answer:**
"Main differences:
1. **Mutability**: Tuples are immutable, lists are mutable
2. **Speed**: Tuples are faster
3. **Memory**: Tuples use less memory
4. **Syntax**: Tuples use `()`, lists use `[]`
5. **Use case**: Tuples for fixed data, lists for dynamic data"

### Q5: Can tuples be used as dictionary keys?
**Answer:**
"Yes! Tuples are hashable (immutable), so they can be dictionary keys:
```python
coordinates = {
    (28.6139, 77.2090): 'Delhi',
    (19.0760, 72.8777): 'Mumbai'
}
```
Lists cannot be keys because they're mutable."

### Q6: What methods are available for tuples?
**Answer:**
"Only 2 methods:
- `count()`: Count occurrences
- `index()`: Find first occurrence
Unlike lists (which have append, remove, etc.), tuples have fewer methods because they're immutable."

### Q7: How to swap variables in Python?
**Answer:**
"Python uses tuple unpacking for elegant swapping:
```python
a, b = 5, 10
a, b = b, a  # Now a=10, b=5
```
No temporary variable needed! Python creates `(b, a)` tuple and unpacks it."

### Q8: When should you use tuples?
**Answer:**
"Use tuples when:
1. Data shouldn't change (coordinates, RGB colors, dates)
2. You need better performance
3. Using as dictionary keys
4. Returning multiple values from functions
5. Protecting data from modification"

---

## 11. Code Templates for Interviews

### Template 1: Multiple Return Values
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5])
print(f"Min: {minimum}, Max: {maximum}")
```

### Template 2: Coordinate System
```python
# Store locations as tuples
cities = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946)
}

lat, lon = cities["Delhi"]
print(f"Delhi coordinates: {lat}, {lon}")
```

### Template 3: Configuration Settings
```python
# Immutable configuration
DB_CONFIG = (
    "localhost",  # host
    5432,         # port
    "postgres",   # database
    "utf8"        # encoding
)

host, port, db, encoding = DB_CONFIG
```

---

## 12. Common Mistakes to Avoid

### Mistake 1: Forgetting Trailing Comma
```python
# ❌ Wrong - this is a string
single = ("item")
type(single)  # <class 'str'>

# ✅ Correct - need comma
single = ("item",)
type(single)  # <class 'tuple'>
```

### Mistake 2: Trying to Modify Tuple
```python
colors = ("red", "green", "blue")

# ❌ Wrong - TypeError
colors[0] = "yellow"

# ✅ Correct - create new tuple
colors = ("yellow", "green", "blue")
```

### Mistake 3: Wrong Unpacking Count
```python
spices = ("cardamom", "clove", "cinnamon")

# ❌ Wrong - ValueError: too many values to unpack
a, b = spices

# ✅ Correct - match the count
a, b, c = spices
```

---

## 13. Pro Tips 💡

1. **Use tuples for fixed data** - Prevents bugs from accidental changes
2. **Faster iteration** - Tuples iterate ~10% faster than lists
3. **Memory efficient** - Use 20-30% less memory than lists
4. **Named tuples** - Use `collections.namedtuple` for readable code
5. **Tuple concatenation** - `tuple1 + tuple2` creates new tuple
6. **Repetition** - `('a',) * 3` gives `('a', 'a', 'a')`
7. **Always use comma** for single-element tuples

---

## 14. Advanced: Named Tuples

```python
from collections import namedtuple

# Create a named tuple class
Spice = namedtuple('Spice', ['name', 'quantity', 'unit'])

# Use it
cardamom = Spice('Cardamom', 2, 'grams')
print(cardamom.name)      # 'Cardamom'
print(cardamom.quantity)  # 2
print(cardamom[0])        # 'Cardamom' (still works like tuple)
```

---

## 15. Final Summary 🎯

| Feature | Details |
|---------|---------|
| **Definition** | Immutable ordered collection |
| **Syntax** | `(item1, item2, item3)` |
| **Single Element** | `(item,)` - needs comma! |
| **Unpacking** | `a, b, c = (1, 2, 3)` |
| **Swapping** | `a, b = b, a` |
| **Membership** | `'item' in tuple` |
| **Methods** | `count()`, `index()` only |
| **Indexing** | `tuple[0]`, `tuple[-1]` |
| **Slicing** | `tuple[1:3]`, `tuple[::-1]` |
| **Immutable** | ✅ Cannot change after creation |

### Interview One-Liner:
**"Tuples are immutable ordered collections using parentheses, faster and more memory-efficient than lists, perfect for fixed data like coordinates or configurations, and enable Python's elegant variable swapping."**

---

*Last Updated: January 2026*

---

## Remember:
> "If the ID changes, it's a new object (immutable).  
> If the ID stays same, it's the same object modified (mutable)."

---

## 🔄 Lists - Mutable Sequences (Complete Guide)

### What is a List?
- **Mutable sequence** that can be changed after creation
- Known as **arrays** in other programming languages
- Can store multiple items of different types
- Defined using square brackets `[]`
- Elements can be reordered, modified, added, or removed

### List vs Tuple:
| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | ✅ Yes | ❌ No |
| Methods | Many (append, insert, etc.) | Few (count, index) |
| Use Case | Dynamic data | Fixed data |

---

## 📝 List Creation & Basic Operations

### Creating Lists
```python
# Empty list
empty = []

# List with items
ingredients = ["water", "milk", "tea"]

# Mixed types
mixed = [1, "hello", 3.14, True]

# From other sequences
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
```

---

## 🛠️ Essential List Methods

### 1. **append(element)** - Add to End
```python
ingredients = ["water", "milk"]
ingredients.append("sugar")
# Result: ["water", "milk", "sugar"]
```
- Adds element at the **end** of list
- Modifies list in-place
- Returns `None`

---

### 2. **insert(index, element)** - Add at Position
```python
chai = ["water", "milk", "ginger"]
chai.insert(2, "black tea")
# Result: ["water", "milk", "black tea", "ginger"]
```
- Adds element at **specific index**
- Shifts existing elements to the right
- Index is 0-based

#### Index Reference:
```
["water", "milk", "ginger"]
   ↓        ↓        ↓
  [0]      [1]      [2]
```

---

### 3. **remove(element)** - Remove by Value
```python
items = ["water", "milk", "sugar", "water"]
items.remove("water")
# Result: ["milk", "sugar", "water"]
```
- Removes **first occurrence** only
- Raises `ValueError` if element not found
- Works regardless of position

---

### 4. **pop([index])** - Remove and Return
```python
items = ["water", "milk", "sugar"]
last = items.pop()
# last = "sugar"
# items = ["water", "milk"]

first = items.pop(0)
# first = "water"
# items = ["milk"]
```
- Removes element at index (default: last)
- **Returns** the removed element
- Useful when you need the value

---

### 5. **extend(iterable)** - Combine Lists
```python
base = ["water", "milk"]
spices = ["ginger", "cardamom"]
base.extend(spices)
# Result: ["water", "milk", "ginger", "cardamom"]
```
- Adds all elements from another list
- Modifies original list
- Different from `append()` which adds the list as single element

---

### 6. **reverse()** - Reverse Order
```python
items = ["water", "milk", "tea"]
items.reverse()
# Result: ["tea", "milk", "water"]
```
- Reverses list **in-place**
- Does NOT return anything (returns `None`)
- Modifies original list

---

### 7. **sort()** - Sort Elements
```python
numbers = [3, 1, 4, 2]
numbers.sort()
# Result: [1, 2, 3, 4]

words = ["tea", "water", "milk"]
words.sort()
# Result: ["milk", "tea", "water"]
```
- Sorts list **in-place** (alphabetically for strings)
- Does NOT return anything
- Optional: `reverse=True` for descending order

---

### 8. **clear()** - Remove All Elements
```python
items = ["water", "milk", "tea"]
items.clear()
# Result: []
```

---

### 9. **count(element)** - Count Occurrences
```python
items = ["water", "milk", "water", "tea"]
count = items.count("water")
# Result: 2
```

---

### 10. **index(element)** - Find Position
```python
items = ["water", "milk", "tea"]
position = items.index("milk")
# Result: 1
```
- Returns index of **first occurrence**
- Raises `ValueError` if not found

---

## 🔢 Built-in Functions for Lists

### max(list) - Maximum Value
```python
sugar_levels = [1, 2, 3, 4, 5]
maximum = max(sugar_levels)
# Result: 5
```

### min(list) - Minimum Value
```python
sugar_levels = [1, 2, 3, 4, 5]
minimum = min(sugar_levels)
# Result: 1
```

### len(list) - List Length
```python
items = ["water", "milk", "tea"]
length = len(items)
# Result: 3
```

### sum(list) - Sum of Numbers
```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
# Result: 15
```

---

## ➕ Operator Overloading with Lists

### What is Operator Overloading?
- When operators (like `+` or `*`) perform more than one task
- Originally designed for numbers
- Also work with lists in Python

---

### Plus (+) Operator - Concatenation
```python
base = ["water", "milk"]
extra = ["ginger"]
combined = base + extra
# Result: ["water", "milk", "ginger"]
```
- Creates **new list** (doesn't modify originals)
- Combines two lists

---

### Multiply (*) Operator - Repetition
```python
brew = ["tea"] * 3
# Result: ["tea", "tea", "tea"]

multi = ["tea", "water"] * 2
# Result: ["tea", "water", "tea", "water"]
```
- Repeats list elements
- Maintains order in each repetition

---

## 📍 List Indexing & Slicing

### 0-Based Indexing
```python
items = ["water", "milk", "tea", "sugar"]
#          [0]     [1]     [2]     [3]
#         [-4]    [-3]    [-2]    [-1]

first = items[0]    # "water"
last = items[-1]    # "sugar"
```

### Slicing
```python
items = ["water", "milk", "tea", "sugar"]

# [start:end]
items[1:3]    # ["milk", "tea"]

# [start:]
items[2:]     # ["tea", "sugar"]

# [:end]
items[:2]     # ["water", "milk"]

# [::step]
items[::2]    # ["water", "tea"]
items[::-1]   # ["sugar", "tea", "milk", "water"]
```

---

## 🔄 Mutable vs Immutable Behavior

### Immutable (Numbers, Strings)
```python
x = 5
print(id(x))  # 140234567890
x = 10        # Creates NEW object
print(id(x))  # 140234567999  ← Different ID
```

### Mutable (Lists)
```python
my_list = [1, 2, 3]
print(id(my_list))  # 140234567890
my_list.append(4)   # Modifies SAME object
print(id(my_list))  # 140234567890  ← Same ID
```

---

## 💾 Byte Arrays (Advanced)

### What is bytearray?
- **Mutable** sequence of bytes (0-255)
- Used for binary data manipulation
- Rarely used in everyday programming

### Syntax
```python
data = bytearray(b"text")
```

### Important Rules:
1. Methods return **new bytearray** (must reassign)
2. Requires `b` prefix for byte literals
3. Similar methods to strings (replace, capitalize, etc.)

### Example
```python
raw = bytearray(b"cinnamon")
raw = raw.replace(b"cinna", b"cardamom")
# Must reassign to capture new bytearray
print(raw)  # bytearray(b'cardamommon')
```

### When to Use:
- Binary file operations
- Network protocols
- Low-level data manipulation
- Character encoding conversions

---

## 🎯 Real-World Use Cases

### E-commerce
```python
# Sort products by price
prices = [29.99, 19.99, 39.99, 9.99]
prices.sort()
# Show lowest to highest

min_price = min(prices)
max_price = max(prices)
```

### Shopping Cart
```python
cart = ["laptop", "mouse"]
cart.append("keyboard")
cart.extend(["monitor", "speakers"])
```

### Inventory Management
```python
stock = ["item1", "item2", "item3"]
sold = stock.pop(0)  # Remove and track sold item
stock.insert(0, "new_item")  # Add new stock at beginning
```

---

## ⚡ Best Practices & Tips

### DO ✅
- Use `append()` when adding single item to end
- Use `extend()` when combining lists
- Use `insert()` when position matters
- Use `pop()` when you need the removed element
- Use `list comprehensions` for creating filtered/transformed lists

### DON'T ❌
- Don't use `append()` to combine lists (use `extend()`)
- Don't forget: `reverse()` and `sort()` return `None`
- Don't modify list while iterating over it
- Don't use `+` in loops (inefficient, use `extend()`)

---

## 🧪 Common Patterns

### Check if element exists
```python
if "milk" in ingredients:
    print("Has milk")
```

### Remove duplicates
```python
unique = list(set(my_list))
```

### Flatten nested list
```python
nested = [[1, 2], [3, 4]]
flat = [item for sublist in nested for item in sublist]
# Result: [1, 2, 3, 4]
```

### Copy a list
```python
# Shallow copy
new_list = old_list.copy()
# or
new_list = old_list[:]
# or
new_list = list(old_list)
```

---

## 📊 Quick Reference Table

| Method | Returns | Modifies List | Purpose |
|--------|---------|---------------|---------|
| `append()` | None | ✅ | Add to end |
| `insert()` | None | ✅ | Add at position |
| `remove()` | None | ✅ | Remove by value |
| `pop()` | Element | ✅ | Remove & return |
| `extend()` | None | ✅ | Combine lists |
| `reverse()` | None | ✅ | Reverse order |
| `sort()` | None | ✅ | Sort in place |
| `clear()` | None | ✅ | Remove all |
| `count()` | Integer | ❌ | Count occurrences |
| `index()` | Integer | ❌ | Find position |

---

## 🎓 Interview Questions & Answers

### Q: What's the difference between append() and extend()?
**A:** `append()` adds a single element (even if it's a list), while `extend()` adds all elements from an iterable.
```python
x = [1, 2]
x.append([3, 4])   # [1, 2, [3, 4]]
y = [1, 2]
y.extend([3, 4])   # [1, 2, 3, 4]
```

### Q: Why do sort() and reverse() return None?
**A:** They modify the list in-place for efficiency. Returning the list would suggest a new list is created, which isn't the case.

### Q: How to copy a list?
**A:** Use `list.copy()`, `list[:]`, or `list(original)`. Assignment (`new = old`) creates a reference, not a copy.

### Q: Are lists faster than tuples?
**A:** No, tuples are faster. Lists need extra overhead for mutability.

---

## 🎯 Interview One-Liner

**"Lists are mutable, ordered collections using square brackets, supporting numerous methods like append/insert/remove, allowing dynamic modifications with the same object ID, ideal for changing data like shopping carts or user inputs, and enabling operator overloading with + for concatenation and * for repetition."**

---

## 🔷 Sets - Unique Mathematical Collections

### What is a Set?
- **Mutable, unordered** collection of **unique** elements
- Based on mathematical set theory
- **No duplicates allowed** - automatically removes duplicates
- Defined using curly braces `{}` or `set()` function
- Elements must be immutable (strings, numbers, tuples - NOT lists)
- **No indexing** - can't access by position (unordered)

### Set vs List vs Tuple:
| Feature | Set | List | Tuple |
|---------|-----|------|-------|
| Syntax | `{1, 2, 3}` | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | ✅ Yes | ✅ Yes | ❌ No |
| Ordered | ❌ No | ✅ Yes | ✅ Yes |
| Duplicates | ❌ No | ✅ Yes | ✅ Yes |
| Indexing | ❌ No | ✅ Yes | ✅ Yes |
| Use Case | Unique items | Dynamic data | Fixed data |

---

## 📐 Mathematical Set Operations (Venn Diagrams)

### Visual Representation:
```
     Set A          Set B
    ┌─────┐        ┌─────┐
    │  A  │        │  B  │
    │   ┌─┼────────┼─┐   │
    │   │ │ A ∩ B  │ │   │  ← Intersection
    │   └─┼────────┼─┘   │
    └─────┘        └─────┘
    └──────────────────────┘
          A ∪ B              ← Union
```

---

## 🛠️ Set Creation

### Creating Sets
```python
# Using curly braces
spices = {"ginger", "cardamom", "cinnamon"}

# Using set() function
numbers = set([1, 2, 3, 4])

# Empty set (must use set(), not {})
empty = set()  # ✅ Correct
empty = {}     # ❌ Wrong - this creates dictionary!

# From string (each character becomes element)
letters = set("hello")
# Result: {'h', 'e', 'l', 'o'}  ← only one 'l'

# Automatic duplicate removal
duplicates = {1, 2, 2, 3, 3, 3}
# Result: {1, 2, 3}  ← duplicates removed automatically
```

---

## ➕ Set Operations (Mathematical)

### 1. **UNION (|)** - Combine All Unique Elements
```python
A = {"cardamom", "ginger", "cinnamon"}
B = {"cloves", "ginger", "black pepper"}
all_spices = A | B
# Result: {"cardamom", "ginger", "cinnamon", "cloves", "black pepper"}
```
- Gets **everything** from both sets
- **No duplicates** - ginger appears only once
- Symbol: `|` (pipe operator)
- Method: `A.union(B)`

**Real-world:** Combining user preferences from multiple sources

---

### 2. **INTERSECTION (&)** - Common Elements Only
```python
A = {"cardamom", "ginger", "cinnamon"}
B = {"cloves", "ginger", "black pepper"}
common = A & B
# Result: {"ginger"}
```
- Gets elements present in **BOTH** sets
- Only overlapping portion (Venn diagram center)
- Symbol: `&` (ampersand)
- Method: `A.intersection(B)`

**Real-world:** Finding common interests between two users

---

### 3. **DIFFERENCE (-)** - Elements in A but NOT in B
```python
A = {"cardamom", "ginger", "cinnamon"}
B = {"cloves", "ginger", "black pepper"}
only_in_A = A - B
# Result: {"cardamom", "cinnamon"}
```
- Gets elements **unique to first set**
- Removes anything that exists in second set
- Symbol: `-` (minus)
- Method: `A.difference(B)`

**Real-world:** Features in premium plan not in basic plan

---

### 4. **SYMMETRIC DIFFERENCE (^)** - Either Set, but NOT Both
```python
A = {"cardamom", "ginger", "cinnamon"}
B = {"cloves", "ginger", "black pepper"}
unique_to_each = A ^ B
# Result: {"cardamom", "cinnamon", "cloves", "black pepper"}
```
- Gets elements in **either set, excluding common**
- Opposite of intersection
- Symbol: `^` (caret)
- Method: `A.symmetric_difference(B)`

**Real-world:** Items unique to each shopping cart

---

## 📝 Set Methods

### Adding Elements

#### add(element) - Add Single Element
```python
spices = {"ginger", "cardamom"}
spices.add("cinnamon")
# Result: {"ginger", "cardamom", "cinnamon"}
```
- Adds one element
- No error if element already exists (silently ignored)

#### update(iterable) - Add Multiple Elements
```python
spices = {"ginger"}
spices.update(["cardamom", "cinnamon"])
# Result: {"ginger", "cardamom", "cinnamon"}
```
- Adds multiple elements from iterable
- Similar to `extend()` for lists

---

### Removing Elements

#### remove(element) - Remove (Error if Not Found)
```python
spices = {"ginger", "cardamom", "cinnamon"}
spices.remove("cardamom")
# Result: {"ginger", "cinnamon"}

spices.remove("cloves")  # ❌ KeyError!
```
- Raises `KeyError` if element doesn't exist

#### discard(element) - Remove (No Error)
```python
spices = {"ginger", "cardamom"}
spices.discard("cinnamon")  # ✅ No error, just does nothing
# Result: {"ginger", "cardamom"}
```
- Safe removal - no error if element missing
- **Preferred** when unsure if element exists

#### pop() - Remove Random Element
```python
spices = {"ginger", "cardamom", "cinnamon"}
removed = spices.pop()
# Returns and removes random element (sets are unordered)
```
- Returns the removed element
- **Warning:** Random element (no guaranteed order)

#### clear() - Remove All Elements
```python
spices = {"ginger", "cardamom"}
spices.clear()
# Result: set()
```

---

## 🔍 Set Relationships & Testing

### Membership Testing (in / not in)
```python
spices = {"ginger", "cardamom", "cinnamon"}

print("ginger" in spices)       # True
print("cloves" in spices)       # False
print("cloves" not in spices)   # True
```

### Subset - Is Every Element of A in B?
```python
A = {"ginger", "cardamom"}
B = {"ginger", "cardamom", "cinnamon", "cloves"}

print(A.issubset(B))    # True
print(A <= B)           # True (alternative syntax)
print(A < B)            # True (proper subset - A ≠ B)
```

### Superset - Does A Contain All Elements of B?
```python
A = {"ginger", "cardamom", "cinnamon", "cloves"}
B = {"ginger", "cardamom"}

print(A.issuperset(B))  # True
print(A >= B)           # True (alternative syntax)
print(A > B)            # True (proper superset - A ≠ B)
```

### Disjoint - No Common Elements?
```python
A = {"ginger", "cardamom"}
B = {"cloves", "cinnamon"}

print(A.isdisjoint(B))  # True (no common elements)

C = {"ginger", "cloves"}
print(A.isdisjoint(C))  # False (ginger is common)
```

---

## ❄️ Frozenset - Immutable Sets

### What is Frozenset?
- **Immutable** version of set
- Cannot add, remove, or modify elements
- Can be used as dictionary keys (regular sets cannot)
- Can be elements of other sets

### Creating Frozenset
```python
# Using frozenset() function
frozen = frozenset(["ginger", "cardamom", "cinnamon"])

# From existing set
regular_set = {"a", "b", "c"}
frozen = frozenset(regular_set)
```

### Operations
```python
frozen1 = frozenset([1, 2, 3])
frozen2 = frozenset([2, 3, 4])

# Can perform set operations
union = frozen1 | frozen2           # Works!
intersection = frozen1 & frozen2     # Works!

# Cannot modify
# frozen1.add(5)      # ❌ AttributeError!
# frozen1.remove(1)   # ❌ AttributeError!
```

### When to Use Frozenset:
- Dictionary keys: `{frozenset([1, 2]): "value"}`
- Set elements: `{frozenset([1, 2]), frozenset([3, 4])}`
- Immutable configuration data
- Hash table keys

---

## 🎯 Real-World Use Cases

### Remove Duplicates from List
```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))
# Result: [1, 2, 3, 4]
```

### Find Common Tags
```python
post1_tags = {"python", "programming", "tutorial"}
post2_tags = {"python", "coding", "tutorial"}
common_tags = post1_tags & post2_tags
# Result: {"python", "tutorial"}
```

### Check User Permissions
```python
user_permissions = {"read", "write", "execute"}
required_permissions = {"read", "write"}

has_access = required_permissions.issubset(user_permissions)
# True - user has all required permissions
```

### Find Missing Skills
```python
required_skills = {"Python", "SQL", "Git"}
candidate_skills = {"Python", "JavaScript", "Git"}
missing = required_skills - candidate_skills
# Result: {"SQL"}
```

### Email List Merge (No Duplicates)
```python
list1 = {"user1@email.com", "user2@email.com"}
list2 = {"user2@email.com", "user3@email.com"}
all_users = list1 | list2
# Result: 3 unique emails
```

---

## ⚡ Performance & Best Practices

### DO ✅
- Use sets for **membership testing** (very fast: O(1))
- Use sets to **remove duplicates** from lists
- Use sets for **mathematical operations** (union, intersection)
- Use frozenset for **immutable** unique collections
- Use sets when **order doesn't matter**

### DON'T ❌
- Don't use sets if you need **indexing** (use list)
- Don't use sets if you need **order preservation** (use list)
- Don't store **mutable objects** (lists, dicts) in sets
- Don't assume any specific **iteration order**

---

## 🔄 Set vs Other Collections

### When to Use Set:
- Need **unique elements only**
- Order doesn't matter
- Fast membership testing
- Mathematical set operations

### When to Use List:
- Need **duplicates**
- Order matters
- Need indexing
- Need to modify by position

### When to Use Tuple:
- Immutable sequence
- Order matters
- Can have duplicates
- Need to hash (use as dict key)

---

## 📊 Quick Reference Table

| Operation | Syntax | Method | Result |
|-----------|--------|--------|--------|
| Union | `A \| B` | `A.union(B)` | All unique elements |
| Intersection | `A & B` | `A.intersection(B)` | Common elements |
| Difference | `A - B` | `A.difference(B)` | In A, not in B |
| Symmetric Diff | `A ^ B` | `A.symmetric_difference(B)` | In either, not both |
| Add element | - | `A.add(x)` | Adds x to A |
| Remove element | - | `A.remove(x)` | Removes x (error if missing) |
| Safe remove | - | `A.discard(x)` | Removes x (no error) |
| Membership | `x in A` | - | True if x in A |
| Subset | `A <= B` | `A.issubset(B)` | Is A subset of B? |
| Superset | `A >= B` | `A.issuperset(B)` | Does A contain B? |
| Disjoint | - | `A.isdisjoint(B)` | No common elements? |

---

## 🧪 Common Patterns

### Check Multiple Conditions
```python
admin_roles = {"admin", "superuser", "moderator"}
user_role = "admin"

if user_role in admin_roles:
    print("Access granted")
```

### Validate Required Fields
```python
required = {"name", "email", "password"}
provided = set(user_data.keys())

missing = required - provided
if missing:
    print(f"Missing fields: {missing}")
```

### Find Duplicates in List
```python
items = [1, 2, 3, 2, 4, 3, 5]
seen = set()
duplicates = set()

for item in items:
    if item in seen:
        duplicates.add(item)
    seen.add(item)
# duplicates: {2, 3}
```

---

## 🎓 Interview Questions & Answers

### Q: What makes sets unique in Python?
**A:** Sets automatically enforce uniqueness - duplicate elements are not allowed. They're unordered and mutable (except frozenset), making them ideal for membership testing and mathematical set operations.

### Q: Why can't you use a list as a set element?
**A:** Lists are mutable (unhashable), and sets require hashable elements. Use tuples or frozensets instead.

### Q: What's the time complexity of membership testing in sets?
**A:** O(1) average case - sets use hash tables internally, making lookups very fast compared to lists O(n).

### Q: Difference between remove() and discard()?
**A:** `remove()` raises KeyError if element doesn't exist; `discard()` does nothing (no error). Use `discard()` when unsure if element exists.

### Q: When should you use frozenset over regular set?
**A:** Use frozenset when you need an immutable set, as a dictionary key, or as an element of another set.

### Q: How to create an empty set?
**A:** Use `set()` - NOT `{}` which creates an empty dictionary!

---

## 🎯 Interview One-Liner

**"Sets are mutable, unordered collections of unique elements using curly braces, supporting mathematical operations like union (|), intersection (&), and difference (-) based on set theory, providing O(1) membership testing, automatically removing duplicates, with frozenset as the immutable variant usable as dictionary keys or set elements."**

---

## 📖 Dictionaries - Named Indexing with Key-Value Pairs

### What is a Dictionary?
- **Mutable, unordered** collection of **key-value pairs**
- Provides **named indexing** instead of numeric (0, 1, 2...)
- Each key maps to a value (like a real dictionary: word → definition)
- Keys must be **unique and immutable** (strings, numbers, tuples)
- Values can be **anything** (any data type, even other dictionaries)
- Defined using curly braces `{}` or `dict()` function
- Python 3.7+: **Insertion order preserved**

### Why Use Dictionaries?
Instead of accessing by position:
```python
# List - numeric indexing
person = ["Hitesh", "Choudhary"]
first_name = person[0]  # Must remember position
```

Use meaningful names:
```python
# Dictionary - named indexing
person = {"first_name": "Hitesh", "last_name": "Choudhary"}
first_name = person["first_name"]  # Self-documenting!
```

### Dictionary vs List vs Set vs Tuple:
| Feature | Dictionary | List | Set | Tuple |
|---------|-----------|------|-----|-------|
| Syntax | `{k: v}` | `[1, 2]` | `{1, 2}` | `(1, 2)` |
| Mutable | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| Ordered | ✅ Yes (3.7+) | ✅ Yes | ❌ No | ✅ Yes |
| Duplicates | Keys: ❌ Values: ✅ | ✅ Yes | ❌ No | ✅ Yes |
| Indexing | By key | By position | ❌ No | By position |
| Use Case | Key-value data | Ordered items | Unique items | Fixed data |

---

## 🛠️ Dictionary Creation

### Method 1: Curly Braces `{}`
```python
# Empty dictionary
empty = {}

# With initial data
chai_order = {
    "type": "masala chai",
    "size": "large",
    "sugar": 2
}

# Mixed value types
person = {
    "name": "Hitesh",
    "age": 30,
    "is_teacher": True,
    "courses": ["Python", "JavaScript"]
}
```

### Method 2: dict() Function
```python
# Using keyword arguments
chai_order = dict(type="masala chai", size="large", sugar=2)

# From list of tuples
items = [("type", "ginger chai"), ("size", "medium")]
chai_order = dict(items)

# From two lists (keys and values)
keys = ["type", "size", "sugar"]
values = ["green tea", "small", 1]
chai_order = dict(zip(keys, values))
```

### Method 3: Dictionary Comprehension
```python
# Create from range
squared = {x: x**2 for x in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squared = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# Result: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

---

## 📝 Accessing Dictionary Data

### Direct Access with [ ]
```python
chai_order = {"type": "masala chai", "size": "large", "sugar": 2}

# Get value by key
chai_type = chai_order["type"]    # "masala chai"
sugar_level = chai_order["sugar"]  # 2

# ⚠️ KeyError if key doesn't exist
customer_note = chai_order["note"]  # ❌ KeyError!
```

### Safe Access with get()
```python
chai_order = {"type": "masala chai", "size": "large"}

# get(key, default) - no error if key missing
sugar = chai_order.get("sugar", 0)  # Returns 0 (default)
chai_type = chai_order.get("type")   # Returns "masala chai"

# Avoids crashes
note = chai_order.get("customer_note", "No note provided")
# Returns "No note provided" instead of crashing
```

**When to use:**
- `[]` - When you're **sure** the key exists
- `get()` - When key **might not exist** (safer)

---

## ➕ Adding & Modifying Data

### Add New Key-Value Pair
```python
chai_recipe = {}

# Add items
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
chai_recipe["sweetener"] = "sugar"

# Result: {"base": "black tea", "liquid": "milk", "sweetener": "sugar"}
```

### Modify Existing Value
```python
chai_order = {"type": "plain", "size": "medium"}

# Change value
chai_order["type"] = "masala chai"  # Overwrites "plain"
chai_order["size"] = "large"

# Result: {"type": "masala chai", "size": "large"}
```

### Using setdefault()
```python
chai_order = {"type": "masala", "size": "large"}

# Set value ONLY if key doesn't exist
chai_order.setdefault("sugar", 1)     # Adds sugar: 1
chai_order.setdefault("type", "plain") # Does nothing (type exists)

# Result: {"type": "masala", "size": "large", "sugar": 1}
```

---

## 🗑️ Removing Data

### del - Delete Key-Value Pair
```python
chai_recipe = {"base": "black tea", "liquid": "milk", "sugar": 2}

# Delete specific key
del chai_recipe["liquid"]
# Result: {"base": "black tea", "sugar": 2}

# ⚠️ KeyError if key doesn't exist
del chai_recipe["spices"]  # ❌ KeyError!
```

### pop(key) - Remove and Return Value
```python
chai_order = {"type": "masala", "size": "large", "sugar": 2}

# Remove and get value
sugar_level = chai_order.pop("sugar")
# sugar_level = 2
# chai_order = {"type": "masala", "size": "large"}

# With default (no error if key missing)
note = chai_order.pop("customer_note", "No note")
# Returns "No note", doesn't crash
```

### popitem() - Remove Last Inserted Pair
```python
chai_order = {"type": "masala", "size": "large", "sugar": 2}

# Remove last item (LIFO - Last In First Out)
last_item = chai_order.popitem()
# last_item = ("sugar", 2)
# chai_order = {"type": "masala", "size": "large"}

# ⚠️ KeyError if dictionary is empty
```

### clear() - Remove All Items
```python
chai_order = {"type": "masala", "size": "large"}
chai_order.clear()
# Result: {}
```

---

## 🔍 Dictionary Methods

### keys() - Get All Keys
```python
chai_order = {"type": "ginger chai", "size": "medium", "sugar": 1}

all_keys = chai_order.keys()
# Result: dict_keys(['type', 'size', 'sugar'])

# Convert to list
key_list = list(chai_order.keys())
# Result: ['type', 'size', 'sugar']
```

### values() - Get All Values
```python
chai_order = {"type": "ginger chai", "size": "medium", "sugar": 1}

all_values = chai_order.values()
# Result: dict_values(['ginger chai', 'medium', 1])

# Convert to list
value_list = list(chai_order.values())
# Result: ['ginger chai', 'medium', 1]
```

### items() - Get Key-Value Pairs as Tuples
```python
chai_order = {"type": "ginger chai", "size": "medium", "sugar": 1}

all_items = chai_order.items()
# Result: dict_items([('type', 'ginger chai'), ('size', 'medium'), ('sugar', 1)])

# Returns list of tuples
item_list = list(chai_order.items())
# Result: [('type', 'ginger chai'), ('size', 'medium'), ('sugar', 1)]
```

### update() - Merge Dictionaries
```python
chai_recipe = {"base": "black tea"}
spices = {"cardamom": "crushed", "ginger": "sliced"}

# Merge spices into chai_recipe
chai_recipe.update(spices)
# Result: {"base": "black tea", "cardamom": "crushed", "ginger": "sliced"}

# Overwrites existing keys
chai_recipe.update({"base": "green tea"})
# Result: {"base": "green tea", ...}
```

### copy() - Create Shallow Copy
```python
original = {"type": "masala", "size": "large"}
copy = original.copy()

# Modify copy
copy["size"] = "small"

# Original unchanged
print(original)  # {"type": "masala", "size": "large"}
print(copy)      # {"type": "masala", "size": "small"}
```

### fromkeys() - Create Dictionary from Keys
```python
# All keys get same default value
keys = ["Masala", "Ginger", "Green"]
stock = dict.fromkeys(keys, 10)
# Result: {"Masala": 10, "Ginger": 10, "Green": 10}

# No default value = None
defaults = dict.fromkeys(["a", "b", "c"])
# Result: {"a": None, "b": None, "c": None}
```

---

## 🔁 Looping Through Dictionaries

### Loop Through Keys (Default)
```python
chai_order = {"type": "masala", "size": "large", "sugar": 2}

# Method 1: Direct iteration
for key in chai_order:
    print(key)
# Output: type, size, sugar

# Method 2: Explicit keys()
for key in chai_order.keys():
    print(key)
# Output: type, size, sugar
```

### Loop Through Values
```python
for value in chai_order.values():
    print(value)
# Output: masala, large, 2
```

### Loop Through Key-Value Pairs
```python
for key, value in chai_order.items():
    print(f"{key}: {value}")
# Output:
# type: masala
# size: large
# sugar: 2
```

---

## 🪆 Nested Dictionaries

### Creating Nested Dictionaries
```python
tea_shop = {
    "chai": {
        "Masala": {"price": 30, "available": True},
        "Ginger": {"price": 25, "available": True},
        "Plain": {"price": 20, "available": False}
    },
    "location": "Mumbai",
    "rating": 4.5
}
```

### Accessing Nested Data
```python
# Access nested values
masala_price = tea_shop["chai"]["Masala"]["price"]
# Result: 30

location = tea_shop["location"]
# Result: "Mumbai"

# Safe nested access
green_price = tea_shop.get("chai", {}).get("Green", {}).get("price", 0)
# Result: 0 (doesn't exist, returns default)
```

### Modifying Nested Data
```python
# Change nested value
tea_shop["chai"]["Plain"]["available"] = True

# Add new nested item
tea_shop["chai"]["Green"] = {"price": 22, "available": True}
```

---

## 🔄 Dictionary Operations (Python 3.9+)

### Union with | (Merge)
```python
default_order = {"type": "plain", "size": "medium"}
custom_order = {"size": "large", "sugar": 2}

# Merge (custom_order overwrites defaults)
final_order = default_order | custom_order
# Result: {"type": "plain", "size": "large", "sugar": 2}
```

### Update with |= (In-Place Merge)
```python
order = {"type": "masala", "size": "medium"}
order |= {"sugar": 2, "ice": False}
# Result: {"type": "masala", "size": "medium", "sugar": 2, "ice": False}
```

---

## ✅ Membership Testing

### Check if Key Exists
```python
chai_order = {"type": "masala", "size": "large", "sugar": 2}

# Check key presence
print("sugar" in chai_order)        # True
print("customer_note" in chai_order) # False

# Check key absence
print("note" not in chai_order)      # True
```

### Check if Value Exists (Slower)
```python
# Check in values
print("masala" in chai_order.values())  # True
print(50 in chai_order.values())         # False
```

---

## 🎯 Real-World Use Cases

### Configuration Settings
```python
config = {
    "host": "localhost",
    "port": 8000,
    "debug": True,
    "database": {
        "host": "db.example.com",
        "user": "admin"
    }
}
```

### User Profile
```python
user = {
    "id": 12345,
    "username": "hitesh",
    "email": "hitesh@example.com",
    "roles": ["admin", "teacher"],
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}
```

### Product Inventory
```python
inventory = {
    "PROD001": {"name": "Laptop", "price": 50000, "stock": 15},
    "PROD002": {"name": "Mouse", "price": 500, "stock": 100},
    "PROD003": {"name": "Keyboard", "price": 1500, "stock": 50}
}
```

### API Response
```python
response = {
    "status": 200,
    "message": "Success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }
}
```

### Counting Occurrences
```python
text = "hello world hello python"
word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

# Result: {"hello": 2, "world": 1, "python": 1}
```

---

## ⚡ Performance & Best Practices

### DO ✅
- Use dictionaries for **key-value mappings**
- Use `get()` when key **might not exist**
- Use meaningful key names (strings)
- Use dictionaries for **fast lookups** (O(1))
- Use `in` to check key existence before access
- Use dictionary comprehension for transformations

### DON'T ❌
- Don't use mutable objects as keys (lists, dicts, sets)
- Don't rely on order in Python < 3.7
- Don't use `[]` without checking key existence
- Don't modify dictionary while iterating
- Don't use dictionaries for ordered sequences (use list)

---

## 🧪 Common Patterns

### Default Dictionary Pattern
```python
# Count occurrences
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
```

### Grouping Items
```python
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"}
]

by_grade = {}
for student in students:
    grade = student["grade"]
    by_grade.setdefault(grade, []).append(student["name"])
# Result: {"A": ["Alice", "Charlie"], "B": ["Bob"]}
```

### Swapping Keys and Values
```python
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
# Result: {1: "a", 2: "b", 3: "c"}
```

### Merging Multiple Dictionaries
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}

# Python 3.9+
merged = dict1 | dict2 | dict3
# Result: {"a": 1, "b": 3, "c": 5, "d": 6}

# Any Python version
merged = {**dict1, **dict2, **dict3}
```

---

## 📊 Quick Reference Table

| Operation | Syntax | Returns | Modifies Dict |
|-----------|--------|---------|---------------|
| Create | `{"k": "v"}` | Dictionary | N/A |
| Access | `d["key"]` | Value | ❌ |
| Safe access | `d.get("key", default)` | Value or default | ❌ |
| Add/Update | `d["key"] = value` | None | ✅ |
| Delete | `del d["key"]` | None | ✅ |
| Pop | `d.pop("key")` | Value | ✅ |
| Pop last | `d.popitem()` | (key, value) | ✅ |
| Clear | `d.clear()` | None | ✅ |
| Keys | `d.keys()` | dict_keys | ❌ |
| Values | `d.values()` | dict_values | ❌ |
| Items | `d.items()` | dict_items | ❌ |
| Update | `d.update(other)` | None | ✅ |
| Copy | `d.copy()` | New dict | ❌ |
| Membership | `"key" in d` | Boolean | ❌ |

---

## 🎓 Interview Questions & Answers

### Q: What's the difference between dict["key"] and dict.get("key")?
**A:** `dict["key"]` raises KeyError if key doesn't exist. `dict.get("key", default)` returns default value (or None) without error - safer when key might not exist.

### Q: Can lists be dictionary keys?
**A:** No, keys must be immutable (hashable). Lists are mutable. Use tuples instead: `{(1, 2): "value"}`.

### Q: What's the time complexity of dictionary lookup?
**A:** O(1) average case - dictionaries use hash tables. This makes them much faster than lists for lookups.

### Q: How to merge two dictionaries?
**A:** Python 3.9+: `merged = dict1 | dict2`. Earlier: `merged = {**dict1, **dict2}` or `dict1.update(dict2)`.

### Q: Are dictionaries ordered?
**A:** Yes, since Python 3.7 insertion order is preserved. Before 3.7, no guaranteed order.

### Q: What happens if duplicate keys in dictionary literal?
**A:** Last value wins: `{"a": 1, "a": 2}` results in `{"a": 2}`.

### Q: Difference between pop() and popitem()?
**A:** `pop(key)` removes specific key. `popitem()` removes last inserted key-value pair (no argument needed).

---

## 🎯 Interview One-Liner

**"Dictionaries are mutable, ordered (3.7+) collections of key-value pairs using curly braces or dict(), providing named indexing with O(1) lookup time, requiring immutable hashable keys, supporting methods like get() for safe access, update() for merging, items()/keys()/values() for iteration, ideal for configuration data, JSON-like structures, and fast lookups by meaningful names rather than numeric indices."**

---

*End of Theory Notes*
