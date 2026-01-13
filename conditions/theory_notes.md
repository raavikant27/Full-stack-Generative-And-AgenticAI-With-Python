# Python Conditions - Theory Notes

## Table of Contents
1. Input and Type Conversion
2. Ternary Operator
3. Nested Conditionals
4. The `pass` Keyword
5. Code Blocks and Indentation

---

## 1. Input and Type Conversion

### Getting User Input
```python
order_amount = input("Enter the order amount: ")
```
- The `input()` function **always returns a string**
- Even if user enters a number, it comes as string: `"40"` not `40`

### Type Checking
```python
print(type(order_amount))  # <class 'str'>
```

### Type Conversion
To convert string to number:
```python
# Convert to integer
order_amount = int(input("Enter the order amount: "))

# Convert to float
price = float(input("Enter price: "))

# Convert to string
text = str(123)  # "123"
```

**Important**: If conversion fails (e.g., converting "hitesh" to int), program will crash with ValueError.

---

## 2. Ternary Operator (Conditional Expression)

### Traditional If-Else Way
```python
if order_amount > 300:
    delivery_fees = 0
else:
    delivery_fees = 30
```

### Ternary Operator Way (One Line)
```python
delivery_fees = 0 if order_amount > 300 else 30
```

### Syntax Structure
```python
variable = value_if_true if condition else value_if_false
```

### How It Works
1. Python evaluates the `condition`
2. If condition is `True`, assign `value_if_true`
3. If condition is `False`, assign `value_if_false`

### Example Breakdown
```python
delivery_fees = 0 if order_amount > 300 else 30
#               ↑         ↑                  ↑
#           if true    condition         if false
```

### Benefits
- Shorter code
- More readable for simple conditions
- Commonly used in Python
- Good for assignments based on conditions

### When to Use
✅ Simple conditions with straightforward outcomes
✅ Assigning values based on a condition
❌ Complex logic (use regular if-else)
❌ Multiple conditions (better with if-elif-else)

---

## 3. Nested Conditionals

### What are Nested Conditionals?
Conditionals inside other conditionals - checking multiple conditions in levels.

### Example: Smart Thermostat
```python
if device_status == "active":
    # First level condition
    if temp > 35:
        # Second level condition (nested inside first)
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")
```

### Structure Visualization
```
Outer If
├── Inner If (checked only if outer is True)
│   └── Code block
├── Inner Else
│   └── Code block
Outer Else
└── Code block
```

### Important Rules
1. **Indentation matters** - Shows which block belongs where
2. Each `else` belongs to its corresponding `if`
3. You can nest as many levels as needed (but keep it readable)
4. Only check inner condition if outer condition is True

### Common Pattern
```python
# Check primary condition first
if primary_condition:
    # Then check secondary condition
    if secondary_condition:
        # Both conditions are True
    else:
        # Primary True, Secondary False
else:
    # Primary condition is False
```

---

## 4. The `pass` Keyword

### What is `pass`?
A placeholder statement that does nothing - tells Python "I'll add code here later"

### Usage
```python
if device_status == "active":
    pass  # TODO: Add logic here
else:
    print("Device is offline")
```

### Why Use `pass`?
- **Prevents syntax errors**: Python requires code in every block
- **Placeholder**: Mark areas to complete later
- **Development workflow**: Write structure first, fill in logic later

### Example Without `pass` (ERROR)
```python
if device_status == "active":
    # This will cause IndentationError
else:
    print("Device is offline")
```

### Example With `pass` (WORKS)
```python
if device_status == "active":
    pass  # Valid placeholder
else:
    print("Device is offline")
```

### Alternatives to `pass`
```python
# Using comment (will cause error)
if condition:
    # TODO: implement this
    
# Using pass (correct way)
if condition:
    pass  # TODO: implement this
```

---

## 5. Code Blocks and Indentation

### What is a Code Block?
A group of statements that belong together, indicated by indentation.

### Python Uses Indentation
Unlike other languages (that use `{}` or `begin/end`), Python uses **indentation** to define blocks.

```python
if condition:
    # This is inside the if block
    statement1
    statement2
    if nested_condition:
        # This is inside nested block
        statement3
# This is outside all blocks
statement4
```

### Indentation Rules
1. Use **4 spaces** (standard) or **1 tab** consistently
2. All statements in same block must have same indentation
3. Don't mix spaces and tabs
4. Indentation shows hierarchy and structure

### Example: Block Levels
```python
# Level 0 (no indentation)
if device_status == "active":
    # Level 1 (one indentation)
    print("Device is active")
    
    if temp > 35:
        # Level 2 (two indentations)
        print("High temperature")
        
        if temp > 50:
            # Level 3 (three indentations)
            print("Critical temperature")
    
    # Back to Level 1
    print("Check complete")

# Back to Level 0
print("Program end")
```

### Common Indentation Errors
```python
# ERROR: Inconsistent indentation
if condition:
    statement1
      statement2  # Extra spaces - ERROR!

# ERROR: No indentation
if condition:
statement1  # Should be indented - ERROR!

# CORRECT
if condition:
    statement1
    statement2
```

---

## Summary

### Key Takeaways
1. **Input is always string** - Use `int()` or `float()` to convert
2. **Ternary operator** - One-line conditional assignment: `value_if_true if condition else value_if_false`
3. **Nested conditionals** - Check conditions within conditions for complex logic
4. **pass keyword** - Placeholder to avoid syntax errors during development
5. **Indentation** - Defines code blocks and hierarchy in Python

### Best Practices
- Use ternary operator for simple, single assignments
- Keep nesting shallow (2-3 levels max) for readability
- Use `pass` when writing structure before implementation
- Be consistent with indentation (4 spaces recommended)
- Add comments to explain complex nested logic

---

## Practice Problems

### Problem 1: Ternary Operator
Convert this to ternary operator:
```python
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

**Answer:**
```python
status = "Adult" if age >= 18 else "Minor"
```

### Problem 2: Nested Conditions
A user can login if:
- Account is active AND password is correct
Write nested conditionals for this.

**Answer:**
```python
if account_status == "active":
    if password == correct_password:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Account is inactive")
```
