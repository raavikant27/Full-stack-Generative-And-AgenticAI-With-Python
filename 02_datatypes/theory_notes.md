# Python Data Types & Objects - Theory Notes

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

## Remember:
> "If the ID changes, it's a new object (immutable).  
> If the ID stays same, it's the same object modified (mutable)."

---

*End of Theory Notes*
