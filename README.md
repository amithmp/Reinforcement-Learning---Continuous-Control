# Reinforcement-Learning---Continuous-Control
Create an agent using Reinforcement learning to control a robotic arm

![Robot Arm](https://github.com/amithmp/Reinforcement-Learning---Continuous-Control/blob/master/reacher.gif)

This project aims to create an agent that control a robotic arm. Goal is to let this double jointed robotic arm is maintain contact with the green sphere. Reward of +0.1 is awarded for each timestep that the robotic arm is on the green sphere. Agent needs to collect a reward of +30 for 100 consecutive episodes for the environment to be considered solved.  

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.


Getting Started

Download the environment from one of the links below. You need only select the environment that matches your operating system:

Version 1: One (1) Agent
  Linux: click here
  Mac OSX: click here
  Windows (32-bit): click here
  Windows (64-bit): click here

Version 2: Twenty (20) Agents
  Linux: click here
  Mac OSX: click here
  Windows (32-bit): click here
  Windows (64-bit): click here

(For Windows users) Check out this link if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

(For AWS) If you'd like to train the agent on AWS (and have not enabled a virtual screen), then please use this link (version 1) or this link (version 2) to obtain the "headless" version of the environment. You will not be able to watch the agent without enabling a virtual screen, but you will be able to train the agent. (To watch the agent, you should follow the instructions to enable a virtual screen, and then download the environment for the Linux operating system above.)

