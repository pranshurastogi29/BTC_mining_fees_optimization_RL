import math
import numpy as np
import pandas as pd
import gym
from gym import spaces
from gym.utils import seeding
from env import FeesMaximizationEnv

env=FeesMaximizationEnv()
episodes = 5
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0 
    
    while not done:
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score+=reward
    print(len(env.select_hash))
    print('Episode:{} Score:{}'.format(episode, score))
env.close()