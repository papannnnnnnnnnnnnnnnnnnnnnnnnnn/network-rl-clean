import sys
import os
import time

# add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stable_baselines3 import DQN
from env.traffic_env import TrafficEnv

# load environment
env = TrafficEnv()

# load trained model
model = DQN.load("models/traffic_dqn")

# reset environment
obs, _ = env.reset()

done = False

while not done:
    # AI chooses action
    action, _states = model.predict(obs)

    # apply action
    obs, reward, done, _, _ = env.step(action)

    print(f"Traffic: {obs[0]:.0f} | Action: {action} | Reward: {reward}")

    time.sleep(0.5)