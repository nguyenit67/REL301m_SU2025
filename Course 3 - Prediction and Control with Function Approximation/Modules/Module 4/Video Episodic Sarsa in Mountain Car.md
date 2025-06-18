Video: Episodic Sarsa in Mountain Car
=====================================

**Introduction**

* This lecture explores **Episodic Sarsa** in a **continuous state domain**.

* The **Mountain Car** problem is used to demonstrate **approximate TD control methods**.

* **Objective**: Drive an underpowered car up a mountain using strategic acceleration.

**Mountain Car Environment**

* The **car starts** in a valley and must reach a **flag at the hilltop**.

* **Challenges**:
  
  * Gravity is **stronger than the engine**, preventing direct ascent.
  
  * The agent must first **drive backward**, gain momentum, then **move forward**.

* **State space**:
  
  * Continuous-valued **position** and **velocity** (2D state space).

* **Actions**:
  
  * **Accelerate forward**
  
  * **Accelerate backward**
  
  * **Coast (neutral)**

**Reward Structure**

* The agent receives **1 reward per timestep** until reaching the goal.

* **No discounting ($\gamma = 1$)**, meaning the agent aims to **minimize steps** to the goal.

**Function Approximation: Tile Coding**

* **Features are generated using tile coding** to handle the continuous state space.

* **Key settings**:
  
  * **8 × 8 grids** for position and velocity.
  
  * **8 overlapping tilings** to improve approximation.
  
  * **Stacked feature representation** for independent actions.

**Formula for Tile Coding Activation**
--------------------------------------

If the agent is in state $s$, the feature vector $X(s)$ is:

$$
X(s) = [x_1, x_2, ..., x_N]
$$

Where **each feature** $x_i$ **corresponds to a tiling region activated by state $s$**.

**Optimistic Initialization**

* **Weights initialized to zero**.

* Because rewards are always **negative**, this encourages **systematic exploration**.

* **Implication**: The agent can act **greedily** without additional randomness.

**Value Function Estimation**

* Since the state space is **uncountable**, the value function is **sampled**.

* **Estimation method**:
  
  * Compute the **maximum state value** at each sampled state.
  
  * **Interpretation**:
    
    * Higher values mean **more steps required**.
    
    * Low values mean **efficient escape routes**.

**Learning Curves Analysis**

* **Three different step sizes ($\alpha$) are tested**:
  
  * $\alpha = 0.1$ (slow learning)
  
  * $\alpha = 0.5$ (faster learning)

* **Step-to-goal measurement**:
  
  * Early episodes have **high step counts**.
  
  * Performance improves, with steps stabilizing around **500 episodes**.
  
  * **Larger $\alpha$ values accelerate learning**.

**Formula for TD Update in Sarsa**
----------------------------------

$$
W \leftarrow W + \alpha \left( R + \gamma V(s') - V(s) \right) X(s)
$$

Where:

* $W$ = weight vector

* $\alpha$ = step size parameter

* $R$ = received reward

* $\gamma$ = discount factor (here $\gamma = 1$)

* $V(s)$ = current value estimate

* $V(s')$ = next state's value estimate

**Step Size Normalization**

* **Scaling step sizes based on feature vector norm** improves stability.

* With **8 tilings**, the **L1 norm of the feature vector** is always **8**.

**Formula for Normalization**
-----------------------------

$$
\alpha' = \frac{\alpha}{||X(s)||_1}
$$

Where $||X(s)||_1$ is the sum of active features.

**Key Takeaways**

* **Mountain Car demonstrates episodic Sarsa with function approximation**.

* **Tile coding enables generalization** across continuous state space.

* **Greedy exploration works due to optimistic initialization**.

* **Larger step sizes speed up learning**, but stability considerations matter.

* **Function approximation creates errors**, but offers practical benefits over tabular methods.

Would you like any refinements or additional visualization details?
