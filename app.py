
# --- Function Definition: order (Returns a Value) ---
def order(item)
    print(f"\n--- Calling order('{item}') ---")
    order_number = 42  # Simulating an order number
    return order_number  # This line is crucial for returning the value

# --- Function Definition: check_stock (Performs an Action) ---
def check_stock(order_item):
    print(f"\n--- Calling check_stock('{order_item}') ---")
    stock = True  # Simulating stock check
    return stock  # This line is crucial for returning the stock status

# --- Function Definition: get_daily_special (Returns a Value) ---
def get_daily_special():
    special = "Blueberry Muffin"
    return special # This returns the value of the daily special

# --- Function Definition: check_order_ready (Performs an Action) ---
def check_order_ready(order_item):
    print(f"--- Calling check_order_ready('{order_item}') ---")
    return True  # Simulating order readiness check

def what_is_your_name():
    return "Coach Olivia"  # This returns the name of the co-teacher