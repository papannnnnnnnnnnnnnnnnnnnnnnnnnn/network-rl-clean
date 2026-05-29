import sys
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# add project root
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from stable_baselines3 import DQN
from env.traffic_env import TrafficEnv

# create environment
env = TrafficEnv()

# load trained model
model = DQN.load("models/traffic_dqn")

# reset environment
obs, _ = env.reset()

# store traffic history
traffic_history = [[] for _ in range(4)]

# create plot
fig, ax = plt.subplots()

lines = [
    ax.plot([], [], label=f"Link {i+1}")[0]
    for i in range(4)
]

ax.set_xlim(0, 50)
ax.set_ylim(0, 100)

ax.set_xlabel("Time Step")
ax.set_ylabel("Traffic Load")
ax.set_title("Live Network Traffic Control using RL")

ax.legend()

step_count = 0

def update(frame):

    global obs
    global step_count

    action, _ = model.predict(obs)

    obs, reward, done, _, _ = env.step(action)

    print(f"Step {step_count} | State: {obs} | Action: {action} | Reward: {reward}")

    for i in range(4):
        traffic_history[i].append(obs[i])

        lines[i].set_data(
            range(len(traffic_history[i])),
            traffic_history[i]
        )

    step_count += 1

    return lines

ani = FuncAnimation(
    fig,
    update,
    frames=50,
    interval=500,
    blit=False
)

plt.show()