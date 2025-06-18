# Actor-Critic Demonstration: Key Concepts and Formulas

## 1. Overview of Actor-Critic Methods

- **Actor-Critic** methods combine two components:
  - The **actor** updates the policy parameters to select better actions.
  - The **critic** estimates the value function to evaluate the current policy and provide feedback to the actor[#].
- These methods are well-suited for both discrete and continuous action spaces and can be used in both episodic and continuing tasks[#].

---

## 2. Structure of the Actor-Critic Algorithm

- **Policy (Actor):**  
  The policy is parameterized as $\pi_\theta(a \mid s)$, where $\theta$ are the policy parameters[#].
- **Value Function (Critic):**  
  The value function is parameterized as $v_w(s)$, where $w$ are the value function parameters[#].
- **Interaction Loop:**
  1. Observe current state $s_t$.
  2. Select action $a_t$ according to $\pi_\theta(a_t \mid s_t)$.
  3. Receive reward $r_{t+1}$ and next state $s_{t+1}$.
  4. Critic computes the TD error (see below).
  5. Critic updates $w$; actor updates $\theta$ using the TD error[#].

---

## 3. Temporal Difference (TD) Error

- The **TD error** measures the difference between the predicted value and the observed reward plus the value of the next state:
  
  $$
  \delta_t = r_{t+1} + \gamma v_w(s_{t+1}) - v_w(s_t)
  $$
  
  where $\gamma$ is the discount factor[#].
- The TD error is used to update both the critic and the actor[#].

---

## 4. Critic Update (Value Function)

- The critic updates its parameters $w$ to minimize the TD error:
  
  $$
  w \leftarrow w + \alpha_c \delta_t \nabla_w v_w(s_t)
  $$
  
  where $\alpha_c$ is the critic's learning rate[#].

---

## 5. Actor Update (Policy)

- The actor updates its parameters $\theta$ in the direction suggested by the TD error:
  
  $$
  \theta \leftarrow \theta + \alpha_a \delta_t \nabla_\theta \log \pi_\theta(a_t \mid s_t)
  $$
  
  where $\alpha_a$ is the actor's learning rate[#].
- This update increases the probability of actions that lead to higher-than-expected rewards and decreases it for lower-than-expected rewards[#].

---

## 6. Summary Table: Actor-Critic Updates

| Component | Update Formula                                                                             | Purpose                  |
| --------- | ------------------------------------------------------------------------------------------ | ------------------------ |
| Critic    | $w \leftarrow w + \alpha_c \delta_t \nabla_w v_w(s_t)$                                     | Value function learning  |
| Actor     | $\theta \leftarrow \theta + \alpha_a \delta_t \nabla_\theta \log \pi_\theta(a_t \mid s_t)$ | Policy improvement       |
| TD Error  | $\delta_t = r_{t+1} + \gamma v_w(s_{t+1}) - v_w(s_t)$                                      | Learning signal for both |

---

## 7. Key Takeaways

- Actor-Critic methods use the TD error as a shared learning signal for both policy and value function updates[#].
- The critic provides low-variance, bootstrapped estimates of value, while the actor directly improves the policy using gradient ascent[#].
- These methods are efficient, flexible, and form the basis for many advanced RL algorithms[#].
