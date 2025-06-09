#######################################################################
# Copyright (C)                                                       #
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)             #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# world height
WORLD_HEIGHT = 7

# world width
WORLD_WIDTH = 10

# wind strength for each column
WIND = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

# possible actions
ACTION_UP = 0
ACTION_DOWN = 1
ACTION_LEFT = 2
ACTION_RIGHT = 3

# probability for exploration
EPSILON = 0.1

# Add epsilon decay parameters
EPSILON_START = 0.1
EPSILON_END = 0.01
DECAY_STEPS = 10000

# Sarsa step size
ALPHA = 0.5

# reward for each step
REWARD = -1.0

START = [3, 0]
GOAL = [3, 7]
ACTIONS = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT]


def step(state, action):
    i, j = state
    if action == ACTION_UP:
        return [max(i - 1 - WIND[j], 0), j]
    elif action == ACTION_DOWN:
        return [max(min(i + 1 - WIND[j], WORLD_HEIGHT - 1), 0), j]
    elif action == ACTION_LEFT:
        return [max(i - WIND[j], 0), max(j - 1, 0)]
    elif action == ACTION_RIGHT:
        return [max(i - WIND[j], 0), min(j + 1, WORLD_WIDTH - 1)]
    else:
        assert False


# play for an episode
def episode(q_value, current_step):
    # Calculate epsilon for this episode
    epsilon = linear_epsilon_decay(current_step, EPSILON_START, EPSILON_END, DECAY_STEPS)

    # track the total time steps in this episode
    time = 0

    # initialize state
    state = START

    # choose an action based on epsilon-greedy algorithm with current epsilon
    action = epsilon_greedy_policy(q_value, state, epsilon)

    # keep going until get to the goal state
    while state != GOAL:
        next_state = step(state, action)
        next_action = epsilon_greedy_policy(q_value, next_state, epsilon)

        # Sarsa update
        q_value[state[0], state[1], action] += ALPHA * (
            REWARD + 1 * q_value[next_state[0], next_state[1], next_action] - q_value[state[0], state[1], action]
        )
        state = next_state
        action = next_action
        time += 1

    return time


# Linear epsilon decay function
def linear_epsilon_decay(step, epsilon_start, epsilon_end, decay_steps):
    """Linear decay of exploration epsilon"""
    # Calculate the step decay factor
    decay_factor = (epsilon_start - epsilon_end) / decay_steps
    # Calculate the current epsilon value
    epsilon = max(epsilon_start - decay_factor * step, epsilon_end)
    return epsilon


def epsilon_greedy_policy(q_value, state, epsilon):
    if np.random.binomial(1, epsilon) == 1:
        action = np.random.choice(ACTIONS)
    else:
        values_ = q_value[state[0], state[1], :]
        action = np.random.choice([action_ for action_, value_ in enumerate(values_) if value_ == np.max(values_)])
    return action


