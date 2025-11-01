def cost_calculate(item, quantity, price):
    print(f"{quantity} {item}s: ${quantity * price:.2f}")

# Method 1
cost_calculate("banana", 6, 1.5)

# Method 2
cost_calculate(item="banana", price=1.6, quantity=8)

# Method 3
cost_calculate("banana", quantity=10, price=2.6)