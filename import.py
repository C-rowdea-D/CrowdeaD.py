import random

coin = random.choice (["heads", "tails"])
print(coin)

dice = random.randint (1,6)
print(dice)

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle (cards)
for card in cards :
        print(card)

import statistics
print(statistics.mean([100,20,30,50,40,20,30,20,10]))
print(statistics.median([100,20,30,50,40,20,30,20,10]))
print(statistics.mode ([100,20,30,50,40,20,30,20,10]))


