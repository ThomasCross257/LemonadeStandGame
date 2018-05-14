import sys
import time
import os
import random

#defining main game mechanics and functions
gameLength = 0
cups = 0
lemons = 0
totalincome = 0
sugar = 0
ice = 0
days = 1
money = 20.00
highTemp = 78
hourlycustomers = 0
customprofit = 0
weather = "Mild"
hour = 7
weatherlist = ["Mild", "Cold", "Hot"]
weatherconditions = "Clear"
soldCups = 0
maxcustomers = 250
customers = 0
customerlikelyhood = 0
weatherlikelyhoodv = 0
lemonlosses = 0
sugarlosses = 0
judgement = "NaN"
score = 0
scorecups = 0
judgementoptions = ["Abysmal", "Bad", "Satisfactory", "Good" ,"Excellent". "Outstanding"]
customerSatisfaction = 0
popularity = 0
totalprofits = 0
lowpricelist = [0.25, 0.26, 0.27, 0.28, 0.29]
mediumpricelist = [0.30, 0.31, 0.32, 0.34, 0.35,0.36,0.37, 0.38, 0.39, 0.40, 0.41, 0.42, 0.43, 0.44]
highpricelist = [0.45,0.46,0.47,0.48,0.49,0.50,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.60,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.70,0.71,0.72,0.73,0.74,0.75,0.76]

#How many cups you need to sell before getting another level up in noteriety
noterietylvl_1 = 15
noterietylvl_2 = 25
noterietylvl_3 = 33
noterietylvl_4 = 44

#flags
ranoutofingredients = False
nomorecustomers = False
secondmenu = False
#flags

#defining prices that the player will set. May change with input
pricepercup = 0.25
lemonsperpitcher = 4
sugarperpitcher = 4
icepercup = 4
#defining the prices of the items
Cups_25 = .81
Cups_50 = 1.75
Cups_100 = 1.85
lemons_10 = 0.81
lemons_30 = 2.26
lemons_75 = 4.06
Sugar_8 = 0.58
Sugar_20 = 1.63
Sugar_48 = 3.50
Ice_100 = 0.86
Ice_250 = 2.23
Ice_500 = 3.84
#defining the prices of the items

#setting the maximum amount of items purchased for a single day for calculating the end of day end of day reports.
max_ice = 0
max_lemons = 0
max_cups = 0
max_sugar = 0
#setting the maximum amount of items for a single day for calculating the end of day end of day reports.

#variables used for the bankrupt page.
totalexpanses = max_lemons + max_ice + max_cups + max_sugar
liquidatedinventory = lemons + ice + cups + sugar
#variables used for the bankrupt page.

#defining the recipie items
sugar_probability = 0
ice_probability = 0
lemon_probability = 0

#External frange function imported to use floats within a given range.
#This was mostly done because of range's inability to use floats, especially when determining the amount of customers the players would get from day to day.


#Customer Calculations
def weatherlikelyhood():
  global weatherlikelyhoodv
  if weather == "Mild":
    g = random.randint(2,6)
    weatherlikelyhoodv  = g + weatherlikelyhoodv
  elif weather == "Cold":
    g = random.randint(1,3)
    weatherlikelyhoodv = g + weatherlikelyhoodv
  elif weather == "Hot":
    g = random.randint(5,10)
    weatherlikelyhoodv = g + weatherlikelyhoodv
def recipielikelyhood():
  global sugarperpitcher
  global icepercup
  global lemonsperpitcher
  global sugar_probability
  global ice_probability
  global lemons_probability
  
  if sugarperpitcher in range(4,7):
    sugar_probability = random.randint(3,8)
  if icepercup in range(2,4):
    ice_probability = random.randint
  if lemonsperpitcher <= 2:
    lemons_probability = random.randint(0,1)
  elif sugarperpitcher <= 3:
    sugar_probability = random.randint(1,2)
  elif icepercup > 4:
    ice_probability = random.randint(1,6)
  elif lemonsperpitcher > 5:
    lemons_probability = random.randint(1,5)
  elif sugarperpitcher >= 8:
    sugar_probability = random.randint(1,4)
  elif icepercup <= 1:
    ice_probability = random.randint(1,5)
  elif lemonsperpitcher in range(3,5):
    lemons_probability = random.randint(2,4)
