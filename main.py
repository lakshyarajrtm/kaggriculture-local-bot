import math
from dataclasses import dataclass


job_cost = {'WATER': 10, 'HARVEST': 5, 'PLANT': 3, 'DIG': 2}


@dataclass
class Pos:
    x: int
    y: int


@dataclass
class Job:
    pos: Pos
    job_type: str

    def priority(self, from_pos: Pos):
        return job_cost[self.job_type] + manhattan_distance(self.pos, from_pos)

def manhattan_distance(to_pos: Pos, from_pos: Pos):
    return abs(to_pos.x - from_pos.x) + abs(to_pos.y - from_pos.y)


def next_action(job_pos: Pos, farmer_pos: Pos, 
        job_type: str = '', job_obj: str = '') -> list[str]:

    if job_pos.x > farmer_pos.x:
        return ['EAST']
    if job_pos.x < farmer_pos.x:
        return ['WEST']
    if job_pos.y > farmer_pos.y:
        return ['SOUTH']
    if job_pos.y < farmer_pos.y:
        return ['NORTH']
    if job_type and job_obj:
        return [job_type, job_obj]
    if job_type:
        return [job_type]

    return ['PASS']

def can_harvest(tile: dict | str | None) -> bool:
    return (
        isinstance(tile, dict)
        and tile.get("kind") == "PLANT"
        and tile.get("crop") == "WHEAT"
        and tile.get("yield_units", 0) >= 1
    )

def find_nearest(tiles: list[list[dict | str | None]], from_pos: Pos, job: str) -> Pos | None:
    min_distance: int = math.inf
    nearest_pos: Pos | None = None
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            to_pos = None
            if job == 'WATER':
                if isinstance(tile, dict) and tile['kind'] == 'PLANT' and not tile['watered_today']:
                    to_pos = Pos(x, y)
            elif job == 'PLANT':
                if tile is None:
                    to_pos = Pos(x, y)
            elif job == 'HARVEST':
                if can_harvest(tile):
                    to_pos = Pos(x, y)
            else:
                raise ValueError('privide a valid job')
            if to_pos:
                distance = manhattan_distance(to_pos, from_pos)
                if min_distance > distance:
                    min_distance = distance
                    nearest_pos = Pos(x, y)
    return nearest_pos

def assign_jobs(obs: dict) -> list[tuple[Pos, Job]]:
    workers: list[Pos] = []
    
                
def agent(obs: dict) -> dict :
    farm : dict = obs['farms'][obs['player']]
    farmer_pos = Pos(*farm['farmer'])
    private = obs['private']
    market_orders = []
    money = farm.get('money', 0)
    hour = farm.get('hour')
    if hour == 0:
        market_orders.extend([['HIRE']] * 4)
    wheat_amt = private['shed'].get('WHEAT', 0)
    if wheat_amt > 0:
        market_orders.append(['SELL','WHEAT',wheat_amt])
    unwatered_plant: Pos = find_nearest(farm['tiles'], farmer_pos, 'WATER')
    if unwatered_plant:
        return {'farmer': next_action(unwatered_plant, farmer_pos, 'WATER'), 'market': market_orders}
    harvestable_plant: Pos = find_nearest(farm['tiles'], farmer_pos, 'HARVEST')
    if harvestable_plant:
        return{'farmer': next_action(harvestable_plant, farmer_pos, 'HARVEST'), 'market': market_orders}
    if private.get('seeds').get('WHEAT', 0) > 0:
        nearest_tile = find_nearest(farm['tiles'], farmer_pos, 'PLANT')
        if nearest_tile:
            return {'farmer': next_action(nearest_tile, farmer_pos, 'PLANT', 'WHEAT'), 'market': market_orders}
        else:
            return {'farmer': ['PASS'], 'market': market_orders}
    else:
        if money > 10:
            market_orders.append(['BUY_SEED', 'WHEAT', 1])
        return {'farmer': ['PASS'], 'market': market_orders}

        


    
    



    


    



    

