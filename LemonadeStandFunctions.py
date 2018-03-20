import main
import sys

#defining main game mechanics and functions
gameLength = 0
cups = 0
lemons = 0
sugar = 0
ice = 0
day = 0
money = 20.00
highTemp = 78
weather = "Mild"
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

def inventory():
    print ("Cups: ",cups,)
    print ("Lemons: ",lemons,)
    print ("Ice: ",ice,)
def stats():
    print ("Day: ",day,)
    print ("Money: ",money,)
    print ("Today's High: ",highTemp,)
    print ("Today's Weather: ",weather,)
def instructions():
    print("You have 7, 14, or 21 days to make as much money as possible, and you’ve decided to open a lemonade stand! You’ll have complete control over your business, including pricing, quality control, inventory control, and purchasing supplies. Buy your ingredients, set your recipe, and start selling!")

    print("The first thing you’ll have to worry about is your recipe. At first, go with the default recipe, but try to experiment a little bit and see IF you can find a better one. Make sure you buy enough of all your ingredients, or you won’t be able to sell!"
    print("You’ll also have to deal with the weather, which will play a big part when customers are deciding whether or not to buy your lemonade. Read the weather report every day! When the temperature drops, or the weather turns bad (overcast, cloudy, rain), don’t expect them to buy nearly as much as they would on a hot, hazy day, so buy accordingly. Feel free to set your prices higher on those hot, muggy days too, as you’ll make more profit, even IF you sell a bit less lemonade.")

    print("The other major factor which comes into play is your customer’s satisfaction. As you sell your lemonade, people will decide how much they like or dislike it.  This will make your business more or less popular. If your popularity is low, fewer people will want to buy your lemonade, even IF the weather is hot and sunny. But IF you’re popularity is high, you’ll do okay, even on a rainy day!")

    print("At the end of 7, 14, or 21 days you’ll see how much money you made. Play again, and try to beat your high score!")
def weather():
    if highTemp in range(68,80):
        weather = "Mild"
        elif highTemp in range(50,67):
          weather = "Cold"
        elif highTemp in range(81,100):
          weather = "Hot"

