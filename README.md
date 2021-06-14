# BTC_mining_fees_optimization_RL <img align="right" width="10%" src="https://s3.envato.com/files/230419052/preview.jpg">
Deep Reinforcement Learning for Fees Optimization

## Abstract

Bitcoin miners construct blocks by selecting a set of transactions from their mempool. Each transaction in the mempool: 

1. includes a fee which is collected by the miner if that transaction is included in a block 
2. has a weight, which indicates the size of the transaction 
3. may have one or more parent transactions which are also in the mempool 

The miner selects an ordered list of transactions which have a combined weight below the maximum block weight. Transactions with parent transactions in the mempool may be included in the list, but only if all of their parents appear before them in the list. Naturally, the miner would like to include the transactions that maximize the total fee.
Here i am using Reiforcement learning to maximize my total my fee keeping the weight in check


## Setup
DRiLLS requires `Python 3.6`, `pip3` and `virtualenv` installed on the system.

1. `virtualenv .venv --python=python3`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`

## Run the Models

1. Run `python ppo.py `
2. Run `python dqn.py `

each model produces a text file with optimized selection of hashes

## How It Works
There are two major components in DRiLLS framework: 

* **Custom environment**: The main time and effort to develop this project comes from designing a custom environment where the agents can do space exploration and with this we can solve this problem as a reinforcement learning task. This environment is implemented as a session in [env.py](BTC_mining_fees_optimization_RL/env.py). To describe the environment **if the agent chooses a transaction which could decrease the Running Average of Total Aggregated Fees** then my environment will award a score of **-1** else the agent will get a reward of **+1**. Keeping the total weight of transaction less than `4,000,000`.Also the action the agent can take is either to select a transaction or not depending on the rewards condition.

* **Reinforcement Learning** environment: it employs an *Advantage Actor Critic agent (A2C)* to navigate the environment searching for the best optimization at a given state. It is implemented in [PPO.py](BTC_mining_fees_optimization_RL/PPO.py).

DRiLLS agent exploring the design space of [Max](https://github.com/lsils/benchmarks/blob/master/arithmetic/max.v) design.

For more details on the inner-workings of the framework, see in [this article on PPO](https://openai.com/blog/openai-baselines-ppo) and [in this documentation on DQN](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)

### Results of Models
Before going to the results here are some important statistics to compare the solutions:
* **Average Fees earned** - So in starting i have checked the mean of fee in the dataset which is around `1456` with average weight of `2000` so if we do basic calculation then we can get `2000` transaction in a weight of `4,000,000` so if we have `2000` transactions with `1456` fee per transaction then total fee would be `2,912,000` 
* **PPO Model Results** - With this approach I have got around `3,444,175` fees with weight around `4,000,538`
* **DQN Model Results** - From this I got `3,096,998` fees with weight of `4,011,052`
* both of the optimized fees is greater than the average also **PPO** model works best with a good of `532,175` as compared to `184,998` of **DQN** network