def plot_q_values(q_value):
    """Plot Q-values as a grid with arrows for each action"""
    fig, ax = plt.subplots(figsize=(15, 10))

    # Create grid
    for i in range(WORLD_HEIGHT + 1):
        ax.axhline(y=i, color="black", linewidth=0.5)
    for j in range(WORLD_WIDTH + 1):
        ax.axvline(x=j, color="black", linewidth=0.5)

    # Arrow directions for each action
    arrow_dirs = {ACTION_UP: (0, 0.3), ACTION_DOWN: (0, -0.3), ACTION_LEFT: (-0.3, 0), ACTION_RIGHT: (0.3, 0)}

    # Colors for actions
    colors = ["red", "blue", "green", "orange"]
    action_names = ["UP", "DOWN", "LEFT", "RIGHT"]

    # Plot arrows for each state-action pair
    for i in range(WORLD_HEIGHT):
        for j in range(WORLD_WIDTH):
            # Center of the cell
            center_x = j + 0.5
            center_y = WORLD_HEIGHT - i - 0.5  # Flip y-axis

            # Mark start and goal states
            if [i, j] == START:
                ax.add_patch(plt.Rectangle((j, WORLD_HEIGHT - i - 1), 1, 1, facecolor="lightgreen", alpha=0.5))
                ax.text(center_x, center_y, "START", ha="center", va="center", fontweight="bold", fontsize=8)
            elif [i, j] == GOAL:
                ax.add_patch(plt.Rectangle((j, WORLD_HEIGHT - i - 1), 1, 1, facecolor="gold", alpha=0.5))
                ax.text(center_x, center_y, "GOAL", ha="center", va="center", fontweight="bold", fontsize=8)

            # Plot arrows for each action
            for action in ACTIONS:
                dx, dy = arrow_dirs[action]
                q_val = q_value[i, j, action]

                # Scale arrow length based on Q-value (normalize)
                max_q = np.max(np.abs(q_value))
                if max_q > 0:
                    scale = min(abs(q_val) / max_q, 1.0) * 0.8
                else:
                    scale = 0.1

                # Arrow position offset from center
                offset_x = center_x + dx * 0.7
                offset_y = center_y + dy * 0.7

                # Draw arrow
                ax.arrow(
                    offset_x,
                    offset_y,
                    dx * scale,
                    dy * scale,
                    head_width=0.05,
                    head_length=0.05,
                    fc=colors[action],
                    ec=colors[action],
                    alpha=0.8,
                )

                # Add Q-value text
                text_x = offset_x + dx * 0.4
                text_y = offset_y + dy * 0.4
                ax.text(
                    text_x,
                    text_y,
                    f"{q_val:.1f}",
                    ha="center",
                    va="center",
                    fontsize=7,
                    bbox=dict(boxstyle="round,pad=0.1", facecolor="white", alpha=0.8),
                )

    # Add wind strength labels
    for j in range(WORLD_WIDTH):
        ax.text(j + 0.5, -0.3, f"W:{WIND[j]}", ha="center", va="center", fontweight="bold", fontsize=8)

    # Customize plot
    ax.set_xlim(0, WORLD_WIDTH)
    ax.set_ylim(0, WORLD_HEIGHT)
    ax.set_aspect("equal")
    ax.set_title("Q-Values Visualization\n(Arrow length proportional to |Q-value|)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Column (Wind strength shown below)")
    ax.set_ylabel("Row")

    # Add legend
    legend_elements = [plt.Line2D([0], [0], color=colors[i], lw=2, label=f"{action_names[i]}") for i in range(4)]
    ax.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(1.02, 1))

    plt.tight_layout()
    plt.savefig("images/q_values_grid.png", dpi=300, bbox_inches="tight")
    plt.show()


def figure_6_3():
    q_value = np.zeros((WORLD_HEIGHT, WORLD_WIDTH, 4))
    episode_limit = 200
    total_steps = 0

    steps = []
    for ep in range(episode_limit):
        # Pass the current total steps for epsilon calculation
        episode_steps = episode(q_value, total_steps)
        steps.append(episode_steps)
        total_steps += episode_steps

        # Print progress every 100 episodes
        if (ep + 1) % 100 == 0:
            current_epsilon = linear_epsilon_decay(total_steps, EPSILON_START, EPSILON_END, DECAY_STEPS)
            print(f"Episode {ep+1}/{episode_limit}, Current epsilon: {current_epsilon:.4f}")

    steps = np.add.accumulate(steps)

    plt.figure(figsize=(10, 6))
    plt.plot(steps, np.arange(1, len(steps) + 1))
    plt.xlabel("Time steps")
    plt.ylabel("Episodes")
    plt.title("Windy Gridworld with Linear Epsilon Decay")
    plt.savefig("images/figure_6_3.png")
    plt.close()

    # Plot Q-values visualization
    plot_q_values(q_value)

    # display the optimal policy
    optimal_policy = []
    for i in range(0, WORLD_HEIGHT):
        optimal_policy.append([])
        for j in range(0, WORLD_WIDTH):
            if [i, j] == GOAL:
                optimal_policy[-1].append("G")
                continue
            bestAction = np.argmax(q_value[i, j, :])
            if bestAction == ACTION_UP:
                optimal_policy[-1].append("U")
            elif bestAction == ACTION_DOWN:
                optimal_policy[-1].append("D")
            elif bestAction == ACTION_LEFT:
                optimal_policy[-1].append("L")
            elif bestAction == ACTION_RIGHT:
                optimal_policy[-1].append("R")
    print("Optimal policy is:")
    for row in optimal_policy:
        print(row)
    print("Wind strength for each column:\n{}".format([str(w) for w in WIND]))


if __name__ == "__main__":
    figure_6_3()
