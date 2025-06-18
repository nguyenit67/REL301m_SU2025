# Learning Parameterized Policies in Reinforcement Learning

## 1. What Are Parameterized Policies?

- **Definition:**  
  A parameterized policy is a function $\pi_\theta(a \mid s)$ that outputs the probability of taking action $a$ in state $s$, where $\theta$ is a vector of parameters[1].
- **Purpose:**  
  Directly parameterizing policies allows agents to represent and learn complex behaviors, especially in large or continuous state and action spaces[1].

---

## 2. Constraints on Policy Parameterization

- **Valid Probability Distribution:**  
  - For all $s$ and $a$, $\pi_\theta(a \mid s) \geq 0$[1].
  - For each state $s$, $\sum_{a} \pi_\theta(a \mid s) = 1$[1].
- **Parameter Vector:**  
  - The policy is typically parameterized by a vector $\theta$ (often denoted as $\boldsymbol{\theta}$)[1].

---

## 3. Softmax Policy Parameterization

- **Action Preferences:**  
  - Define a preference function $h(s, a; \theta)$ for each action in each state[1].
- **Softmax Formula:**  
  The probability of selecting action $a$ in state $s$ is:
  
  $$
  \pi_\theta(a \mid s) = \frac{\exp(h(s, a; \theta))}{\sum_{a'} \exp(h(s, a'; \theta))}
  $$
  - $h(s, a; \theta)$ is called the action preference, not the action value[1].
- **Properties:**  
  - Ensures all probabilities are positive and sum to one[1].
  - Allows smooth, differentiable policy updates[1].

---

## 4. Advantages of Policy Parameterization

- **Compact Representation:**  
  - Enables representing complex policies with relatively few parameters[1].
- **Generalization:**  
  - Facilitates generalization across similar states, improving learning efficiency[1].
- **Continuous Action Spaces:**  
  - Easily extends to continuous actions, unlike tabular or discrete policies[1].
- **Flexibility:**  
  - Can represent a wide range of policies, from simple to highly complex[1].
- **Learning Complex Policies:**  
  - Well-suited for high-dimensional state spaces and challenging tasks[1].
- **End-to-End Learning:**  
  - Supports direct optimization of the policy to maximize cumulative rewards[1].

---

## 5. Summary Table: Key Concepts

| Concept                  | Description                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------- |
| Parameterized Policy     | $\pi_\theta(a \mid s)$ outputs action probabilities given state and parameters          |
| Valid Policy Constraints | $\pi_\theta(a \mid s) \geq 0$, $\sum_a \pi_\theta(a \mid s) = 1$                        |
| Action Preference        | $h(s, a; \theta)$, used in softmax but not the same as action-value                     |
| Softmax Policy           | $\pi_\theta(a \mid s) = \frac{\exp(h(s, a; \theta))}{\sum_{a'} \exp(h(s, a'; \theta))}$ |
| Advantages               | Compactness, generalization, flexibility, continuous actions, end-to-end learning       |

---

## 6. Key Takeaways

- Parameterized policies are a powerful framework for representing and learning policies in RL[1].
- The softmax policy is a common and effective way to ensure valid, differentiable action selection[1].
- Policy parameterization enables agents to generalize, handle complex environments, and optimize behavior directly[1].
