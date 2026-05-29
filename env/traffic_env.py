import gymnasium as gym
from gymnasium import spaces
import numpy as np

class TrafficEnv(gym.Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()

        # actions:
        # 0 = reduce link 1
        # 1 = reduce link 2
        # 2 = reduce link 3
        # 3 = reduce link 4
        self.action_space = spaces.Discrete(4)

        # network traffic state
        self.observation_space = spaces.Box(
            low=0,
            high=100,
            shape=(4,),
            dtype=np.float32
        )

        self.state = None
        self.step_count = 0

    def reset(self, seed=None, options=None):
        self.state = np.random.randint(
            20,
            80,
            size=(4,)
        ).astype(np.float32)

        self.step_count = 0

        return self.state, {}

    def step(self, action):

        # increase all links slightly
        self.state += np.random.randint(0, 10, size=(4,))

        # chosen action reduces one link
        self.state[action] -= 15

        # keep values valid
        self.state = np.clip(self.state, 0, 100)

        # reward system
        congestion = np.sum(self.state > 75)

        reward = -congestion

        self.step_count += 1

        done = self.step_count >= 50

        return self.state, reward, done, False, {}