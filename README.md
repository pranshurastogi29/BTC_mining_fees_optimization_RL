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

### Study An Enhanced Model
The goal is to enhance the model architecture used in [drills/model.py]. An enhancement should give better results (less area **AND** meets timing constraints):
* Deeper network architecure. 
* Changing gamma rate.
* Changing learning rate.
* Improve normalization.


## How It Works
There are two major components in DRiLLS framework: 

* **Logic Synthesis** environment: a setup of the design space exploration problem as a reinforcement learning task. The logic synthesis environment is implemented as a session in [drills/scl_session.py](drills/scl_session.py) and [drills/fpga_session.py](drills/fpga_session.py).
* **Reinforcement Learning** environment: it employs an *Advantage Actor Critic agent (A2C)* to navigate the environment searching for the best optimization at a given state. It is implemented in [drills/model.py](drills/model.py) and uses [drills/features.py](drills/features.py) to extract AIG features.

DRiLLS agent exploring the design space of [Max](https://github.com/lsils/benchmarks/blob/master/arithmetic/max.v) design.

![](https://media.giphy.com/media/XbbW4WjeLuqneVbGEU/giphy.gif)

For more details on the inner-workings of the framework, see Section 4 in [the paper](https://github.com/scale-lab/DRiLLS/blob/drills-preprint/doc/preprint/DRiLLS_preprint_AH.pdf).
