# UNIT-3D-TASK 7 SHOPPING CART WITH PRODUCTS 
def shopping_cart(**products):
    total = 0
    print("Items Purchased:")
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total += price
    print(f"Total: ₹{total}")
shopping_cart(apple=15, orange=12, mango=10)