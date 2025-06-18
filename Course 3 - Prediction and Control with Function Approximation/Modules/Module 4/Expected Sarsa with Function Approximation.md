# Sarsa, Expected Sarsa, and Q-Learning with Function Approximation

## 1. Sarsa with Function Approximation

- **Purpose:** Learn an action-value function $Q(s, a; \mathbf{w})$ using parameter vector $\mathbf{w}$ instead of a table, enabling generalization to large or continuous state spaces[1].
- **Update Rule:**

$$
\mathbf{w} \leftarrow \mathbf{w} + \alpha \left[ R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}; \mathbf{w}) - Q(S_t, A_t; \mathbf{w}) \right] \nabla_{\mathbf{w}} Q(S_t, A_t; \mathbf{w})
$$

- $\alpha$: learning rate  
- $R_{t+1}$: reward  
- $\gamma$: discount factor  
- $\nabla_{\mathbf{w}} Q(S_t, A_t; \mathbf{w})$: gradient of $Q$ with respect to weights[1].

---

## 2. Expected Sarsa with Function Approximation

- **Key Idea:** Instead of using the value of the next action actually taken, use the expected value under the target policy for the next state[2].
- **Target Calculation:**

$$
\text{Target} = R_{t+1} + \gamma \sum_{a'} \pi(a' \mid S_{t+1}) Q(S_{t+1}, a'; \mathbf{w})
$$

- $\pi(a' \mid S_{t+1})$: probability of action $a'$ under the target policy at $S_{t+1}$[2].

- **Update Rule:**

$$
\mathbf{w} \leftarrow \mathbf{w} + \alpha \left[ R_{t+1} + \gamma \sum_{a'} \pi(a' \mid S_{t+1}) Q(S_{t+1}, a'; \mathbf{w}) - Q(S_t, A_t; \mathbf{w}) \right] \nabla_{\mathbf{w}} Q(S_t, A_t; \mathbf{w})
$$

- **Benefit:** Reduces variance in updates compared to Sarsa, especially when the policy is stochastic[2].

---

## 3. Q-Learning with Function Approximation

- **Key Idea:** Q-learning is an off-policy method; the target policy is greedy with respect to the current Q-function[3].
- **Target Calculation:**

$$
\text{Target} = R_{t+1} + \gamma \max_{a'} Q(S_{t+1}, a'; \mathbf{w})
$$

- **Update Rule:**

$$
\mathbf{w} \leftarrow \mathbf{w} + \alpha \left[ R_{t+1} + \gamma \max_{a'} Q(S_{t+1}, a'; \mathbf{w}) - Q(S_t, A_t; \mathbf{w}) \right] \nabla_{\mathbf{w}} Q(S_t, A_t; \mathbf{w})
$$

- **Relation to Expected Sarsa:** Q-learning is a special case of expected Sarsa where the target policy is greedy (i.e., probability 1 for the action with the highest Q-value)[3].

---

## 4. General Notes on Function Approximation

- **Why Use Function Approximation?**
  - Enables RL in large or continuous state-action spaces where tabular methods are infeasible[1].
  - Generalizes learning to unseen states by sharing information via features or neural network parameters[1].
- **Gradient Term:** The gradient $\nabla_{\mathbf{w}} Q(S_t, A_t; \mathbf{w})$ distributes the update to all weights according to their influence on the current Q-value[1].
- **Linear vs. Nonlinear Approximation:**
  - Linear: $Q(s, a; \mathbf{w}) = \mathbf{w}^\top \mathbf{x}(s, a)$
  - Nonlinear: e.g., neural networks, where $Q$ is a nonlinear function of $\mathbf{w}$[1].

---

## 5. Summary Table

| Method         | Target Formula                                                               | Update Rule                                                                                                                       |
| -------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Sarsa          | $R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}; \mathbf{w})$                           | $\mathbf{w} \leftarrow \mathbf{w} + \alpha [\text{Target} - Q(S_t, A_t; \mathbf{w})] \nabla_{\mathbf{w}} Q(S_t, A_t; \mathbf{w})$ |
| Expected Sarsa | $R_{t+1} + \gamma \sum_{a'} \pi(a' \mid S_{t+1}) Q(S_{t+1}, a'; \mathbf{w})$ | Same as above, with expected value as target                                                                                      |
| Q-learning     | $R_{t+1} + \gamma \max_{a'} Q(S_{t+1}, a'; \mathbf{w})$                      | Same as above, with max as target                                                                                                 |

---

## 6. Key Takeaways

- Sarsa, Expected Sarsa, and Q-learning can all be extended to use function approximation by updating weights instead of table entries[1][2].
- Expected Sarsa uses the expected value under the target policy, reducing variance[2].
- Q-learning uses the maximum action value, making it a special case of expected Sarsa[3].
- All updates involve a gradient term to distribute the error to the weights, enabling generalization[1].
