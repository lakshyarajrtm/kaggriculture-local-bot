from kaggle_environments import make
from agent_one import agent

env = make("kaggriculture", configuration={"episodeSteps": 21}, debug=True)
env.run([agent, "random"])  # or env.run(["main.py", "random"]) to load from a file

# View result
final = env.steps[-1]
for i, s in enumerate(final):
    print(f"Player {i}: reward={s.reward}, status={s.status}")

