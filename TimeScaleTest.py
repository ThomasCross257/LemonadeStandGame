import time
import sys
import random

customers = 100
noteriety = 1
dice = 0
hourlycustomers = 0
price = 0.50
profit = 0
money = 0
timescale = 0
hour = 7

def timescaleset():
  global timescale
  timescale = int(input("How fast would you like the simulation?"))
  

def diceroller():
  global dice
  dice = random.randint(1,10)

def purchasingcustomers():
  global customers
  global noteriety
  global dice
  global hourlycustomers
  global price
  global money
  g = random.randint(1,5)
  diceroller()
  hourlycustomers = customers / 2 * noteriety / dice
  if hourlycustomers <= 16:
    hourlycustomers = hourlycustomers * g
    g = random.randint(1,12)
  if hourlycustomers > 35:
    hourlycustomers = 23
  customprofit = 0.50 * hourlycustomers
  money = customprofit + money
  hourlycustomers = int(round(hourlycustomers))
  money = int(round(money))
  customers = customers - hourlycustomers
  print("You have made: $" ,money, " this past hour.")
  print(hourlycustomers, " customers visited you this hour.")
  
def nocustomers():
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
      elif hour == 8 or hour == 9 or hour == 10 or hour == 11 or   hour == 12:
        print("It is now: " ,hour, "AM")
      if hour == 19:
        break

def hourlogger():
  global hour
  print("It is now 7AM.")  
  while 7 != 19 or customers > 0:
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
    if hour >= 19 or customers <= 0:
        break
    
def endofday():
  print("It's time to close!")
  sys.exit()

def masterkey():
  timescaleset()
  hourlogger()
  if customers <= 0:
    print("No more customers!")
    nocustomers()
  endofday()

masterkey()
