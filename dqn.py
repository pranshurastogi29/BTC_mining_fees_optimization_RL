
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from envs import FeesMaximizationEnv

model = DQN('MlpPolicy', env, verbose = 1)
model.learn(total_timesteps=200000)

obs = env.reset()
c = []
while True:
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    c.append(env.envs[0].select_hash)
    if done: 
        print('Optimized_fees_DQN', info[0]['terminal_observation'][0] , 'Optimized_weight_DQN' , info[0]['terminal_observation'][1])
        break
selected_hash_DQN = c[-2]
Optimized_fees_DQN , Optimized_weight_DQN  = info[0]['terminal_observation']
env.close()

textfile = open("Fees_optimied_DQN.txt", "w")

for element in selected_hash_DQN:

    textfile.write(element + "\n")

textfile.close()