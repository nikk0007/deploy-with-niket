# ============================================================
# 01_why_functions.py
# Topic: Why Functions Exist — The Copy-Paste Disaster
# ============================================================

# The problem: same logic written in three different places.
# One place gets updated. The other two are forgotten. Bugs ship to production.

# ---- THE BAD WAY — copy-paste programming ----

cart_price = 1200

# On the cart page
gst_cart = cart_price * 0.18
total_cart = cart_price + gst_cart
print(f"[Cart Page]     Price: Rs.{cart_price} | GST: Rs.{gst_cart} | Total: Rs.{total_cart}")

# On the invoice page — same logic, copy-pasted
gst_invoice = cart_price * 0.18       # rate changed? have to remember to update here too
total_invoice = cart_price + gst_invoice
print(f"[Invoice Page]  Price: Rs.{cart_price} | GST: Rs.{gst_invoice} | Total: Rs.{total_invoice}")

# On the checkout summary — same logic again
gst_checkout = cart_price * 0.18      # and here too
total_checkout = cart_price + gst_checkout
print(f"[Checkout Page] Price: Rs.{cart_price} | GST: Rs.{gst_checkout} | Total: Rs.{total_checkout}")

print()
print("Now imagine the GST rate changes from 18% to 28%.")
print("You have to find and update 3 separate places. Miss one — bugs go live.")
print()

# ---- THE RIGHT WAY — define the logic once, call it everywhere ----

def calculate_gst(base_price, gst_rate=0.18):
    """
    Calculate GST amount and total for a given base price.
    gst_rate: decimal form — 0.18 means 18%
    Returns a dict with gst_amount and total.
    """
    gst_amount = base_price * gst_rate
    total = base_price + gst_amount
    return {"gst": round(gst_amount, 2), "total": round(total, 2)}

# Now all three pages call the same function.
# Rate changes? Update the function. All three fix automatically.

result = calculate_gst(1200)
print(f"[Cart Page]     GST: Rs.{result['gst']} | Total: Rs.{result['total']}")

result = calculate_gst(1200)
print(f"[Invoice Page]  GST: Rs.{result['gst']} | Total: Rs.{result['total']}")

result = calculate_gst(1200)
print(f"[Checkout Page] GST: Rs.{result['gst']} | Total: Rs.{result['total']}")

print()
print("Rate changes to 28%? Update ONE line inside the function.")
print("All three pages fix themselves automatically. Zero bugs.")
