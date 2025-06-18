# Exploration under Function Approximation in Reinforcement Learning

## 1. Optimistic Initial Values

- **Tabular Setting:**  
  In tabular RL, optimistic initial values are set by initializing each state-action value $Q(s, a)$ higher than the true value, encouraging the agent to explore actions it hasn't tried yet[1].

- **Function Approximation Setting:**  
  
  - Optimistic initialization means setting the weights $\mathbf{w}$ so that the estimated value $Q(s, a; \mathbf{w})$ is optimistic for all $(s, a)$[1].
  - For **binary features**: Set each weight to the largest possible return. If every state has at least one active feature, all values will be optimistic:
    
    $$
    Q(s, a; \mathbf{w}) = \mathbf{w}^\top \mathbf{x}(s, a)
    $$
    
    where $\mathbf{x}(s, a)$ is the feature vector[1].
  - For **nonlinear function approximation** (e.g., neural networks): The relationship between weights and values is complex, so achieving optimism everywhere is difficult[1].

- **Limitations:**  
  
  - If features are global (e.g., a single feature always active), any update affects all states, so optimism can be lost before some states are visited[1].
  - The effectiveness of optimistic initialization depends on how features generalize across states[1].

---

## 2. Localized vs. Global Updates

- **Tile Coding:**  
  - Tile coding can produce localized updates, meaning changes to the value function affect only a subset of states, preserving optimism in unexplored regions longer[1].
- **Neural Networks:**  
  - Neural networks can generalize aggressively, so updates may affect many states at once, potentially erasing optimism quickly[1].

---

## 3. Epsilon-Greedy Exploration

- **Definition:**  
  Epsilon-greedy selects a random action with probability $\epsilon$ and the greedy (best) action with probability $1 - \epsilon$[1].

- **Applicability:**  
  
  - Works with any function approximator (linear or nonlinear), as it only requires access to action-value estimates $Q(s, a; \mathbf{w})$[1].
  - Does not depend on how values are initialized[1].

- **Formula:**  
  
  $$
  \pi(a \mid s) = 
\begin{cases}
  1 - \epsilon + \frac{\epsilon}{|\mathcal{A}|} & \text{if } a = \arg\max_{a'} Q(s, a'; \mathbf{w}) \\
  \frac{\epsilon}{|\mathcal{A}|} & \text{otherwise}
\end{cases}
  $$
  
  where $|\mathcal{A}|$ is the number of actions[1].

- **Characteristics:**  
  
  - Epsilon-greedy is **not a directed exploration method**; it relies on randomness to discover better actions[1].
  - It is less systematic than methods based on optimism, as it does not prioritize unexplored or uncertain actions[1].

---

## 4. Summary Table

| Method                        | How It Works                                                 | Pros/Cons                                                                                           |
| ----------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Optimistic Initial Values     | Initialize $Q(s, a; \mathbf{w})$ high for all $(s, a)$       | Encourages exploration, but may be ineffective with global features or aggressive generalization[1] |
| Tile Coding (Local Updates)   | Features are localized, so updates affect only nearby states | Preserves optimism in unexplored regions longer[1]                                                  |
| Neural Networks (Global Gen.) | Updates can affect many states at once                       | May erase optimism quickly, less control over exploration[1]                                        |
| Epsilon-Greedy                | Randomly explores with probability $\epsilon$                | Simple, works with any function approximator, but not systematic or directed[1]                     |

---

## 5. Key Takeaways

- **Optimistic initial values** can encourage exploration, but their effectiveness depends on the feature representation and the generalization properties of the function approximator[1].
- **Tile coding** supports more localized updates, helping maintain optimism in unexplored areas, while **neural networks** may generalize too broadly[1].
- **Epsilon-greedy** is a robust, general-purpose exploration strategy that works with any function approximator, but it is not as systematic as optimism-based methods[1].
