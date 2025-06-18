# Policy Parameterizations in Reinforcement Learning

## 1. Overview of Policy Parameterization

- **Definition:**  
  A policy parameterization defines a policy $\pi_\theta(a \mid s)$ as a function that outputs the probability of taking action $a$ in state $s$, parameterized by a vector $\theta$.
- **Purpose:**  
  Enables learning and representing complex policies in large or continuous state and action spaces, beyond tabular methods.

---

## 2. Softmax Policy for Discrete Actions

- **Action Preferences:**  
  Each action $a$ in state $s$ has a preference value $h(s, a; \theta)$, which is a parameterized function of the state and action.
- **Softmax Formula:**  
  The policy is given by:
  
  $$
  \pi_\theta(a \mid s) = \frac{\exp(h(s, a; \theta))}{\sum_{a'} \exp(h(s, a'; \theta))}
  $$
  
  ensuring a valid probability distribution over actions.
- **Properties:**  
  - All probabilities are positive and sum to 1.  
  - Differentiable with respect to $\theta$, enabling gradient-based optimization.

---

## 3. Gaussian Policies for Continuous Actions

- **Definition:**  
  For continuous action spaces, policies can be parameterized as Gaussian distributions:
  
  $$
  \pi_\theta(a \mid s) = \mathcal{N}(a \mid \mu_\theta(s), \sigma_\theta^2(s))
  $$
  
  where $\mu_\theta(s)$ and $\sigma_\theta(s)$ are parameterized mean and standard deviation functions.
- **Exploration Control:**  
  The variance $\sigma_\theta^2(s)$ controls exploration; larger variance encourages broader action sampling.
- **Advantages:**  
  - Enables smooth and fine-grained control over actions.  
  - Facilitates generalization across similar actions.  
  - Compatible with gradient-based policy optimization methods.

---

## 4. Actor-Critic with Parameterized Policies

- **Actor:**  
  Learns the policy parameters $\theta$ to improve action selection.
- **Critic:**  
  Estimates the value function (e.g., state-value or action-value) to provide feedback for policy improvement.
- **Update Mechanism:**  
  - The critic uses semi-gradient temporal difference (TD) learning to estimate value functions.  
  - The actor updates policy parameters using the temporal difference error (TDR) from the critic.

---

## 5. Gradient of the Log-Policy

- For both softmax and Gaussian policies, the gradient of the log-policy with respect to parameters $\theta$ is used in policy gradient methods:
  
  $$
  \nabla_\theta \log \pi_\theta(a \mid s)
  $$
- This gradient guides the update of $\theta$ to increase the probability of better actions.

---

## 6. Summary Table

| Policy Type     | Parameterization                                    | Key Formula                                                                         | Use Case                 |
| --------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------ |
| Softmax Policy  | Preferences $h(s,a;\theta)$                         | $\pi_\theta(a \mid s) = \frac{\exp(h(s,a;\theta))}{\sum_{a'} \exp(h(s,a';\theta))}$ | Discrete action spaces   |
| Gaussian Policy | Mean $\mu_\theta(s)$, variance $\sigma_\theta^2(s)$ | $\pi_\theta(a \mid s) = \mathcal{N}(a \mid \mu_\theta(s), \sigma_\theta^2(s))$      | Continuous action spaces |

---

## 7. Key Takeaways

- Parameterized policies provide a flexible and powerful framework for representing policies in RL.
- Softmax policies are widely used for discrete actions, ensuring valid probability distributions and differentiability.
- Gaussian policies enable smooth control and exploration in continuous action spaces.
- Actor-critic methods leverage parameterized policies and value function estimation for efficient learning.
