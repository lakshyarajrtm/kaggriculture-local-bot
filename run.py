print("1. run.py started", flush=True)

print("2. importing kaggle_environments", flush=True)
from kaggle_environments import make
print("3. imported kaggle_environments", flush=True)

print("4. importing agent", flush=True)
from main import agent
print("5. imported agent", flush=True)

print("6. creating environment", flush=True)
env = make(
    "kaggriculture",
    configuration={"episodeSteps": 24},
    debug=True,
)
print("7. environment created", flush=True)

print("8. running game", flush=True)
env.run([agent, "pass"])
print("9. game finished", flush=True)

final = env.steps[-1]

for i, state in enumerate(final):
    print(
        f"Player {i}: reward={state.reward}, status={state.status}",
        flush=True,
    )

