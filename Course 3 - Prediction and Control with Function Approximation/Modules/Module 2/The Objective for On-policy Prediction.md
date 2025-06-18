# The Objective for On-policy Prediction

# 1. Mean-Squared Value Error Objective

The foundation of policy evaluation in RL involves measuring how well we're estimating value functions.

$$
\overline{VE} = \sum_{s} \mu(s) \left[ v_{\pi}(s) - \hat{v}(s, \mathbf{w}) \right]^2
$$

Where:

- $v_π(s)$ is the true value function
- $v̂(s,\bold{w})$ is our approximation
- $\bold{w}$ represents the weights we're trying to optimize
- $\mu(s)$ is the fraction of time we visited $s$ when following policy $\pi$

# 2. Gradient Descent in RL

Gradient descent is a fundamental optimization technique used to minimize the value error.

![image.png](The%20Objective%20for%20On-policy%20Prediction%20216dd3d90e73816986acfbc97bb17e64/image.png)

$$
\begin{align*}
&\nabla \sum_{s \in \mathcal{S}} \mu(s) \left[ v_\pi(s) - \hat{v}(s, \mathbf{w}) \right]^2 \\
&= \sum_{s \in \mathcal{S}} \mu(s) \nabla \left[ v_\pi(s) - \hat{v}(s, \mathbf{w}) \right]^2 \\
&= -\sum_{s \in \mathcal{S}} \mu(s) 2 \left[ v_\pi(s) - \hat{v}(s, \mathbf{w}) \right] \nabla \hat{v}(s, \mathbf{w})
\end{align*}
$$

$$
\begin{align*}
\hat{v}(s, \mathbf{w}) &\doteq \langle \mathbf{w}, \mathbf{x}(s) \rangle \\
\nabla \hat{v}(s, \mathbf{w}) &= \mathbf{x}(s)
\end{align*}
$$

## Key Components:

- Policy Gradient Methods
    - Updates policy parameters $θ$ directly
    - Maximizes expected return
- Value Function Approximation
    - Estimates V(s) or Q(s,a)
    - Minimizes mean-squared error
- Actor-Critic Methods
    - Combines policy gradient and value-based approaches
    - Actor: policy function
    - Critic: value function

### **Gradient Monte Carlo**

$$
\begin{aligned}
    \mathbf{w}_{t+1} &\doteq \mathbf{w}_t + \alpha \left[ v_{\pi}(S_t) - \hat{v}(S_t, \mathbf{w}_t) \right] \nabla \hat{v}(S_t, \mathbf{w}_t) \\
    \mathbf{w}_{t+1}&\doteq \mathbf{w}_t + \alpha \left[ G_t - \hat{v}(S_t, \mathbf{w}_t) \right] \nabla \hat{v}(S_t, \mathbf{w}_t)
\end{aligned}

$$

**Gradient Monte Carlo Algorithm for Policy Evaluation**

**Inputs**

- The **policy** $\pi$ to be evaluated.
- A **differentiable function** $\hat{v} : S \times \mathbb{R}^d \to \mathbb{R}$.
- **Step size parameter** $\alpha > 0$.
- **Initialize weights** $\mathbf{w} \in \mathbb{R}^d$ arbitrarily (e.g., $\mathbf{w} = 0$).

**Algorithm Steps**

1. **Loop forever** (for each episode):
    - Generate an episode $S_0, A_0, R_1, S_1, A_1, \dots, R_T, S_T$ using $\pi$.
    - Loop for each step of episode $t = 0, 1, \dots, T-1$:
        - Update the weights using **stochastic gradient descent**:
        $\mathbf{w} \gets \mathbf{w} + \alpha \left[ G_t - \hat{v}(S_t, \mathbf{w}) \right] \nabla \hat{v}(S_t, \mathbf{w})$

# 3. State Aggregation

A method to handle large state spaces by grouping similar states together.

## Properties:

- Reduces computational complexity
- Enables better generalization
- Linear function approximation technique

<aside>
Example: If you have 8 states, you might group them into 2 clusters of 4 states each. All states in the same group share the same value estimate.

</aside>

# 4. Practical Implementation Tips

- Start with small learning rates to ensure stability
- Monitor the value error during training
- Consider state similarity when designing aggregation groups
- Use gradient clipping to prevent large updates

# 5. Common Challenges

- Balancing exploration vs exploitation
- Choosing appropriate state aggregation groups
- Dealing with non-stationary environments
- Managing the bias-variance tradeoff in value estimation

```python
# Simple example of value function update
def update_value_function(state, reward, next_state, alpha):
    current_value = v_hat[state]
    next_value = v_hat[next_state]
    td_error = reward + gamma * next_value - current_value
    v_hat[state] = current_value + alpha * td_error
```