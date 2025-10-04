# Electricity Bill Calculator

# Rate per unit
rate_per_unit = 5  # in INR

# Ask the user for the number of units consumed
units_consumed = float(input("Enter the number of units consumed: "))

# Calculate the total bill
total_bill = units_consumed * rate_per_unit

# Display the result
print(f"Your electricity bill for {units_consumed} units is: ₹{total_bill:.2f}")