def customerpricelikelyhood():
  global pricepercup
  global lowpricelist
  global mediumpricelist
  global highpricelist
  if pricepercup < 0.24:
    customerlikelyhood = random.randint(7,10)
  elif pricepercup in lowpricelist:
    customerlikelyhood = random.randint(6,9)
  elif pricepercup in mediumpricelist:
    customerlikelyhood = random.randint(5,7)
  elif pricepercup in highpricelist:
    customerlikelyhood = random.randint(2,5)
  elif pricepercup >= 0.77:
    customerlikelyhood = random.randint(0,3)
def calculatingcustomers():
  global customers
  global customerlikelyhood
  global sugar_probability
  global ice_probability
  global lemons_probability
  global weatherlikelyhoodv
  
  recipie_probability = sugar_probability + ice_probability + lemon_probability
  totalcustomerlikelyhood = customerlikelyhood + recipie_probability + weatherlikelyhoodv
  customers = 5 * totalcustomerlikelyhood
  if customers > 250:
    customers = 250
#Customer Calculations

#Running the simulation
def timescaleset():
  global timescale
  timescale = int(input("How fast would you like the simulation?"))

def diceroller():
  global dice
  dice = random.randint(1,10)

def cash():
  global hourlycustomers
  global pricepercup
  global money
  global totalprofits
  global customprofit
  customprofit = pricepercup * hourlycustomers
  totalprofits = pricepercup * hourlycustomers
  money = customprofit + money

def ingredientloss():
  global sugar
  global lemons
  global ice
  recipiecalc_1 = lemonsperpitcher * hourlycustomers
  recipiecalc_2 = sugarperpitcher * hourlycustomers
  recipiecalc_3 = icepercup * hourlycustomers
  lemons = lemons - recipiecalc_1
  sugar = sugar - recipiecalc_2
  ice = ice - recipiecalc_3

def purchasingcustomers():
  global customers
  global popularity
  global dice
  global hourlycustomers
  global price
  global money
  global lemons
  global ice
  global customprofit
  global totalprofits
  global sugar
  global lemonsperpitcher
  global cups
  global icepercup
  global sugarperpitcher
  g = random.randint(1,5)
  diceroller()
  hourlycustomers = 5 + customers * popularity + dice / 2
  if hourlycustomers > 10:
    hourlycustomers = hourlycustomers - dice
  if hourlycustomers > 35:
   g = random.randint(1,12)
   hourlycustomers = 23
   hourlycustomers = hourlycustomers - g
   if hourlycustomers > 30 or 25 or 15:
     hourlycustomers = hourlycustomers / 2
  hourlycustomers = int(round(hourlycustomers))
  cash()
  money = int(round(money))
  cups = cups - hourlycustomers
  customers = customers - hourlycustomers
  totalprofits = totalprofits + customprofit
  print("You have made: $" ,customprofit, " this past hour.")
  print(hourlycustomers, " customers visited you this hour.")
  ingredientloss()
  
def sellingnothing():
  while 7 != 19:
      global hour
      time.sleep(0)
      hour = hour + 1
      if hour == 13:
        print("It is now: 1PM.")
      elif hour == 14:
        print("It is now: 2PM.")
      elif hour == 15:
        print("It is now: 3PM.")
      elif hour == 16:
        print("It is now: 4PM.")
      elif hour == 17:
        print("It is now: 5PM.")
      elif hour == 18:
        print("It is now: 6PM.")
      elif hour == 19:
        print("It is now: 7PM.")
        break
      elif hour == 8 or hour == 9 or hour == 10 or hour == 11 or   hour == 12:
        print("It is now: " ,hour, "AM")

