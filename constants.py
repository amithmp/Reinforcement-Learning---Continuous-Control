import torch

print("Loading new constants")

TARGET_SCORE = 30

SINGLE_AGENT = False

BUFFER_SIZE = int(1e6)  # replay buffer size
GAMMA = 0.99            # discount factor
TAU = 1e-3              # for soft update of target parameters
EPSILON = 1.0           # explore->exploit noise process added to act step
EPSILON_DECAY = 1e-6    # decay rate for noise process
n_episodes=1000         
max_t=10000
OU_SIGMA = 0.2          # Ornstein-Uhlenbeck noise parameter
OU_THETA = 0.15         # Ornstein-Uhlenbeck noise parameter


USE_LSTM = False         # Flag indicating whether to use LSTM or plan FC
NUM_LAYERS_LSTM = 2     # Number of layers in the LSTM if used
SEQUENCE_LEN = 1        # Length of sequence of inputs to LSTM. If more than 1, should process input accordingly


BATCH_SIZE = 128        # minibatch size
LR_ACTOR = 5e-4         # learning rate 
LR_CRITIC = 6e-4        # learning rate 
LR_DECAY = True
LR_DECAY_STEP = 1
LR_DECAY_GAMMA = 0.8
WEIGHT_DECAY = 0 
OPTIMIZER = "RMSPROP"
UPDATE_EVERY = 40       # how often to update the network
NUM_EPOCHS = 10          # How many learning epochs/iterations per each update
NEURON_1 = 128          # Number of Neurons in the first (FC or LSTM) layer 
NEURON_2 = 32           # Number of neurons in the second (FC) layer


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

