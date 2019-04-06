# Reinforcement-Learning---Continuous-Control
Create an agent using Reinforcement learning to control a robotic arm

[![Multi tasking Robot Arm](https://img.youtube.com/vi/NxX5fiid3hg/0.jpg)](https://www.youtube.com/watch?v=NxX5fiid3hg)

This project aims to create an agent that control a robotic arm. Goal is to let this double jointed robotic arm is maintain contact with the green sphere. Reward of +0.1 is awarded for each timestep that the robotic arm is on the green sphere. Agent needs to collect a reward of +30 for 100 consecutive episodes for the environment to be considered solved.  

![Robot Arm](https://github.com/amithmp/Reinforcement-Learning---Continuous-Control/blob/master/reacher.gif)

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.


### Getting Started

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:

    - **_Version 1: One (1) Agent_**
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)

    - **_Version 2: Twenty (20) Agents_**
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)

    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux_NoVis.zip) (version 1) or [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux_NoVis.zip) (version 2) to obtain the "headless" version of the environment.  You will **not** be able to watch the agent without enabling a virtual screen, but you will be able to train the agent.  (_To watch the agent, you should follow the instructions to [enable a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the **Linux** operating system above._)

# Solution 


Agent is created using the DDPG (Deep Deterministic Policy Gradient) suitable for stochastic and continuous action spaces. This agent could solve the environment in 36 episodes as below

![Robot Arm](https://github.com/amithmp/Reinforcement-Learning---Continuous-Control/blob/master/Result chart.jpeg)

## Algorithm and Hyperparameters

This agent uses 2-layer LSTM network for both actor and critic. LSTM is chosen with the intuition that ideal action of the  agent depends on the previous action, state etc and LSTM is good to represent temporal sequences. Number of neurons is set to 256 to learn complex representation and relationship among dimensions of the state. 

**Learning Method**: Both actor and critic are set to learn (i.e. network is updated) every 50 timesteps. Each learning step involves 5 epochs.

**Learning Rate**: Learning rate is chosen to 1e-3 for the actor and 3e-3 after multiple experiments. Further, learn rate scheduler is used wherein the learning rate decays by a factor of 0.1 at each epoch. 

**Optimizer**: RMRPROP is used after trying ADAM initially. RMSPROP is found to be suitable for RNNs in many cases.

