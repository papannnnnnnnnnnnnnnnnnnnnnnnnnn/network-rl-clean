import sys
import os
import matplotlib.pyplot as plt

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from stable_baselines3 import DQN
from env.traffic_env import TrafficEnv

env = TrafficEnv()

model = DQN.load("models/traffic_dqn")

obs, _ = env.reset()

traffic_history = []

done = False

while not done:

    action, _ = model.predict(obs)

    obs, reward, done, _, _ = env.step(action)

    traffic_history.append(obs.copy())

    print(f"State: {obs} | Action: {action} | Reward: {reward}")

for i in range(4):
    plt.plot(
        [x[i] for x in traffic_history],
        label=f"Link {i+1}"
    )

plt.xlabel("Time Step")
plt.ylabel("Traffic Load")
plt.title("Network Traffic Control using RL")
plt.legend()

plt.show()