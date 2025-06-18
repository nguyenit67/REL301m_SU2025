# Policy Gradient for Continuing Tasks: Key Concepts and Formulas

## 1. Objective of Policy Gradient Algorithms

- **Goal:**  
  The main goal in reinforcement learning is to maximize the long-term expected reward by directly optimizing the parameters of a policy $\pi_\theta(a \mid s)$, where $\theta$ is the parameter vector[#][7].
- **Continuing Tasks:**  
  For continuing (non-episodic) tasks, the objective can be:
  - The expected discounted return:
    
    $$
    J(\theta) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t R_{t+1} \right]
    $$
    
    where $0 < \gamma < 1$ is the discount factor[#][7].
  - The average reward per time step:
    
    $$
    \bar{r}_\pi = \lim_{T \to \infty} \frac{1}{T} \mathbb{E}_\pi \left[ \sum_{t=1}^T R_t \right]
    $$
    
    where $R_t$ is the reward at time $t$[#][10][12].

---

## 2. Average Reward Objective

- **Definition:**  
  The average reward objective focuses on maximizing the expected reward per time step in the long run, which is especially suitable for continuing tasks[#][10][12].
- **Formula:**  
  
  $$
  \bar{r}_\pi = \sum_{s} \mu_\pi(s) \sum_{a} \pi_\theta(a \mid s) r(s, a)
  $$
  
  where $\mu_\pi(s)$ is the stationary distribution of states under policy $\pi$[#][10][12].
- **Optimization Goal:**  
  Find policy parameters $\theta^*$ that maximize $\bar{r}_\pi$:
  
  $$
  \theta^* = \arg\max_\theta \bar{r}_\pi
  $$
  
  [#][10][12]

---

## 3. Policy Gradient Theorem

- **Purpose:**  
  Provides a way to compute the gradient of the expected return (or average reward) with respect to the policy parameters, enabling gradient ascent optimization[#][7][9].
- **Theorem Statement:**  
  The gradient of the expected return with respect to $\theta$ is:
  
  $$
  \nabla_\theta J(\theta) = \mathbb{E}_{s \sim \mu_\pi, a \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a \mid s) Q_\pi(s, a) \right]
  $$
  
  where $Q_\pi(s, a)$ is the action-value function under policy $\pi$[#][7][9].
- **Interpretation:**  
  The policy is improved by increasing the probability of actions that yield higher returns, as measured by $Q_\pi(s, a)$[#][7][9].

---

## 4. Challenges in Policy Gradient for Continuing Tasks

- **Changing State Distribution:**  
  Modifying the policy changes the stationary distribution $\mu_\pi(s)$, making the optimization landscape non-stationary and more challenging[#][11][13].
- **Sample-Based Estimation:**  
  The gradient is estimated using samples from the agent's interaction with the environment, which introduces variance and requires careful algorithm design[#][7][9].
- **Bias-Variance Tradeoff:**  
  Using baselines or advantage functions can reduce variance in the gradient estimate without introducing bias[#][7][8].

---

## 5. Policy Gradient Algorithm Steps

1. **Sample Trajectories:**  
   Collect trajectories $(s_t, a_t, r_{t+1})$ by following the current policy $\pi_\theta$[#][7].
2. **Estimate Returns or Advantages:**  
   Compute $Q_\pi(s_t, a_t)$ or an advantage estimate for each state-action pair[#][7][8].
3. **Compute Policy Gradient:**  
   Calculate the gradient:
   
   $$
   g = \frac{1}{N} \sum_{i=1}^N \nabla_\theta \log \pi_\theta(a_i \mid s_i) Q_\pi(s_i, a_i)
   $$
   
   where $N$ is the number of samples[#][7][9].
4. **Update Policy Parameters:**  
   Perform gradient ascent:
   
   $$
   \theta \leftarrow \theta + \alpha g
   $$
   
   where $\alpha$ is the learning rate[#][7][9].

---

## 6. Summary Table: Key Concepts

| Concept                 | Formula / Description                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------- |
| Policy                  | $\pi_\theta(a \mid s)$: probability of action $a$ in state $s$ given parameters $\theta$            |
| Average Reward          | $\bar{r}_\pi = \sum_{s} \mu_\pi(s) \sum_{a} \pi_\theta(a \mid s) r(s, a)$                           |
| Policy Gradient Theorem | $\nabla_\theta J(\theta) = \mathbb{E}_{s, a} [\nabla_\theta \log \pi_\theta(a \mid s) Q_\pi(s, a)]$ |
| Policy Update           | $\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)$                                         |

---

## 7. Key Takeaways

- Policy gradient methods directly optimize parameterized policies to maximize expected return or average reward in RL[#][7][9].
- The policy gradient theorem provides a principled way to compute gradients for policy improvement[#][7][9].
- Average reward objectives are especially suitable for continuing tasks, where the agent interacts with the environment indefinitely[#][10][12].
- Practical algorithms estimate gradients using sampled trajectories and update policy parameters via gradient ascent[#][7][9].
