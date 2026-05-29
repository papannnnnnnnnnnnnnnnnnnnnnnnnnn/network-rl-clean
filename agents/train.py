import sys
import os

# add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stable_baselines3 import DQN
from env.traffic_env import TrafficEnv

# create environment
env = TrafficEnv()

# create model
model = DQN(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=0.001,
    buffer_size=10000
)

# train model
model.learn(total_timesteps=5000)

# save trained model
model.save("models/traffic_dqn")