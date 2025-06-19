# Eligibility Traces in Reinforcement Learning

## What Are Eligibility Traces?

Eligibility traces are a fundamental mechanism in reinforcement learning that help solve the temporal credit assignment problem—determining which past states or actions should be credited (or blamed) for received rewards. An eligibility trace is a temporary record that marks which states or actions are "eligible" for learning updates when a reward or error signal is received.

---

## Why Are They Called "Eligibility Traces"?

The term "eligibility trace" comes from the idea that only certain states or actions are eligible to receive credit for a reward or error at any given time. The trace keeps track of how recently and frequently each state or action has been visited, and this information is used to determine how much each should be updated when learning occurs.

---

## How Do Eligibility Traces Work?

-   **Mechanistic View:**  
    An eligibility trace is a memory variable associated with each state or action. When a state or action is visited, its trace is incremented (or "bumped up"), and then it decays over time unless revisited.
-   **Mathematical Formulation:**  
    For a state $s$, the eligibility trace at time $t$ can be defined as:
    $$
    E_t(s) = \gamma \lambda E_{t-1}(s) + 1(S_t = s)
    $$
    where $\gamma$ is the discount factor, $\lambda$ is the trace-decay parameter, and $1(S_t = s)$ is 1 if the current state is $s$, 0 otherwise.
-   **Learning Update:**  
    When a temporal-difference (TD) error occurs, the update is distributed to all states or actions in proportion to their eligibility traces.

---

## Forward and Backward Views

-   **Forward View:**  
    Theoretical perspective—eligibility traces unify TD and Monte Carlo methods, creating a spectrum of algorithms between one-step TD and Monte Carlo.
-   **Backward View:**  
    Algorithmic perspective—eligibility traces act as a decaying memory of past events, marking which states or actions are eligible for updates when a TD error occurs.

---

## Why Use Eligibility Traces?

-   **Faster Learning:**  
    They allow information about rewards to propagate more quickly to relevant states or actions, speeding up learning compared to one-step methods.
-   **Credit Assignment:**  
    They provide a principled way to assign credit to events that happened in the recent past, not just the immediate previous step.
-   **Unification:**  
    Eligibility traces bridge the gap between TD and Monte Carlo methods, offering a family of algorithms that can be tuned for efficiency and stability.

---

## Summary Table: Key Points

| Concept               | Description                                                                |
| --------------------- | -------------------------------------------------------------------------- |
| Eligibility Trace     | Temporary record marking states/actions as eligible for learning updates   |
| Trace Update          | $E_t(s) = \gamma \lambda E_{t-1}(s) + 1(S_t = s)$                          |
| Credit Assignment     | Updates distributed to eligible states/actions based on their trace values |
| Forward/Backward View | Theoretical (what is computed) vs. mechanistic (how it is computed)        |
| Benefit               | Faster, more efficient learning and unified view of RL algorithms          |

---

## Key Takeaways

-   Eligibility traces are a core mechanism for temporal credit assignment in RL.
-   They enable faster and more effective learning by marking which states or actions are eligible for updates.
-   The name reflects their role in determining eligibility for learning changes as rewards and errors are observed.
