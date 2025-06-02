#######################################################################
# Copyright (C)                                                       #
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)             #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.table import Table

matplotlib.use("Agg")

WORLD_SIZE_HEIGHT = 5
WORLD_SIZE_WIDTH = 4
# left, up, right, down
ACTIONS = [
    np.array([0, -1]),
    np.array([-1, 0]),
    np.array([0, 1]),
    np.array([1, 0]),
]
ACTION_PROB = 0.25


def is_terminal(state):
    y, x = state

    return (x == 0 and y == 0) or (x == WORLD_SIZE_WIDTH - 1 and y == WORLD_SIZE_HEIGHT - 2)


def step(state, action):
    if is_terminal(state):
        return state, 0

    next_state = (np.array(state) + action).tolist()
    y_next, x_next = next_state

    if y_next < 0 or y_next >= WORLD_SIZE_HEIGHT or x_next < 0 or x_next >= WORLD_SIZE_WIDTH:
        # Nhảy ra ngoài lưới, trở về vị trí hiện tại
        next_state = state
    elif y_next == WORLD_SIZE_HEIGHT - 1 and x_next != 1:
        # Nếu vị trí tiếp theo là hàng cuối cùng và không phải cột 1 (ô 15), dịch lên trên 1 ô (ô 12 hoặc ô 14)
        next_state = [y_next - 1, x_next]

    reward = -1
    return next_state, reward


def draw_image(image):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])

    nrows, ncols = image.shape
    width, height = 1.0 / ncols, 1.0 / nrows

    # Add cells
    for (i, j), val in np.ndenumerate(image):
        tb.add_cell(i, j, width, height, text=val, loc="center", facecolor="white")

        # Row and column labels...
    for i in range(len(image)):
        tb.add_cell(i, -1, width, height, text=i, loc="right", edgecolor="none", facecolor="none")
        tb.add_cell(-1, i, width, height / 2, text=i, loc="center", edgecolor="none", facecolor="none")
    ax.add_table(tb)


def compute_state_value(in_place=True, discount=1.0, delta=1e-4):
    new_state_values = np.zeros((WORLD_SIZE_HEIGHT, WORLD_SIZE_WIDTH))
    iteration = 0
    while True:
        if in_place:
            state_values = new_state_values
        else:
            state_values = new_state_values.copy()
        old_state_values = state_values.copy()

        for i in range(WORLD_SIZE_HEIGHT):
            for j in range(WORLD_SIZE_WIDTH):
                value = 0
                if i == WORLD_SIZE_HEIGHT - 1 and j != 1:
                    continue

                if not is_terminal([i, j]):
                    for action in ACTIONS:
                        (next_i, next_j), reward = step([i, j], action)
                        value += ACTION_PROB * (reward + discount * state_values[next_i, next_j])
                new_state_values[i, j] = value

        max_delta_value = abs(old_state_values - new_state_values).max()
        if max_delta_value < delta:
            break

        iteration += 1

    return new_state_values, iteration


def figure_4_1():
    # While the author suggests using in-place iterative policy evaluation,
    # Figure 4.1 actually uses out-of-place version.
    a_values, asycn_iteration = compute_state_value(in_place=True)
    values, sync_iteration = compute_state_value(in_place=False)
    draw_image(np.round(a_values, decimals=3))

    print("In-place: {} iterations".format(asycn_iteration))
    print("Synchronous: {} iterations".format(sync_iteration))

    plt.savefig("images/figure_4_1.png")
    plt.close()


if __name__ == "__main__":
    figure_4_1()
