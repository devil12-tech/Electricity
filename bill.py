# Electricity Bill Calculator with Discount

# Rate per unit
rate_per_unit = 5  # in INR

# Ask the user for the number of units consumed
units_consumed = float(input("Enter the number of units consumed: "))

# Calculate the total bill
total_bill = units_consumed * rate_per_unit

# Check if total bill exceeds 1000 for discount
if total_bill > 1000:
    discount = total_bill * 0.10  # 10% discount
    total_bill_after_discount = total_bill - discount
    print(f"Congratulations! You get a 10% discount of ₹{discount:.2f}.")
    print(f"Your total electricity bill after discount is: ₹{total_bill_after_discount:.2f}")
else:
    print(f"Your total electricity bill is: ₹{total_bill:.2f}")