def betweendays():
  print("What would you like to do before the next day?")
  g = input("""
  A. Change your recipie.
  B. Check your inventory.
  C. Check your funds.
  D. Buy more ingredients
  E. Start the next day.
  """)
  if g == "A" or g == "a":
    recipiesetup2()
  elif g == "B" or g == "B":
    inventorypage()
  elif g == "C" or g == "c":
    funds()
  elif g == "D" or g == "d":
    purchasemenu3()
  elif g == "E" or g == "e":
    gamestartpage()
    

def hourlogger():
  global hour
  print("It is now 7AM.")  
  while 7 != 19 or customers > 0 or lemons > 0 or ice > 0 or cups > 0 or sugar > 0 or money > 0:
    time.sleep(timescale)
    purchasingcustomers()
    hour = hour + 1
    if hour == 13:
      print("It is now: 1PM.")
    elif hour == 14:
      print("It is now: 2PM.")
    elif hour == 15:
      print("It is now: 3PM.")
    elif hour == 16:
      print("It is now: 4PM.")
    elif hour == 17:
      print("It is now: 5PM.")
    elif hour == 18:
      print("It is now: 6PM.")
    elif hour == 19:
      print("It is now: 7PM.")
    elif hour == 8 or hour == 9 or hour == 10 or hour == 11 or   hour == 12:
      print("It is now: " ,hour, "AM")
    if hour >= 19 or customers <= 0 or ice <= 0 or sugar <= 0 or lemons <= 0 or money > 0:
        break
def endofdayreports():
  global ice
  global days
  global max_cups
  global sugarperpitcher
  global max_sugar
  global sugar
  global popularity
  global lemons
  global max_lemons
  global lemonsperpitcher
  global scorecups
  soldcups = cups - max_cups
  absoldcups = abs(soldcups) #Eliminate any decimals or false negatives
  
  #Examining if the amount of sold cups by multiplying or dividing depending on how many cups have been used.
  if absoldcups in range(16,31):
    lemonsloss = lemonsperpitcher * soldcups 
    #Multiplication/Divison operator absent as there are 16 cups in a gallon The range enveloping more than 16 is inaccurate but there is no other method at the moment to change that.
    sugarloss = sugarperpitcher * soldcups
  elif absoldcups in range(32,47):
    lemonsloss = lemonsperpitcher * soldcups * 2
    sugarloss = sugarperpitcher * soldcups * 2
  elif absoldcups > 48:
    lemonsloss = lemonsperpitcher * soldcups * 4
    sugarloss = sugarperpitcher * soldcups * 4
  elif absoldcups in range(8,15):
    lemonsloss = lemonsperpitcher * soldcups / 2
    sugarloss = sugarperpitcher * soldcups / 2
  elif absoldcups <= 7:
    lemonsloss = lemonsperpitcher * soldcups / 4
    sugarloss = sugarperpitcher * soldcups / 4
  else:
    lemonsloss = 0
    sugarloss = 0
  absingred1 = abs(sugarloss)
  absingred2 = abs(lemonsloss)
  lemons = lemons - absingred2
  sugar = sugar - absingred1
  ice = 0
  if soldcups >= noterietylvl_1 or soldcups >= noterietylvl_2 or soldcups >= noterietylvl_3 or soldcups >= noterietylvl_4:
    print("You are becoming more popular!")
    popularity = popularity + 1
    print("Your popularity is now: " ,popularity)
  scorecups = scorecups + soldcups
  print("You sold: " ,abs(soldcups), " Cups")
  print("You lost: " ,abs(lemonsloss), " units of lemons.")
  print("You lost: " ,abs(sugarloss), " units of sugar.")
  print("All your ice has melted.")
  days = days + 1
  if days > gameLength:
    endgame()
  betweendays()
def endofday():
  print("It's time to close!")
  endofdayreports()

def masterkey():
  global nomorecustomers
  global ranoutofingredients
  timescaleset()
  hourlogger()
  if customers <= 0:
    nomorecustomers = True
    print("No more customers are interested!")
    sellingnothing()
  elif ice <= 0 or sugar <= 0 or lemons <= 0:
    print("Ran out of ingredients!")
    ranoutofingredients = True
    sellingnothing()
  elif money < 0:
    print("You've gone bankrupt!")
    bankruptpage()
  endofday()


