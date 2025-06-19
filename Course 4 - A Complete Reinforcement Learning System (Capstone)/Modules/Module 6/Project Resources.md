# Let's Review: Comparing TD and Monte Carlo

## Summary

Temporal Difference (TD) learning and Monte Carlo (MC) methods are two foundational approaches for estimating value functions in reinforcement learning.

### Monte Carlo (MC) Methods

-   **Update after full episodes:** MC waits until an entire episode is finished before updating value estimates.
-   **Uses actual returns:** The update is based on the actual total return observed from the episode.
-   **No bootstrapping:** MC does not use estimates of future values during the episode.

### Temporal Difference (TD) Methods

-   **Update after each step:** TD updates value estimates at every time step, using the observed reward and the estimate of the next state’s value.
-   **Bootstrapping:** TD uses its own current value estimates to update itself.
-   **Can learn online:** TD can learn before an episode ends, making it more suitable for continuing tasks.

### Key Differences

| Aspect        | Monte Carlo (MC) | Temporal Difference (TD) |
| ------------- | ---------------- | ------------------------ |
| Update timing | End of episode   | After each step          |
| Target        | Actual return    | Reward + estimated value |
| Bootstrapping | No               | Yes                      |
| Applicability | Episodic tasks   | Episodic and continuing  |
| Variance      | High             | Lower                    |
| Bias          | Low              | Can be higher            |

### Formula Comparison

-   **MC Update:**

    $$
    V(s) \leftarrow V(s) + \alpha \left[ G_t - V(s) \right]
    $$

    where $G_t$ is the actual return from time $t$ to the end of the episode.

-   **TD(0) Update:**
    $$
    V(s_t) \leftarrow V(s_t) + \alpha \left[ r_{t+1} + \gamma V(s_{t+1}) - V(s_t) \right]
    $$

---

# Joelle Pineau: About RL That Matters

## Summary

Joelle Pineau discusses the importance of making reinforcement learning research impactful and relevant to real-world problems.

### Key Points

-   **Reproducibility:** RL research should be reproducible, with clear experimental protocols and open-source code.
-   **Benchmarks:** Use meaningful and diverse benchmarks that reflect real-world challenges, not just synthetic or toy problems.
-   **Generalization:** Agents should be evaluated on their ability to generalize to new, unseen environments and tasks.
-   **Robustness:** RL solutions should be robust to noise, variability, and unexpected changes in the environment.
-   **Collaboration:** Engage with domain experts and practitioners to ensure RL solutions address real needs and constraints.
-   **Ethics and Impact:** Consider the societal and ethical implications of deploying RL systems, especially in sensitive domains.

### Practical Recommendations

-   Report negative results and failure cases.
-   Compare new algorithms to strong baselines.
-   Document all hyperparameters and experimental settings.
-   Focus on problems where RL can make a tangible difference.

---
