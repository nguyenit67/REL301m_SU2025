# Agent Architecture: Overview of Design Choices

## Overview

Designing the architecture of a reinforcement learning (RL) agent involves making a series of key decisions that determine how the agent will perceive, act, and learn within its environment. This meeting focuses on the main architectural choices and their implications for agent performance and flexibility.

---

## 1. State Representation

-   **Raw vs. Processed Inputs:** Decide whether to use raw sensory data (like pixels or sensor readings) or to process these into higher-level features.
-   **Feature Engineering:** For small problems, hand-crafted features or state aggregation may suffice. For complex environments, automated feature extraction (e.g., using neural networks) is often necessary.
-   **Dimensionality:** The choice of representation affects the size and tractability of the state space.

---

## 2. Action Representation

-   **Discrete vs. Continuous Actions:** The agent's action space can be a finite set (e.g., up, down, left, right) or a continuous range (e.g., steering angles).
-   **Action Encoding:** Actions may be one-hot encoded or parameterized, depending on the learning algorithm and environment.

---

## 3. Policy Representation

-   **Tabular Policies:** Suitable for small, discrete state and action spaces.
-   **Parameterized Policies:** Use linear function approximation or neural networks for larger or continuous spaces.
-   **Stochastic vs. Deterministic:** Decide whether the policy should output probabilities (stochastic) or fixed actions (deterministic).

---

## 4. Value Function Representation

-   **Tabular Value Functions:** Store a value for each state or state-action pair (only feasible for small problems).
-   **Function Approximation:** Use linear methods (like tile coding) or nonlinear methods (like deep neural networks) for scalability and generalization.

---

## 5. Learning Algorithm

-   **Value-Based:** Learn value functions and derive policies (e.g., Q-learning, Sarsa).
-   **Policy-Based:** Learn the policy directly (e.g., Policy Gradient, REINFORCE).
-   **Actor-Critic:** Combine both approaches, maintaining separate structures for policy (actor) and value (critic).

---

## 6. Exploration Strategy

-   **Epsilon-Greedy:** Randomly explore actions with a small probability.
-   **Softmax/Entropy-Based:** Encourage exploration based on uncertainty or entropy.
-   **Optimistic Initialization:** Start with optimistic value estimates to drive exploration.

---

## 7. Update Mechanism

-   **Online vs. Batch:** Update agent parameters after every step (online) or after collecting a batch of experiences.
-   **Synchronous vs. Asynchronous:** Updates can be performed in lockstep with environment steps or in parallel.

---

## 8. Memory and Experience Replay

-   **Experience Replay:** Store past experiences and sample them for learning, improving data efficiency and stability.
-   **Eligibility Traces:** Use traces to assign credit to recently visited states or actions.

---

## 9. Modular Design

-   **Separation of Concerns:** Structure the agent so that components (policy, value function, exploration, memory) can be swapped or modified independently.
-   **Scalability:** Design for easy scaling to larger problems or distributed architectures.

---

## Key Takeaways

-   The architecture of an RL agent is defined by choices in state/action representation, policy/value function parameterization, learning algorithm, exploration, and memory.
-   Each design decision impacts the agent’s learning efficiency, scalability, and ability to generalize.
-   Modular and flexible architectures are preferred for experimentation and real-world deployment.
