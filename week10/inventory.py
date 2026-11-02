# Reflection
#
# 1. Most surprising thing about Python lists:
# What surprised me most is how easy lists are to create and use. With one line
# I can store a whole set of values, and built-in tools like len(), sum(), max(),
# and min() give me useful information from it right away. I expected it to take
# more work to get answers out of a collection of data.
#
# 2. Business situation where a list beats doing it manually in Excel:
# When I am working at a register and handling a difficult cash transaction, I
# have to add up several amounts and make sure the total is right while a
# customer waits. Doing that by hand, or in a spreadsheet with formulas, is slow
# and easy to get wrong. With a Python list I could store each amount, use sum()
# to get the total instantly, and use a loop to apply a discount or tax to every
# amount the same way.

# inventory.py
# Author: Zafar Indawala
# module 10 lab: Inventory List Manager

print("--- Exercise 1: Build the list ---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0])#first item
print(inventory[-1])#last item
middle = len(inventory) // 2 #calculate the index
print(inventory[middle])# middle item

print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3]) #first 3 items
print(inventory[-2]) #last 2 items
print(inventory[::2]) #every second item

print("--- Exercise 4: Modifying the list ---")
inventory.append("envelope")

print(inventory) 
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison---")
coords = [40.7128, -74.0060]

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average list of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count 

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2)) # 10% discount

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
