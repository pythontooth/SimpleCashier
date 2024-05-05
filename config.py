# Payments
name_dayincome = 'day_income.txt'
income_tax = 0.23 # Tax
after_tax = 1 - income_tax # Displays the after tax total
tax_percentage = income_tax * 100 # Displays the tax percentage

# Transactions, discounts
name_transactions = 'transactions.txt'
disc0 = 0.9  # Represents a 10% discount
disc1 = str(100 - disc0 * 100) + "%"  # Calculate the final price after discount

# PIN settings
pin = "0000"
pin_enabled = True
pin_tries = 3

# Other
command_end = "session_exit" # Ends the day/session

# Users list
users = {
  "Patrick": 1,
  "Robert": 2,
  "Michael": 3,
  "William": 4,
  "David": 5,
  "James": 6,
  "John": 7,
  "Joseph": 8,
  "Andrew": 9,
  "Thomas": 10,
}

# Products list
products = {
    "apple": 2.99,
    "banana": 3.99,
    "orange": 2.99,
    "strawberry": 3.49,
    "grape": 2.79,
    "pear": 2.49,
    "watermelon": 0.99,
    "blueberry": 4.29,
    "pineapple": 3.79,
    "kiwi": 1.89,
    "mango": 3.99,
    "avocado": 1.49,
    "coconut": 1.79,
    "lemon": 4.99,
    "lime": 0.79,
    "peach": 2.69,
    "grapefruit": 2.59,
    "raspberry": 5.49,
    "cantaloupe": 1.99,
    "cranberry": 3.99,
    "fig": 4.49,
    "apricot": 2.89,
    "blackberry": 3.29,
    "pomegranate": 3.69,
    "tangerine": 2.49,
    "kiwifruit": 1.79,
    "papaya": 2.99,
    "persimmon": 3.29,
    "honeydew": 2.29,
    "nectarine": 2.99,
    "plum": 2.39,
    "cherry": 1.99,
    "guava": 2.19,
    "abcdefg": 0.79,
    "passionfruit": 4.99,
    "quince": 3.79,
    "starfruit": 5.29,
    "boysenberry": 3.69,
    "elderberry": 3.19,
    "kumquat": 4.49,
    "mulberry": 3.59,
    "plantain": 1.59,
    "soursop": 4.79,
    "dragonfruit": 6.99,
    "jackfruit": 5.49,
    "lychee": 7.99,
    "example": 3.49
}