#inventory initialization
def endgamereports():
  global scorecups
  global money
  global judgement
  global judgementoptions
  
  print("Over the course of " ,gameLength, " days, You sold: " ,scorecups)
  print("You wound up with $" ,money)
  if scorecups in range(0,20):
    judgement = judgementoptions[0]
  elif scorecups in range(21,40):
    judgement = judgementoptions[1]
  elif scorecups in range(41,60):
    judgement = judgementoptions[2]
  elif scorecups in range(61,80):
    judgement = judgementoptions[3]
  elif scorecups in range(81, 100):
    judgement = judgementoptions[4]
  elif scorecups > 100:
    judgement = judgementoptions[5]
  print("Overall, we'd say you did:" ,judgement)

def endgame():
  print("Game Over!")
  endgamereports()
  g = input("Would you like to play again? (Y/N)")
  if g == "Y":
    os.execl(sys.executable, sys.executable, *sys.argv) 
    #restarts the whole program from scratch and clears all variables.
    begininput()
  elif g == "N":
    print("Goodbye! I hope you enjoyed the game.")
    time.sleep(3)
    sys.exit()

def funds():
  print("You currently have: $",money)
  betweendays()

def inventorypage():
	global cups
	global lemons
	global ice
	global sugar
	print("You have the following:")
	print(cups, " Cups")
	print(lemons, " lemons")
	print(sugar, " Sugar")
	print(ice, " Ice")
	betweendays()

def daypicker():
	global gameLength
	g = input("""How many days would you like to play?
  7 days
  14 days
  21 days
  """)
	if g == "7 days" or g == "7 Days" or g == "7 DAYS":
		gameLength = 7
		recipiesetup()
	elif g == "14 days" or g == "14 Days" or g == "14 DAYS":
		gameLength = 14
		recipiesetup()
	elif g == "21 days" or g == "21 Days" or g == "21 DAYS":
		gameLength = 21
		recipiesetup()

def gamestartpage():
  global days
  global gameLength
  if days == gameLength:
    print("This is the last day!")
  elif days > gameLength:
    pass
  print("This is day ",days, " of " ,gameLength)
  print("You currently have: " ,money)
  weatherpicker()
  print("The weather will be: " ,weather, " and: ",weatherconditions)
  weatherlikelyhood()
  recipielikelyhood()
  customerpricelikelyhood()
  calculatingcustomers()
  time.sleep(5)
  masterkey()

def weatherpicker():
  global weather
  global weatherlist
  global hightemp
  global weatherconditions
  g = random.choice(weatherlist)
  weather = g 
  if weather == "Mild":
    hightemp = random.randint(68,80)
  elif weather == "Cold":
    hightemp = random.randint(32,67)
  elif weather == "Hot":
    hightemp = random.randint(81,100)
  if weather == "Cold":
    j = random.randint(0, 100)
    if j in range(0,15):
      weatherconditions == "Mostly Cloudy"
    elif j in range(16,30):
      weatherconditions == "Overcast"
    elif j in range(31,45):
      weatherconditions == "Light Rain"
    elif j in range(46,60):
      weatherconditions == "Rain"
    elif j in range(61,75):
      weatherconditions == "Heavy Rain"
    elif j >= 76:
      weatherconditions == "Rainstorm"

def bankruptpage():
	gonebankrupt = True
	print("Your total income was: " ,totalincome)
	print("In total you bought this much ice, sugar, cups and lemons combined:" ,totalexpanses)
	print("All of your assets have been liquidated, which amounts to: " ,liquidatedinventory)


