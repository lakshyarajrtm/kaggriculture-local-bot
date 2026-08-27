from collections import deque

from game import *
from schedular import *



# Agents state
actions: list[list[str]] = deque()
market_orders = [['BUY_SEED', 'WHEAT', 1]] * 3
market_orders.append(['BUY_ANIMAL', 'COW', 1])



# Agent's functionality
def agent(obj: dict) -> dict :

    player = obj.get('player')

    farm = obj.get('farms')[player]

    


    



    

