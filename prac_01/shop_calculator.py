""""
A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""

# empty list of item prices
item_prices = []

# input request from user
num_items = int(input('How many items: '))

# for loop running based on number of items user entered
for i in range (0, num_items):
    price = float(input('Enter price of item:'))
    item_prices.append(price)

if price >= 100:
    final_price = price - 0.1(price)
elif price < 100:
    final_price = price

print(final_price)