def recipiesetup():
	global lemonsperpitcher
	global sugarperpitcher
	global pricepercup
	global icepercup
	global lemons
	global sugar
	global ice
	print("Your recipie is currently:")
	print("lemons: ",lemonsperpitcher)
	print("Sugar: ",sugarperpitcher)
	print("Ice: " ,icepercup)
	print("Cup price" ,pricepercup)
	f = input("""What would you like to edit?
  lemons
  Sugar
  Ice
  Cup price
  To Start the game Type: "Game Continue"
  """)
	if f == "lemons" or f == "LEMONS" or f == "lemons":
		lemonsperpitcher = int(
		    input("Please input how many lemons you'd like in your mix"))
		if lemonsperpitcher > lemons:
		  lemonsperpitcher = 0
		  print("You cannot input more lemons that you have.")
		else:
		  recipiesetup()
	elif f == "Sugar" or f == "SUGAR" or f == "sugar":
		sugarperpitcher = int(
		    input("Please input how much sugar you'd like in your mix"))
		if sugarperpitcher > sugar:
		  sugarperpitcher = 0
		  print("You cannot input more units of sugar than you have.")
		  recipiesetup()
		else:
		    recipiesetup()
	elif f == "Ice" or f == "ICE" or f == "ice":
	 icepercup = int(input("Please input how much ice you'd like in your mix"))
	 if icepercup > ice:
	   icepercup = 0
	   print("You cannot put more ice in than you already have.")
	   recipiesetup()
	 recipiesetup()
	elif f == "Cup price" or f == "Cup Price" or f == "CUP PRICE" or f == "cup price":
		pricepercup = float(input("Please input the price you would like for your cups."))
		if pricepercup > 2.00 or pricepercup < 0.05:
		  pricepercup = 0
		  print("You cannot set the price beyond $2.00 or below $0.05")
		  recipiesetup()
		recipiesetup()
	elif f == "Game Continue" or f == "game continue" or f == "Game continue" or f == "GAME CONTINUE":
	    gamestartpage()
	else:
	  print("Invalid input...")
	  recipiesetup

def recipiesetup2():
	global lemonsperpitcher
	global sugarperpitcher
	global pricepercup
	global icepercup
	global lemons
	global sugar
	global ice
	print("Your recipie is currently:")
	print("lemons: ",lemonsperpitcher)
	print("Sugar: ",sugarperpitcher)
	print("Ice: " ,icepercup)
	print("Cup price" ,pricepercup)
	f = input("""What would you like to edit?
  lemons
  Sugar
  Ice
  Cup price
  To go back to the previous menu, simply type: "Back"
  """)
	if f == "lemons" or f == "LEMONS" or f == "lemons":
		lemonsperpitcher = int(
		    input("Please input how many lemons you'd like in your mix"))
		if lemonsperpitcher > lemons:
		  lemonsperpitcher = 0
		  print("You cannot input more lemons that you have.")
		else:
		  recipiesetup()
	elif f == "Sugar" or f == "SUGAR" or f == "sugar":
		sugarperpitcher = int(
		    input("Please input how much sugar you'd like in your mix"))
		if sugarperpitcher > sugar:
		  sugarperpitcher = 0
		  print("You cannot input more units of sugar than you have.")
		  recipiesetup()
		else:
		    recipiesetup()
	elif f == "Ice" or f == "ICE" or f == "ice":
	 icepercup = int(input("Please input how much sugar you'd like in your mix"))
	 if icepercup > ice:
	   icepercup = 0
	   print("You cannot put more ice in that you already have.")
	   recipiesetup()
	elif f == "Cup price" or f == "Cup Price" or f == "CUP PRICE" or f == "cup price":
		pricepercup = float(input("Please input the price you would like for your cups."))
		if pricepercup > 2.00 or pricepercup < 0.05:
		  pricepercup = 0
		  print("You cannot set the price beyond $2.00 or below $0.05")
		  recipiesetup()
		else:
		  recipiesetup()
	elif f == "Back" or f == "back":
	    betweendays()

#Purchasing functions
def purchasecups25():
	global money
	global cups
	global max_cups
	moneychange = money - Cups_25
	money = moneychange
	round(money)
	cups = cups + 25
	max_cups = max_cups + cups
	print(
	    "You have purchased 25 cups. Your funds are now:",
	    money,
	)
	if secondmenu == True:
	  purchasemenu3()
	else:
	  purchasemenu2()

def purchasecups50():
	global money
	global cups
	global max_cups
	moneychange = money - Cups_50
	money = moneychange
	round(money)
	print(
	    "You have purchased 50 cups. Your funds are now:",
	    money,
	)
	cups = cups + 50
	max_cups = max_cups + cups
	purchasemenu2()

