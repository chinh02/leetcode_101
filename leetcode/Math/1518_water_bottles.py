# There are numBottles water bottles that are initially full of water. 
# You can exchange numExchange empty water bottles from the market with one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

numBottles = 15
numExchange = 4

def numWaterBottles(numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles // numExchange > 0:
            fullBottles = numBottles // numExchange
            result += fullBottles
            numBottles = fullBottles + (numBottles % numExchange) 
        return result

print(numWaterBottles(numBottles, numExchange))