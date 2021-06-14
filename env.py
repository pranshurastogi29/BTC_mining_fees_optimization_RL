import math
import numpy as np
import pandas as pd
import gym
from gym import spaces
from gym.utils import seeding

class FeesMaximizationEnv(gym.Env):
    """
    Description:
        The agent (a miner) want to select the transaction. For any given
        state the agent may choose to accept or reject the transaction keeping 
        weight is less then limit
    
    Observation:
        Type: Box(2)
        Num    Observation               Min            Max
        0      Fee                       0              inf
        1      Weights                   0              4000000
    Actions:
        Type: Discrete(3)
        Num    Action
        0      Dont process the transaction
        1      Process the transaction

    Reward:
         Reward of 1 is awarded if the running average fee increases
         Reward of -1 is awarded if the running average fee decreases

    Episode Termination:
         Weight exceeds 4000000
    """

    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 30
    }

    def __init__(self, goal_velocity=0):
        self.min_fee = 0
        self.max_fee =  np.finfo(np.float32).max
        self.max_weight = 4000000
        self.min_weight = 0
        self.df = pd.read_csv('mempool.csv')[['tx_id','fee','weight']]
        self.low = np.array(
            [self.min_fee, self.min_weight], dtype=np.float32
        )
        self.high = np.array(
            [self.max_fee, self.max_weight], dtype=np.float32
        )

        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(
            self.low, self.high, dtype=np.float32
        )

        self.seed()
        self.current_fee = 0
        self.current_weight = 0
        self.c = 1
        self.select_hash = []

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def select_transaction(self):
        seed = np.random.choice(np.arange(len(self.df)), 1, replace=False)[0]
        return self.df.values[seed]

    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))

        fee , weight  = self.state
        select_hash , selected_fee , selected_weight = self.select_transaction()

        if (fee + selected_fee) > (self.current_fee / self.c):
          self.current_fee  = fee + selected_fee
          self.current_weight = weight + selected_weight
          self.c = self.c + 0.5
          self.select_hash.append(select_hash)
          reward = 1

        elif (fee + selected_fee) <= (self.current_fee / self.c):
          reward = -1


        done = bool(
          self.current_weight > self.max_weight
        )

        self.state = (self.current_fee, self.current_weight)
        return np.array(self.state), reward, done, {}

    def reset(self):
        self.state = np.array([0,0])
        self.current_fee, self.current_weight = 0 , 0
        self.c = 1
        self.select_hash = []
        return np.array(self.state)