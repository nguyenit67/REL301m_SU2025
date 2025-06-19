# Examples of Episodic and Continuing Tasks in Reinforcement Learning

## Overview

In reinforcement learning, tasks are fundamentally categorized into two types based on their interaction structure: episodic tasks and continuing tasks. This distinction is crucial for understanding how agents learn and how we design RL algorithms, as it affects reward calculation, learning objectives, and algorithm selection.

---

## Episodic Tasks

### Definition

Episodic tasks are characterized by interactions that naturally break down into distinct sequences called episodes. Each episode has a clear beginning and end, with the agent reaching one or more terminal states that conclude the current interaction sequence.

### Key Characteristics

* **Terminal States:** Episodes end when the agent reaches a designated terminal state.
* **Reset Mechanism:** After episode completion, the environment typically resets to an initial state or distribution of starting states.
* **Finite Duration:** Each episode contains a finite number of time steps.
* **Well-Defined Returns:** The total reward (return) for each episode is finite and well-defined.

### Examples of Episodic Tasks

| Task Type           | Description                | Terminal Condition          |
| ------------------- | -------------------------- | --------------------------- |
| **Board Games**     | Chess, Go, checkers        | Checkmate, win/loss/draw    |
| **Video Games**     | Atari games, arcade games  | Game over, level completion |
| **Maze Navigation** | Finding exit in a maze     | Reaching the goal state     |
| **Robot Assembly**  | Assembling a specific part | Task completion or failure  |
| **Card Games**      | Poker hands, blackjack     | Hand completion             |

---

## Continuing Tasks

### Definition

Continuing tasks involve agent-environment interactions that do not have natural endpoints. The agent operates continuously without breaking into identifiable episodes, and the interaction can theoretically continue indefinitely.

### Key Characteristics

* **No Terminal States:** There are no designated ending points in the interaction.
* **Infinite Duration:** The interaction sequence can continue forever.
* **Discounted Returns:** Future rewards are typically discounted to ensure finite return calculations.
* **Ongoing Optimization:** The agent continuously adapts its behavior based on immediate feedback.

### Examples of Continuing Tasks

| Task Type                 | Description                                      | Why Continuing                              |
| ------------------------- | ------------------------------------------------ | ------------------------------------------- |
| **Process Control**       | Managing chemical processes, temperature control | Requires constant monitoring and adjustment |
| **Financial Trading**     | Algorithmic trading decisions                    | Markets operate continuously                |
| **Autonomous Navigation** | Robot moving through warehouse                   | Operates indefinitely without natural stops |
| **Power Management**      | Solar-powered robot managing energy              | Continuous energy optimization required     |
| **Job Scheduling**        | Assigning tasks to machines                      | Manufacturing processes run continuously    |

---

## Mathematical Formulation

### Episodic Task Returns

For episodic tasks, the return is simply the sum of rewards within an episode:

$$
G_t = R_{t+1} + R_{t+2} + ... + R_T
$$

where $T$ is the terminal time step.

### Continuing Task Returns

For continuing tasks, we use discounted returns to ensure finite values:

$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ... = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
$$

where $0 \leq \gamma < 1$ is the discount factor.

---

## Algorithm Implications

### Episodic Tasks

* **Monte Carlo Methods:** Can learn from complete episodes, updating policies only after episode completion.
* **Episode-Based Evaluation:** Performance measured by averaging returns over multiple episodes.
* **Clear Learning Boundaries:** Each episode provides a complete learning experience.

### Continuing Tasks

* **Temporal Difference Learning:** Learn in real-time without waiting for episode completion.
* **Average Reward Formulation:** Often use average reward per time step as the optimization objective.
* **Continuous Adaptation:** Agent must adapt strategies based on ongoing feedback.

---

## Unified Notation

To handle both task types mathematically, we can introduce the concept of an absorbing terminal state for episodic tasks. This special state:

* Transitions only to itself
* Generates only zero rewards
* Allows unified mathematical treatment of both episodic and continuing tasks

---

## Practical Considerations

### Choosing Task Type

When formulating an RL problem, ask: "Does the interaction have a natural endpoint?" This fundamental question guides:

* **Algorithm Selection:** Different methods work better for each task type.
* **Reward Structure Design:** How to structure incentives and feedback.
* **Performance Evaluation:** How to measure and compare agent performance.

### Hybrid Approaches

Some real-world problems can be formulated either way:

* **Artificial Episodes:** Continuing tasks can be divided into artificial episodes for training purposes.
* **Extended Episodes:** Episodic tasks can be extended to study long-term behavior.

---

## Key Takeaways

* The episodic vs. continuing distinction is fundamental to RL problem formulation and affects algorithm design, reward calculation, and performance evaluation.
* Episodic tasks have clear start and end points, making them suitable for Monte Carlo methods and episode-based learning.
* Continuing tasks require discounting and real-time learning approaches like temporal difference methods.
* Understanding this distinction is crucial for selecting appropriate algorithms and designing effective RL solutions.
