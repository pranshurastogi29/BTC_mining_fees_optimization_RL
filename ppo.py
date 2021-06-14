from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from envs import FeesMaximizationEnv

env=FeesMaximizationEnv()
env = DummyVecEnv([lambda: env])
model = PPO('MlpPolicy', env, verbose = 1)
model.learn(total_timesteps=200000)

obs = env.reset()
l = []
while True:
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    l.append(env.envs[0].select_hash)
    if done: 
        print('Optimized_fees_PPO', info[0]['terminal_observation'][0] , 'Optimized_weight_PPO' , info[0]['terminal_observation'][1])
        break
selected_hash_PPO = l[-2]
Optimized_fees_PPO , Optimized_weight  = info[0]['terminal_observation']
env.close()

textfile = open("Fees_optimied_PPO.txt", "w")

for element in selected_hash_PPO:

    textfile.write(element + "\n")

textfile.close()