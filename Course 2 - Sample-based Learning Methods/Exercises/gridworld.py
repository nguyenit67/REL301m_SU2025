# 2.1 code demo for Monte Carlo– HoaDNT@fe.edu.vn
import numpy as np


class GridWorld:
    def __init__(self):
        self.grid_size = (3, 4)
        self.num_actions = 4  # Up, Down, Left, Right
        self.rewards = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])  # Reward of +1 in the bottom-right cell
        self.start_state = (2, 0)

    def step(self, state, action):
        # Define the dynamics of the environment
        row, col = state
        if action == 0:  # Up
            row = max(0, row - 1)
        elif action == 1:  # Down
            row = min(self.grid_size[0] - 1, row + 1)
        elif action == 2:  # Left
            col = max(0, col - 1)
        elif action == 3:  # Right
            col = min(self.grid_size[1] - 1, col + 1)
        next_state = (row, col)
        reward = self.rewards[row, col]
        return next_state, reward


def monte_carlo(grid_world, num_episodes, gamma=1.0):
    returns_sum = np.zeros(grid_world.grid_size)
    returns_count = np.zeros(grid_world.grid_size)
    V = np.zeros(grid_world.grid_size)

    for _ in range(num_episodes):
        episode = generate_episode(grid_world)
        visited_states = set()
        for t, (state, action, reward) in enumerate(episode):
            if state not in visited_states:
                visited_states.add(state)
                G = sum([gamma**i * step[2] for i, step in enumerate(episode[t:])])

                returns_sum[state] += G
                returns_count[state] += 1
                V[state] = returns_sum[state] / returns_count[state]

    return V


def generate_episode(grid_world):
    episode = []
    state = grid_world.start_state
    while True:
        action = np.random.choice(grid_world.num_actions)
        next_state, reward = grid_world.step(state, action)
        episode.append((state, action, reward))
        if next_state == (2, 3):  # Terminal state
            break
        state = next_state
    return episode


# Create a grid world environment
grid_world = GridWorld()

# Run Monte Carlo to estimate the state-value function
num_episodes = 1000
V = monte_carlo(grid_world, num_episodes)

# Print the estimated state-value function
print("Estimated State-Value Function:")
print(V)
