# Problem: Online T-shirt Store Delivery Fees Calculator
# If order amount > 300, delivery is free (0 rupees)
# Otherwise, delivery costs 30 rupees
# Task: Use ternary operator to decide delivery fees

# Get order amount from user and convert to integer
order_amount = int(input("Enter the order amount: "))

# Print order amount and its type (for learning purposes)
print(f"Order amount is: {order_amount} (Type: {type(order_amount)})")

# Using Ternary Operator
# Syntax: variable = value_if_true if condition else value_if_false
delivery_fees = 0 if order_amount > 300 else 30

# Display the delivery fees
print(f"Delivery fees is: {delivery_fees}")