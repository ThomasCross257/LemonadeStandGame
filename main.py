import sys
import Pygame # learn more: https://python.org/pypi/Pygame
import random

#defining main game mechanics and functions
gameLength = 0
cups = 0
Lemons = 0
sugar = 0
ice = 0
day = 0
money = 20.00
highTemp = 78
weather = "Mild"
weatherlist = ["Mild" "Cold" "Hot"]
soldCups = 0
customers = 0
judgement = "NaN"
customerSatisfaction = 0
populatiy = 0

#defining the prices of the items
Cups_25 = .81
Cups_50 = 1.75
Cups_100 = 1.85
Lemons_10 = 0.81
Lemons_30 = 2.26
Lemons_75 = 4.06
Sugar_8 = 0.58
Sugar_20 = 1.63
Sugar_48 = 3.50
Ice_100 = 0.86
Ice_250 = 2.23
Ice_500 = 3.84

def instructions():
    print("Welcome to the Lemonade Stand Game!")
    print("""You have 7, 14, or 21 days to make as much money as possible, and you’ve decided to open a lemonade stand! You’ll have complete control over your business, including pricing, quality control, inventory control, and purchasing supplies. Buy your ingredients, set your recipe, and start selling!
    
    The first thing you’ll have to worry about is your recipe. At first, go with the default recipe, but try to experiment a little bit and see IF you can find a better one. Make sure you buy enough of all your ingredients, or you won’t be able to sell!"
    
    You’ll also have to deal with the weather, which will play a big part when customers are deciding whether or not to buy your lemonade. Read the weather report every day! When the temperature drops, or the weather turns bad (overcast, cloudy, rain), don’t expect them to buy nearly as much as they would on a hot, hazy day, so buy accordingly. Feel free to set your prices higher on those hot, muggy days too, as you’ll make more profit, even IF you sell a bit less lemonade.
    
    The other major factor which comes into play is your customer’s satisfaction. As you sell your lemonade, people will decide how much they like or dislike it.  This will make your business more or less popular. If your popularity is low, fewer people will want to buy your lemonade, even IF the weather is hot and sunny. But IF you’re popularity is high, you’ll do okay, even on a rainy day!"
    
    At the end of 7, 14, or 21 days you’ll see how much money you made. Play again, and try to beat your high score!""")

def purchasecups25():
    global money
    global cups
    moneychange = money - Cups_25
    money = moneychange
    round(money)
    cups = cups + 25
    print("You have purchased 25 cups. Your funds are now:", money,)
    purchasemenu2()
def purchasecups50():
    global money
    global cups
    moneychange = money - Cups_50
    money = moneychange
    round(money)
    print("You have purchased 50 cups. Your funds are now:", money,)
    cups = cups + 50
    purchasemenu2()
def purchasecups100():
  global money
  global cups
  moneychange = money - Cups_100
  money = moneychange
  round(money)
  print("You have purchased 100 cups. Your funds are now:", money,)
  cups = cups + 100
  purchasemenu2()
def purchaselemon10():
    global money
    global Lemons
    Lemons = Lemons + 10
    moneychange = money - Lemons_10
    money = moneychange
    round(money)
    round(money)
    print("You have purchased 10 Lemons. Your funds are now:", money,)
    purchasemenu2()
def purchaselemon30():
    global money
    global Lemons
    Lemons = Lemons + 30
    moneychange = money - Lemons_30
    money = moneychange
    round(money)
    print("You have purchased 30 Lemons. Your funds are now:", money,)
    purchasemenu2()
def purchaselemon75():
  global money
  global Lemons
  Lemons = Lemons + 75
  moneychange = money - Lemons_75
  money = moneychange
  round(money)
  print("You have purchased 75 Lemons. Your funds are now:", money,)
  purchasemenu2()
def purchasesugar8():
    global money
    global sugar
    sugar = sugar + 8
    moneychange = money - Sugar_8
    money = moneychange
    round(money)
    print("You have purchased 8 units of Sugar. Your funds are now:", money,)
    purchasemenu2()
def purchasesugar20():
    global money
    global sugar
    sugar = sugar + 20
    moneychange = money - Sugar_20
    money = moneychange
    round(money)
    print("You have purchased 20 units of Sugar. Your funds are now:", money,)
    purchasemenu2()
def purchasesugar48():
  global money
  global sugar
  sugar = sugar + 48
  moneychange = money - Sugar_48
  money = moneychange
  round(money)
  print("You have purchased 48 units of Sugar. Your funds are now:", money,)
  purchasemenu2()
