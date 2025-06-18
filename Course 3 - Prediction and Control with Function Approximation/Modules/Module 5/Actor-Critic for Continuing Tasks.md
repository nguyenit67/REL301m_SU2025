# Actor-Critic for Continuing Tasks: Key Concepts and Formulas

## 1. Overview of Actor-Critic Methods

- Actor-Critic methods combine policy-based and value-based approaches in reinforcement learning (RL), enabling efficient learning in continuing (non-episodic) tasks[1].
- The **actor** learns the policy, parameterized by $\theta$, denoted as $\pi_\theta(a \mid s)$[1].
- The **critic** estimates the value function (state-value or action-value) to evaluate the policy and provide feedback to the actor[1].

---

## 2. Policy Gradient Estimation

- The goal is to estimate the gradient of the expected return (or average reward) with respect to the policy parameters $\theta$[1].
- Common methods for estimating policy gradients include:
  - **Finite Difference Methods:** Approximate the gradient by perturbing parameters and observing changes in return[1].
  - **Score Function Methods:** Use likelihood ratios to estimate gradients from sampled trajectories[1].
  - **Likelihood Ratio Methods:** Subtract a baseline from returns to reduce variance in the gradient estimate[1].
  - **Actor-Critic Methods:** Combine policy gradient estimation with value function approximation for improved efficiency[1].
  - **Natural Policy Gradient:** Incorporate the geometry of the parameter space for better convergence and stability[1].

---

## 3. Actor-Critic Algorithm Steps

1. **Initialize** actor and critic parameters randomly[1].
2. **Interact** with the environment to collect trajectories by following the current policy $\pi_\theta$[1].
3. **Compute returns or advantages** for each time step[1].
4. **Update the critic** by minimizing the error between predicted and actual returns[1].
5. **Compute the advantage function** $A(s, a)$, often as:
   
   $$
   A(s, a) = Q(s, a) - V(s)
   $$
   
   where $Q(s, a)$ is the action-value and $V(s)$ is the state-value[1].
6. **Update the actor parameters** using the policy gradient:
   
   $$
   \theta \leftarrow \theta + \alpha \nabla_\theta \log \pi_\theta(a \mid s) A(s, a)
   $$
   
   where $\alpha$ is the learning rate[1].
7. **Repeat** the process until convergence or for a fixed number of episodes[1].

---

## 4. Policy Gradient Update

- The policy gradient theorem states:
  
  $$
  \nabla_\theta J(\theta) = \mathbb{E}_{s \sim \mu_\pi, a \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a \mid s) Q_\pi(s, a) \right]
  $$
  
  where $\mu_\pi$ is the stationary distribution of states under policy $\pi$[1].
- Using the advantage function reduces variance:
  
  $$
  \nabla_\theta J(\theta) = \mathbb{E}_{s, a} \left[ \nabla_\theta \log \pi_\theta(a \mid s) A(s, a) \right]
  $$
  
  which leads to more stable and efficient learning[1].

---

## 5. Advantages of Actor-Critic Methods

- Combine the benefits of policy gradient and value function methods, allowing for both efficient exploration and stable learning[1].
- Can handle continuous action spaces, making them suitable for a wide range of RL problems[1].
- More sample efficient than pure policy gradient methods due to the use of a critic for variance reduction[1].
- Well-suited for continuing tasks with average reward objectives, as they do not require episodic resets[1].

---

## 6. Summary Table

| Step | Description                  | Formula / Notes                                                                     |
| ---- | ---------------------------- | ----------------------------------------------------------------------------------- |
| 1    | Initialize parameters        | Random initialization                                                               |
| 2    | Collect trajectories         | Follow $\pi_\theta$                                                                 |
| 3    | Compute returns / advantages | $A(s, a) = Q(s, a) - V(s)$                                                          |
| 4    | Update critic                | Minimize value function error                                                       |
| 5    | Update actor                 | $\theta \leftarrow \theta + \alpha \nabla_\theta \log \pi_\theta(a \mid s) A(s, a)$ |

---

## 7. Key Takeaways

- Actor-Critic methods provide a powerful and flexible framework for RL in continuing tasks, combining the strengths of both policy-based and value-based learning[1].
- Estimating policy gradients with a critic reduces variance and improves learning stability, especially in complex environments[1].
- The advantage function is crucial for efficient and effective policy updates[1].
- Advanced methods like natural policy gradients can further enhance convergence and performance[1].
