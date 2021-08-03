# shopping_cart.py
from datetime import datetime
from os import system, name

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def checkout(user_products):
    products_price = []

    for product in user_products:
        for item in products:
            if product == item["id"]:
                products_price.append(item["price"])

    subtotal = sum(products_price)
    tax = 8.75
    tax_total = (subtotal * tax)/100
    total = subtotal + tax_total

    return round(subtotal, 2), round(tax_total, 2), round(total, 2)

def print_name_price(user_products):
    for product in user_products:
        for item in products:
            if product == item["id"]:
                print(f"...{item['name']} (${item['price']})")

def clear_input():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def receip(user_products, subtotal, tax, total):
    clear_input()
    print("-"*50)
    print("GREEN FOODS GROCERY\nWWW.GREEN-FOODS-GROCERY.COM")

    print("-"*50)
    today = datetime.now()
    print("CHECKOUT AT: ", today)

    print("-"*50)
    print("SELECTED PRODUCTS: ")
    print_name_price(user_products)

    print("-"*50)
    print("SUBTOTAL", round(subtotal, 2))
    print("TAX", round(tax, 2))
    print("TOTAL", round(total, 2))

    print("-"*50)
    print("thanks, see you again soon!".upper())
    print("-"*50)

if __name__ == "__main__":
    user_products = []
    while True:
        product = input("Please input a product identifier: ")
        if product.upper() == "DONE":
            break

        try:
            user_products.append(int(product))
        except:
            user_products.append(0)

    
    total = checkout(user_products)
    receip(user_products, total[0], total[1], total[2])