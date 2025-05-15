# Function to calculate the final price after applying discount
def calculate_discount(price, discount_percent):
    # Apply discount only if it's 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Prompt the user to enter original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function to calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Display the result
    if discount_percent >= 20:
        print(f"Discount applied. Final price: ksh{final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ksh{final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
