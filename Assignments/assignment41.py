# Assignment 41 : Implement the solution to the Problem
item_price = [1050, 2200, 8575, 485, 234, 150, 399]
def price_max (item_price):
    print ("Price of costliest item in the retail store : ", max(item_price))
def average_price(item_price):
    total_price = 0
    for i in item_price :
        total_price += i
    average_price = total_price/len(item_price)
    print ("Average price of items in the retail store : ", average_price)
def display_sorted_price (item_price):
    item_price.sort()
    print ("Item price list in increasing order : ", item_price)
price_max(item_price)
average_price(item_price)
display_sorted_price(item_price)

# ===========================OUTPUT=============================
# Price of costliest item in the retail store :  8575
# Average price of items in the retail store :  1870.4285714285713
# Item price list in increasing order :  [150, 234, 399, 485, 1050, 2200, 8575]
