# Output
# Case 1
# Please enter your fav 🍧?: VAnilla
# Yes, we have vanilla in stock
stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

favourite = input("Please enter your favourite 🍧 ?:").strip().lower()

if favourite == stock1:
    print(f"Yes, we have {stock1} in stock")
elif favourite == stock2:
    print(f"Yes, we have {stock2} in stock")
elif favourite == stock3:
    print(f"Yes, we have {stock3} in stock")
elif favourite == stock4:
    print(f"Yes, we have {stock4} in stock")

else:
    print(f"Sorry, we ran out of {favourite.capitalize()}")

# Case 2
# Please enter your fav 🍧?: salted Caramel
# Sorry, we ran out of Salted Caramel


stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

favourite = input("Please enter your favourite 🍧 ?:").strip().lower()

if (
    favourite != stock1
    or favourite != stock2
    or favourite != stock3
    or favourite != stock4
):
    print(f"Sorry, we ran out of {favourite.capitalize()}")


# Task 1.3

stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

available_flavors = [stock1, stock2, stock3, stock4]
favourite = input("Please enter your favourite 🍧 ?:").strip().lower()

if favourite in available_flavors:
    print(f"Yes, we have {favourite} in stock")
else:
    print(f"Sorry, we ran out of {favourite}")


# T ask 1.4
