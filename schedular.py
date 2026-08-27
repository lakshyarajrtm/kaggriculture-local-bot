
from game import *


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def distance_to(self, other: "Position") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


@dataclass
class Job:
    tile: Position
    job_type: Action




def generate_action(job_pos: Position, farmer_pos: Position, 
        job_type: Action = None, job_obj: Crop | Animal = None) -> list[list[str]]:

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



def calculate_cost(workers: list[Position], jobs: list[Position]) -> list[tuple[int, int]]:

    size = max(len(workers), len(jobs))
    if size == 0:
        return []

    costs = [
        [
            workers[i].distance_to(jobs[j])
            if i < len(workers) and j < len(jobs)
            else 0
            for j in range(size)
        ]
        for i in range(size)
    ]

    # Hungarian algorithm
    u = [0] * (size + 1)
    v = [0] * (size + 1)
    matched_row = [0] * (size + 1)
    path = [0] * (size + 1)

    for row in range(1, size + 1):
        matched_row[0] = row
        column = 0
        minimum = [float("inf")] * (size + 1)
        used = [False] * (size + 1)

        while True:
            used[column] = True
            current_row = matched_row[column]
            delta = float("inf")
            next_column = 0

            for candidate in range(1, size + 1):
                if used[candidate]:
                    continue

                reduced_cost = (
                    costs[current_row - 1][candidate - 1]
                    - u[current_row]
                    - v[candidate]
                )

                if reduced_cost < minimum[candidate]:
                    minimum[candidate] = reduced_cost
                    path[candidate] = column

                if minimum[candidate] < delta:
                    delta = minimum[candidate]
                    next_column = candidate

            for candidate in range(size + 1):
                if used[candidate]:
                    u[matched_row[candidate]] += delta
                    v[candidate] -= delta
                else:
                    minimum[candidate] -= delta

            column = next_column
            if matched_row[column] == 0:
                break

        while column:
            previous_column = path[column]
            matched_row[column] = matched_row[previous_column]
            column = previous_column

    result: list[tuple[int, int]] = []

    for column in range(1, size + 1):
        worker_index = matched_row[column] - 1
        job_index = column - 1

        # Exclude assignments involving dummy entries.
        if worker_index < len(workers) and job_index < len(jobs):
            result.append((worker_index, job_index))

    result.sort()
    return result

def find_jobs(farm: list[list[str]]) -> list[tuple]:
    jobs: list[tuple] = []
    for i, row in enumerate(farm):
        for j, tile in enumerate(row):
            if tile is None:
                jobs.append(Job(Position(i, j), Action.PLANT))
            if isinstance(tile, dict):
                tile['']
