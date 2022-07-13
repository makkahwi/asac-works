print("**************************************")
print("**  Welcome to the Snakes Cafe    ! **")
print("**  Please see our menu below       **")
print("**                                  **")
print('** To quit at any time, type "quit" **')
print("**************************************\n\n")

menu = {
  "Appetizers": ["Hummus", "Mutabbal"],
  "Entrees": ["Vegan Burger", "Baked Falafel"],
  "Desserts": ["Fruit Salad","Row fruits"],
  "Beverages": ["Green Tea", "Black Coffee"]
}

categories = list(map(lambda key: key, menu.keys()))
items = list(map(lambda key: list(map(lambda item: item.upper(), menu[key])), categories))

def listing (key):
  print("\n",key)
  print("-----")
  list(map(lambda item: print(item), menu[key]))

print("Our Menu...")
list(map(lambda key: listing(key), menu.keys()))

order = []

print("\n\n***********************************")
print("** What would you like to order? **")
print("***********************************\n")

def ordering ():
  newOrder = input().upper()

  correctOrder = False

  if newOrder != "QUIT":
    for item in items:
      if newOrder in item:
        correctOrder = True
        order.append(newOrder)

    if not correctOrder:
      print("Your entry is wrong, please try again")

    print()

    uorder = []

    for item in order:
        if item not in uorder:
          uorder.append(item)
    
    list(map(lambda item: print(sum(1 for _ in filter(lambda items: items == item,order)),"order of", item, "have been added to your meal"),uorder))
    ordering()
  else :
    if not len(order):
      print("You ordered nothing")

ordering()