# The Objective for Temporal Difference

# 1. Fundamental Concepts

Temporal Difference (TD) learning is a fundamental technique in Reinforcement Learning that combines ideas from Monte Carlo methods and dynamic programming.

## Key Components

- Value Estimation: Predicts future rewards from a given state
- Bootstrapping: Uses existing estimates to update current estimates
- Online Learning: Updates occur at each time step

# 2. TD Update Formula

<aside>
The core TD update rule for function approximation:

</aside>

$$
w ← w + α[R_{t+1} + γV(S_{t+1}) - V(S_t)]∇V(S_t)
$$

Where:

- $w$: weight parameters
- $α$: learning rate
- $R_{t+1}$: immediate reward
- $γ$: discount factor
- $V(S)$: value function

# 3. TD vs Monte Carlo Methods

### TD Learning

- Updates after each step
- Lower variance
- Biased estimates
- More sample efficient

### Monte Carlo

- Updates after complete episodes
- Higher variance
- Unbiased estimates
- Less sample efficient

# 4. Important Properties of TD Learning

## Advantages

- Online learning capability
- Works well with continuous tasks
- Faster convergence in many cases
- Can learn from incomplete sequences

## Limitations

- Biased value estimates
- Not true gradient descent
- May not converge to optimal solution

# 5. Semi-Gradient TD Algorithm

![image.png](The%20Objective%20for%20Temporal%20Difference%20216dd3d90e73819b877bc51f9bb7c79e/image.png)

## Semi-gradient TD(0) for estimating $\hat{v} \approx v_{\pi}$

### Inputs

- The **policy** $\pi$ to be evaluated
- A **differentiable function** $\hat{v} : \mathcal{S}^+ \times \mathbb{R}^d \to \mathbb{R}$ such that $\hat{v}(\text{terminal}, \cdot) = 0$
- **Step size parameter** $\alpha > 0$
- **Initialize value-function weights** $\mathbf{w} \in \mathbb{R}^d$ arbitrarily (e.g., $\mathbf{w} = 0$).

### Algorithm Steps

**Loop for each episode**:

**Initialize $S$**

**Loop for each step of episode**:

- Choose $A \sim \pi(\cdot | S)$.
- Take action $A$, observe $R, S'$.
- Update the weights using **semi-gradient TD(0)**:
$\mathbf{w} \gets \mathbf{w} + \alpha [R + \gamma \hat{v}(S', \mathbf{w}) - \hat{v}(S, \mathbf{w})] \nabla \hat{v}(S, \mathbf{w})$
- Set $S \gets S'$

until $S$ is terminal.

```python
# Basic semi-gradient TD(0) algorithm
def semi_gradient_td(state, action, reward, next_state, alpha):
    current_value = value_function(state)
    next_value = value_function(next_state)
    td_target = reward + gamma * next_value
    td_error = td_target - current_value
    # Update weights
    weights += alpha * td_error * gradient_value_function(state)
```

# 6. Practical Tips for Implementation

<aside>
Best Practices for New Learners:

</aside>

- Start with small learning rates (α ≈ 0.1)
- Use function approximation for continuous state spaces
- Monitor TD error for convergence
- Compare results with Monte Carlo methods when possible

# 7. Common Applications

| **Domain** | **Example Application** |
| --- | --- |
| Game Playing | Learning game strategies |
| Robotics | Motion control |
| Finance | Trading strategies |
| Resource Management | Inventory control |