def purchaseice100():
    global money
    global ice
    ice = ice + 100
    moneychange = money - Ice_100
    money = moneychange
    round(money)
    print("You have purchased 100 units of Ice. Your funds are now:", money,)
    purchasemenu2()
def purchaseice250():
    global money
    global ice
    ice = ice + 250
    moneychange = money - Ice_250
    money = moneychange
    round(money)
    print("You have purchased 250 units of Ice. Your funds are now:", money,)
    purchasemenu2()
def purchaseice500():
  global money
  global ice
  ice = ice + 500
  moneychange = money - Ice_500
  money = moneychange
  round(money)
  print("You have purchased 500 units of Ice. Your funds are now:", money,)
  purchasemenu2()

def purchasemenu():
  purchaseinput = (input (print ("""This is the purchasing page, below will be prices for each item. Input the following commands 
  Cups:
  'Buy 25 Cups' $0.81
  'Buy 50 Cups' $1.75
  'Buy 100 Cups' $1.85
  Lemons:
  'Buy 10 Lemons' $0.81
  'Buy 30 Lemons' $2.26
  'Buy 75 Lemons' $4.06
  Sugar:
  'Buy 8 Sugar' $0.58
  'Buy 20 Sugar' $1.63
  'Buy 48 Sugar' $3.50
  Ice:
  'Buy 100 Ice' $0.86
  'Buy 250 Ice' $2.23
  'Buy 500 Ice' $3.84
  """)))
  if money > 0:
    if purchaseinput == "Buy 25 Cups":
      purchasecups25()
    elif purchaseinput == "Buy 50 Cups":
        purchasecups50()
    elif purchaseinput == "Buy 100 Cups":
        purchasecups100()
    elif purchaseinput == "Buy 10 Lemons":
        purchaselemon10()
    elif purchaseinput == "Buy 30 Lemons":
        purchaselemon30()
    elif purchaseinput == "Buy 75 Lemons":
        purchaselemon75()
    elif purchaseinput == "Buy 8 Sugar":
        purchasesugar8()
    elif purchaseinput == "Buy 20 Sugar":
        purchasesugar20()
    elif purchaseinput == "Buy 48 Sugar":
        purchasesugar48()
    elif purchaseinput == "Buy 100 Ice":
        purchaseice100()
    elif purchaseinput == "Buy 250 Ice":
        purchaseice250()
    elif purchaseinput == "Buy 500 Ice":
        purchaseice500()
def purchasemenu2():
  purchaseinput = (input (print ("""Continue Purchasing until you would like to start the game.
  Cups:
  'Buy 25 Cups' $0.81
  'Buy 50 Cups' $1.75
  'Buy 100 Cups' $1.85
  Lemons:
  'Buy 10 Lemons' $0.81
  'Buy 30 Lemons' $2.26
  'Buy 75 Lemons' $4.06
  Sugar:
  'Buy 8 Sugar' $0.58
  'Buy 20 Sugar' $1.63
  'Buy 48 Sugar' $3.50
  Ice:
  'Buy 100 Ice' $0.86
  'Buy 250 Ice' $2.23
  'Buy 500 Ice' $3.84
  """)))
  if money > 0:
    if purchaseinput == "Buy 25 Cups":
      purchasecups25()
    elif purchaseinput == "Buy 50 Cups":
        purchasecups50()
    elif purchaseinput == "Buy 100 Cups":
        purchasecups100()
    elif purchaseinput == "Buy 10 Lemons":
        purchaselemon10()
    elif purchaseinput == "Buy 30 Lemons":
        purchaselemon30()
    elif purchaseinput == "Buy 75 Lemons":
        purchaselemon75()
    elif purchaseinput == "Buy 8 Sugar":
        purchasesugar8()
    elif purchaseinput == "Buy 20 Sugar":
        purchasesugar20()
    elif purchaseinput == "Buy 48 Sugar":
        purchasesugar48()
    elif purchaseinput == "Buy 100 Ice":
        purchaseice100()
    elif purchaseinput == "Buy 250 Ice":
        purchaseice250()
    elif purchaseinput == "Buy 500 Ice":
        purchaseice500()
    elif purchaseinput == "begin" or purchaseinput == "Begin" or purchaseinput == "BEGIN":
        pass
    else:
      print("Incorrect input, redirecting")
      purchasemenu2()
instructions()
def begininput():
  start = (input(print("If you have read these instructions, please type 'START'")))
  if start == "START" or start == "start" or start == "Start":
    purchasemenu()
  else:
    print("Error, Invalid input. Recalculating...")
begininput()