def purchasecups100():
	global money
	global cups
	global max_cups
	moneychange = money - Cups_100
	money = moneychange
	round(money)
	print(
	    "You have purchased 100 cups. Your funds are now:",
	    money,
	)
	cups = cups + 100
	max_cups = max_cups + cups
	purchasemenu2()

def purchaselemon10():
	global money
	global lemons
	global max_lemons
	lemons = lemons + 10
	max_lemons = max_lemons + lemons
	moneychange = money - lemons_10
	money = moneychange
	round(money)
	round(money)
	print(
	    "You have purchased 10 lemons. Your funds are now:",
	    money,
	)
	purchasemenu2()

def purchaselemon30():
	global money
	global lemons
	global max_lemons
	lemons = lemons + 30
	max_lemons = max_lemons + lemons
	moneychange = money - lemons_30
	money = moneychange
	round(money)
	print(
	    "You have purchased 30 lemons. Your funds are now:",
	    money,
	)
	purchasemenu2()

def purchaselemon75():
	global money
	global lemons
	global max_lemons
	lemons = lemons + 75
	max_lemons = max_lemons + lemons
	moneychange = money - lemons_75
	money = moneychange
	round(money)
	print(
	    "You have purchased 75 lemons. Your funds are now:",
	    money,
	)
	purchasemenu2()

def purchasesugar8():
	global money
	global sugar
	global max_sugar
	sugar = sugar + 8
	max_sugar = max_sugar + sugar
	moneychange = money - Sugar_8
	money = moneychange
	round(money)
	print(
	    "You have purchased 8 units of Sugar. Your funds are now:",
	    money,
	)
	purchasemenu2()

def purchasesugar20():
	global money
	global sugar
	global max_sugar
	sugar = sugar + 20
	max_sugar = max_sugar + sugar
	moneychange = money - Sugar_20
	money = moneychange
	round(money)
	print(
	    "You have purchased 20 units of Sugar. Your funds are now:",
	    money,
	)
	purchasemenu2()

def purchasesugar48():
	global money
	global sugar
	global max_sugar
	sugar = sugar + 48
	max_sugar = max_sugar + sugar
	moneychange = money - Sugar_48
	money = moneychange
	round(money)
	print(
	    "You have purchased 48 units of Sugar. Your funds are now:",
	    money,
	)
	purchasemenu2()

def purchaseice100():
	global money
	global ice
	global max_ice
	ice = ice + 100
	max_ice = max_ice + ice
	moneychange = money - Ice_100
	money = moneychange
	round(money)
	print(
	    "You have purchased 100 units of Ice. Your funds are now:",
	    money,
	)
	purchasemenu2()

def purchaseice250():
	global money
	global ice
	global max_ice
	ice = ice + 250
	moneychange = money - Ice_250
	money = moneychange
	round(money)
	print(
	    "You have purchased 250 units of Ice. Your funds are now:",
	    money,
	)
	purchasemenu2()

def purchaseice500():
	global money
	global ice
	global max_ice
	ice = ice + 500
	moneychange = money - Ice_500
	money = moneychange
	round(money)
	print(
	    "You have purchased 500 units of Ice. Your funds are now:",
	    money,
	)
	purchasemenu2()

