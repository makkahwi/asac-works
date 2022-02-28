print("***************************************")
print("*  Welcome to Suhaib's Fake Resturant *")
print("***************************************")
print("* Pleace make your pick of menu below *")
print("***************************************\n\n")

menu = {
  "Appetizers": {"A1": "Hummus", "A2":"Mutabbal"},
  "Entrees": {"E1": "Vegan Burger", "E2": "Baked Falafel"},
  "Desserts": {"D1": "Fruit Salad", "D2": "Row fruits"},
  "Beverages": {"B1": "Green Tea", "B2": "Black Coffee"}
}

categories = list(map(lambda key: key, menu.keys()))
items = list(map(lambda key: list(map(lambda item: item, menu[key])), categories))

def listing (key):
  print("\n",key)
  print("\n-----")
  list(map(lambda item: print(item,":",menu[key][item]), menu[key]))

print("Our Menu...")
list(map(lambda key: listing(key), menu.keys()))

order = []

def ordering ():
  print("\n#Please type down the number of your next choice ('A1' or 'D2' or 'B2' ...etc) or type 'Done' to exit")
  newOrder = input().upper()

  correctOrder = False

  if newOrder != "DONE":
    for item in items:
      if newOrder in item:
        add = menu[categories[items.index(item)]][newOrder]
        correctOrder = True
        order.append(add)
        print("You just ordered", add)

    if not correctOrder:
      print("Your entry is wrong, please try again")
    
    print("You have ordered so far", order)
    ordering()
  else :
    if len(order):
      print("You full order is", order)
    else:
      print("You ordered nothing")

ordering()