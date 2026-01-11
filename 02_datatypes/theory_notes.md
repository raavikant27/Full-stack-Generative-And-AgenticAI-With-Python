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

*End of Theory Notes*
