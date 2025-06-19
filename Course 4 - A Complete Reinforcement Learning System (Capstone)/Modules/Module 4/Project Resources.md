# Let's Review: Non-Linear Approximation with Neural Networks

## Summary

Neural networks are powerful non-linear function approximators used in reinforcement learning (RL) to estimate value functions or policies, especially in environments with large or continuous state spaces. Unlike linear methods, neural networks can capture complex, non-linear relationships between states, actions, and values.

**Key Points:**

-   Neural networks use layers of neurons with non-linear activation functions, enabling them to approximate highly complex functions.
-   In RL, neural networks can approximate both the state-value function $v(s)$ and the action-value function $q(s, a)$.
-   Training is done using gradient descent and backpropagation, where the TD error serves as the loss signal.
-   Non-linear approximation enables RL agents to generalize across similar states and actions, but introduces challenges with stability and convergence.
-   Techniques like experience replay and target networks are often used to stabilize learning, especially in deep Q-learning.

**Formula Example (TD Error for Q-learning with NN):**

$$
\text{Loss} = \left(R_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a'; w^-) - Q(s_t, a_t; w)\right)^2
$$

where $w$ are the neural network weights and $w^-$ are the target network weights.

---

# Drew Bagnell on System Identification and Optimal Control

## Summary

System identification is the process of building a model of a system from data, which is a key step in model-based reinforcement learning and optimal control. The goal is to learn a model that is accurate enough to enable reliable planning and control.

**Key Points:**

-   System identification involves collecting data from the environment and fitting a model to predict future states or rewards.
-   In model-based RL, the learned model is used for planning and policy optimization.
-   Optimal control leverages the model to compute control strategies that optimize a performance criterion.
-   Agnostic system identification methods aim to provide strong guarantees even when the true system is not in the assumed model class.
-   Iterative approaches alternate between data collection (exploration) and model updating, leading to improved policies over time.

::: mermaid
flowchart TD
A["Collect Data"] --> B["Fit Model"]
B --> C["Plan/Optimize Policy"]
C --> D["Deploy Policy"]
D --> E["Collect More Data"]
E --> B
:::

---

# Susan Murphy on RL in Mobile Health

## Summary

Reinforcement learning is increasingly used in mobile health (mHealth) to personalize interventions and support healthy behaviors. Mobile devices and wearables provide continuous streams of data, enabling RL algorithms to learn when and how to deliver interventions most effectively.

**Key Points:**

-   mHealth interventions aim to deliver timely, personalized support to users (e.g., activity reminders, stress management prompts).
-   RL is used to optimize decision rules for when and how to deliver interventions, maximizing long-term health outcomes.
-   The environment is highly dynamic, with user context (location, mood, activity) changing frequently.
-   Micro-randomized trials (MRTs) are used to collect data for offline RL analysis, enabling the construction of initial decision rules.
-   Online RL algorithms adapt these rules in real time as more user data is collected, allowing for personalization and continual improvement.
-   Challenges include high noise in reward signals, small sample sizes, and the need for interventions to be minimally intrusive.

**Formula Example (Average Reward Objective):**

$$
\bar{r}_\pi = \lim_{T \to \infty} \frac{1}{T} \mathbb{E}_\pi \left[ \sum_{t=1}^T R_t \right]
$$

::: mermaid
flowchart TD
A["User State (Sensors, Context)"] --> B["RL Agent"]
B --> C{"Intervene?"}
C -- Yes --> D["Deliver mHealth Intervention"]
C -- No --> E["Wait/Observe"]
D --> F["Observe Outcome"]
E --> F
F --> B
:::

