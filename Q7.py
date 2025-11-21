# Program to read purchase data and calculate billing details

file_obj = open("purchase-1.txt", "r")
file_lines = file_obj.readlines()
file_obj.close()

item_prices = {}       # { item : price }
discount_each = 0

for line in file_lines:
    line = line.strip()
    if line == "":
        continue

    if line.startswith("Discount"):
        parts = line.split()
        discount_each = int(parts[1])
    else:
        item_name, item_cost = line.split()
        item_prices[item_name] = int(item_cost)

# Calculations
total_items = len(item_prices)

# Assume every 3rd item is free
free_items = total_items // 3

total_cost = sum(item_prices.values())
total_discount = total_items * discount_each
final_bill = total_cost - total_discount

# Display results
print("No of items purchased:", total_items)
print("No of free items:", free_items)
print("Amount to pay:", total_cost)
print("Discount given:", total_discount)
print("Final amount paid:", final_bill)
