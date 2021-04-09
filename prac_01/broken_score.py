"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

first_item = float(input("Price of first item: "))
second_item = float(input("Price of second item: "))
third_item = float(input("Price of third item: "))
fourth_item = float(input("Price of fourth item: "))

sub_total = first_item + second_item + third_item + fourth_item

if sub_total >= 100:
    final_price = 0.9 * sub_total
elif sub_total < 100:
    final_price = sub_total


print("Final price is: {}".format(final_price))