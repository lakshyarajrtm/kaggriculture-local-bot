
from enum import Enum
from dataclasses import dataclass
from collections import deque

@dataclass
class GameConfig:
    episode_steps: int = 720
    board_size: int = 10
    starting_money: int = 3_000
    max_market_orders_per_turn: int = 10
    turns_per_day: int = 24
    shed_capacity: int = 100
    weed_spawn_chance: float = 0.005
    town_shop_unlock_interval: int = 3
    town_shop_sell_interval: int = 4
    town_center_sell_interval: int = 24





class Crop(str, Enum):
    WHEAT = 'WHEAT'
    CARROT = 'CARROT'
    TOMATO = 'TOMATO'
    STRAWBERRY = 'STRAWBERRY'
    MELON = 'MELON'

class BuildType(str, Enum):
    BUILD_COOP = 'BUILD_COOP'
    BUILD_PASTURE = 'BUILD_PASTURE'

class Animal(str, Enum):
    GOOSE = 'GOOSE'
    COW = 'COW'
    SHEEP = 'SHEEP'

class Direction(str, Enum):
    EAST = 'EAST'
    WEST = 'WEST'
    NORTH = 'NORTH'
    SOUTH = 'SOUTH'

class Action(str, Enum):
    WATER = 'WATER'
    HARVEST = 'HARVEST'
    FERTILIZE = 'FERTILIZE'
    DIG = 'DIG'
    PLANT = 'PLANT'
    PLACE = 'PLACE'
    PICKUP = 'PICKUP'
    CARE = 'CARE'






