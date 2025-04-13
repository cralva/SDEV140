"""
Author: Cristian Alvarez
Date: 4/13/25
Assignment: M4 Assignment Part 2
Version: 1.0
"""

#initialization
shopItems = {}

#get data
shopItems = { #storing keys and values into this dictionary
    'Apple': 0.50,
    'Banana': 0.20,
    'Mango': 0.99,
    'Coconut': 2.99,
    'Pineapple': 3.99
}
#process data
def get_price(item): #creating our function so that we can get the price
    return item[1]

sortedItems = sorted(shopItems.items(), key=get_price, reverse=True) #sorting the dictionary by price

for item, price in sortedItems[:3]: #getting the three most expensive keys
    # output information
    print(item, price)