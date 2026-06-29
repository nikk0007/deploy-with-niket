# Section 6: The elif Keyword
# Example: Delivery app order status

order_status = input(
    "Enter order status (placed/out for delivery/delivered/cancelled): "
).lower()

if order_status == "placed":
    print("Your order has been placed.")
elif order_status == "out for delivery":
    print("Your order is out for delivery.")
elif order_status == "delivered":
    print("Your order has been delivered. Enjoy!")
elif order_status == "cancelled":
    print("Your order was cancelled.")
else:
    print("Unknown status. Please contact support.")

# Rules to remember:
#   - You can write as many elif blocks as you need.
#   - Python checks conditions top to bottom and stops
#     at the FIRST True condition.
#   - All remaining elif/else blocks are skipped after that.
#   - Only ONE block runs, every time.