def purchasemenu():
	purchaseinput = (input(
	    print(
	        """This is the purchasing page, below will be prices for each item. Input the following commands 
  Cups:
  'Buy 25 Cups' $0.81
  'Buy 50 Cups' $1.75
  'Buy 100 Cups' $1.85
  lemons:
  'Buy 10 lemons' $0.81
  'Buy 30 lemons' $2.26
  'Buy 75 lemons' $4.06
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
		elif purchaseinput == "Buy 10 lemons":
			purchaselemon10()
		elif purchaseinput == "Buy 30 lemons":
			purchaselemon30()
		elif purchaseinput == "Buy 75 lemons":
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
	purchaseinput = (input(
	    print("""Continue Purchasing until you would like to set the days. Type: Days to start selecting.
  Cups:
  'Buy 25 Cups' $0.81
  'Buy 50 Cups' $1.75
  'Buy 100 Cups' $1.85
  lemons:
  'Buy 10 lemons' $0.81
  'Buy 30 lemons' $2.26
  'Buy 75 lemons' $4.06
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
		elif purchaseinput == "Buy 10 lemons":
			purchaselemon10()
		elif purchaseinput == "Buy 30 lemons":
			purchaselemon30()
		elif purchaseinput == "Buy 75 lemons":
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
		elif purchaseinput == "days" or purchaseinput == "Days" or purchaseinput == "DAYS":
			daypicker()
			secondmenu = True
		else:
			print("Incorrect input, redirecting")
			purchasemenu2()
	elif money <= 7:
	  print("You are dangerously close to overspending! For the sakes of this game you will no longer be able to purchase anymore items.")
	  secondmenu = True
	  daypicker()

def purchasemenu3():
	purchaseinput = (input(
	    print("""Restock on anything you'd like until you feel like going back to the menu. Type: 'Return' to go back to the menu.
  Cups:
  'Buy 25 Cups' $0.81
  'Buy 50 Cups' $1.75
  'Buy 100 Cups' $1.85
  lemons:
  'Buy 10 lemons' $0.81
  'Buy 30 lemons' $2.26
  'Buy 75 lemons' $4.06
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
		elif purchaseinput == "Buy 10 lemons":
			purchaselemon10()
		elif purchaseinput == "Buy 30 lemons":
			purchaselemon30()
		elif purchaseinput == "Buy 75 lemons":
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
		elif purchaseinput == "Return" or purchaseinput == "return" or purchaseinput == "RETURN":
			betweendays()
		else:
			print("Incorrect input, redirecting")
			purchasemenu3()

#Purchasing Functions

def instructions():
	print("Welcome to the Lemonade Stand Game!")
	print(
	    """You have 7, 14, or 21 days to make as much money as possible, and you’ve decided to open a lemonade stand! You’ll have complete control over your business, including pricing, quality control, inventory control, and purchasing supplies. Buy your ingredients, set your recipe, and start selling!
    
    The first thing you’ll have to worry about is your recipe. At first, go with the default recipe, but try to experiment a little bit and see IF you can find a better one. Make sure you buy enough of all your ingredients, or you won’t be able to sell!"
    
    You’ll also have to deal with the weather, which will play a big part when customers are deciding whether or not to buy your lemonade. Read the weather report every day! When the temperature drops, or the weather turns bad (overcast, cloudy, rain), don’t expect them to buy nearly as much as they would on a hot, hazy day, so buy accordingly. Feel free to set your prices higher on those hot, muggy days too, as you’ll make more profit, even IF you sell a bit less lemonade.
    
    The other major factor which comes into play is your customer’s satisfaction. As you sell your lemonade, people will decide how much they like or dislike it.  This will make your business more or less popular. If your popularity is low, fewer people will want to buy your lemonade, even IF the weather is hot and sunny. But IF you’re popularity is high, you’ll do okay, even on a rainy day!"
    
    At the end of 7, 14, or 21 days you’ll see how much money you made. Play again, and try to beat your high score!"""
	)

def begininput():
	instructions()
	start = (input(
	    print("If you have read these instructions, please type 'START'")))
	if start == "START" or start == "start" or start == "Start":
		purchasemenu()
	elif start == "debug_quickstart":
	  devpassword = input("Enter password:")
	  if devpassword == "Holdout":
	    global lemons
	    global max_cups
	    global ice
	    global sugar
	    global cups
	    global max_lemons
	    global max_ice
	    global max_sugar
	    lemons = 10000
	    max_lemons = 10000
	    max_cups = 10000
	    cups = 10000
	    ice = 10000
	    sugar = 10000
	    max_ice = 10000
	    max_sugar = 10000
	    daypicker()
	  else:
	    print("It's not nice trying to impersonate devs! Back to the normal game for you!")
	    purchasemenu()
	else:
		print("Error, Invalid input. Recalculating...")

begininput()
