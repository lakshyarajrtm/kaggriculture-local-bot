# Kaggriculture Local Bot

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Approach](https://img.shields.io/badge/approach-algorithmic-blue)
![Status](https://img.shields.io/badge/status-early%20development-orange)

An algorithmic strategy bot for the **Kaggriculture** farming simulation in
[`kaggle-environments`](https://github.com/Kaggle/kaggle-environments). The project uses deterministic planning, optimization, and mathematical decision-making—**not machine learning**—to manage a farm and compete against another agent.

> [!IMPORTANT]
> This project is under active development. The local game model and the first worker-scheduling components are implemented, but the agent does not yet play a complete match.

## Objective

The bot is being designed to maximize its final Kaggriculture reward by coordinating farm work and economic decisions across a limited episode. This includes:

- buying seeds and animals;
- selecting what and how much to plant;
- assigning farmers to jobs efficiently;
- watering and fertilizing crops at useful intervals;
- harvesting and selling production;
- caring for livestock;
- deciding when additional farm hands are worth their cost; and
- balancing money, storage, land, labor, and time.

The local game model currently defines a `10 × 10` board, `3,000` starting money, a `100`-unit shed, up to `10` market orders per turn, and a default `720`-step episode. The development runner currently overrides the episode length to `21` steps for short matches.

## Current Implementation

| Area | Status | Details |
| --- | --- | --- |
| Game model | In progress | Configuration values and enums for crops, animals, movement, building, and farm actions are defined in `game.py`. |
| Movement | Implemented | `generate_action()` moves a farmer one tile toward a job using grid coordinates. |
| Worker assignment | Implemented | `calculate_cost()` builds a Manhattan-distance cost matrix and uses the Hungarian algorithm to match farmers with jobs. |
| Job discovery | In progress | `find_jobs()` begins scanning the farm board and identifies empty tiles as planting jobs. |
| Agent policy | Scaffolded | `agent_one.py` reads the active player's farm and contains initial orders for three wheat seeds and one cow. It does not yet return a complete action payload. |
| Market strategy | Planned | `market.py` is reserved for buying and selling logic. |
| Local match runner | Implemented | `run.py` creates a Kaggriculture environment, runs the bot against the built-in random agent, and prints final rewards and statuses. |

## Strategy Design

The planned decision loop is:

1. Read the observation and extract the active player's farm state.
2. Find actionable jobs across the board.
3. Score jobs by urgency, expected value, and resource cost.
4. Match available farmers to jobs while minimizing travel distance.
5. Generate movement or farm actions for each assigned worker.
6. Submit market orders that support the next production cycle.
7. Re-evaluate the plan on the next step.

### Crop planning

The crop planner will choose among wheat, carrot, tomato, strawberry, and melon. Crop selection should consider seed cost, growth time, water and fertilizer demand, expected sale value, available plots, and the number of turns remaining.

### Watering, fertilizing, and harvesting

Farm jobs will be prioritized by marginal value and urgency. The scheduler should send workers to crops that need immediate care, harvest mature crops before value is lost, and avoid spending resources where they cannot pay back before the episode ends.

### Animal management

The game model currently represents geese, cows, and sheep, together with coop and pasture construction. The future animal policy will compare purchase and care costs with expected production and will schedule `PLACE`, `PICKUP`, and `CARE` jobs.

### Farm hands

Hiring decisions will compare wages with the additional value created by parallel work. Once multiple farmers are available, the assignment problem is handled by the Hungarian algorithm in `schedular.py`.

### Economy and market

The market policy will coordinate purchases and sales while respecting the per-turn order limit, shed capacity, shop timing, and a cash reserve. Early versions will use explainable return-on-investment rules before adding deeper multi-turn optimization.

## Algorithmic Approach

The project currently uses:

- **Manhattan distance** to estimate travel cost on the farm grid;
- the **Hungarian algorithm** to find a minimum-cost assignment of workers to jobs; and
- **deterministic action generation** to translate an assignment into movement or work commands.

Planned extensions include priority queues for urgent jobs, constrained resource allocation, crop-profit calculations, finite-horizon scheduling, and short look-ahead simulations. These are conventional algorithms and heuristics; the bot is intentionally non-AI and non-ML.

## Project Structure

```text
kaggriculture-local-bot/
├── agent_one.py   # Agent state and main Kaggle agent function
├── game.py        # Configuration plus crop, animal, action, and movement enums
├── market.py      # Planned market decision logic
├── run.py         # Local bot-versus-random match runner
├── schedular.py   # Positions, jobs, routing, assignment, and job discovery
└── README.md
```

> `schedular.py` keeps the repository's current filename. It may be renamed to `scheduler.py` later.

## Getting Started

### Requirements

- Python 3.10 or newer
- A version of `kaggle-environments` that includes the `kaggriculture` environment

### Installation

```bash
git clone https://github.com/lakshyarajrtm/kaggriculture-local-bot.git
cd kaggriculture-local-bot

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install kaggle-environments
```

If Kaggriculture is supplied separately from the public package, install or register the competition environment according to its official instructions before running the bot.

### Run a local match

```bash
python3 run.py
```

`run.py` starts a short 21-step match between `agent_one.agent` and Kaggle's `random` agent, then prints each player's final reward and status.

The current agent is incomplete, so a successful competitive run is not expected yet.

## Roadmap

- [x] Define core configuration values and game enums.
- [x] Generate one-step movement toward a target job.
- [x] Assign workers to jobs with the Hungarian algorithm.
- [ ] Complete farm-board parsing and job discovery.
- [ ] Define the action dictionary returned by `agent()`.
- [ ] Implement planting, watering, fertilizing, and harvesting policies.
- [ ] Implement animal placement, care, and collection.
- [ ] Build market buying and selling logic.
- [ ] Add farm-hand hiring and multi-worker scheduling.
- [ ] Add unit tests for routing, assignment, and edge cases.
- [ ] Add full-match benchmarks against baseline agents.
- [ ] Package the finished agent for competition submission.

## Contributing

The codebase is experimental and its interfaces may change. Issues and pull requests are welcome, especially for isolated scheduling logic, strategy ideas, tests, and bug fixes.

Please keep new decision logic deterministic and explainable, and include tests or match results when changing strategy behavior.

## License

This repository does not currently include a license. Until one is added, the author retains all rights to the source code.
