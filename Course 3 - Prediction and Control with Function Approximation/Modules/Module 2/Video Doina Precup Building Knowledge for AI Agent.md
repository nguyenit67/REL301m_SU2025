# Video: Doina Precup: Building Knowledge for AI Agents with Reinforcement Learning

### **Introduction**

- Speaker: **Doina Precup**, Professor at McGill University and Research Scientist at DeepMind.
- Focus: **Abstraction in Reinforcement Learning**—how agents build **procedural** and **predictive** knowledge.
- Two types of knowledge:
    - **Procedural knowledge**: Learning how to perform tasks (e.g., policies, skills, and goal-driven behavior).
    - **Predictive knowledge**: Understanding **what will happen** given an agent’s actions (e.g., value functions, models).

### **Knowledge Representation**

- **Desirable properties**:
    - Learnable: Knowledge should be acquired from data.
    - Expressive: Agents should generalize across different situations.
    - Composable: Agents should **combine** smaller knowledge pieces into larger ones.
- **State abstraction** and **function approximation** help RL agents generalize over time and space.

### **Temporal Abstraction in RL**

- RL agents start with **simple, short-term actions**, but real-world tasks require extended actions.
- **Example**: Traveling from Montreal to Edmonton involves multiple steps (cab, airport, flight), not just muscle movements.
- **Abstraction benefit**: Agents can **plan efficiently** using high-level sequences instead of thousands of small steps.
- **Solution**: **Options framework** (skills or temporally extended actions).

### **Options Framework**

- An **option** consists of:
    1. **Initiation set**: When an option **can begin** (e.g., flying only starts at an airport).
    2. **Internal policy**: Sequence of actions **within the option** (e.g., walking to the gate).
    3. **Termination condition**: When an option **ends** (e.g., reaching a destination or responding to an emergency).
- **Options create structured decision-making** at different timescales.

### **Semi-Markov Decision Processes (SMDPs)**

- **Extends standard MDPs** by incorporating **variable-length actions**.
- **Markov property still holds**, but actions have **probabilistic durations**.
- Planning algorithms like **Temporal Difference (TD) learning** still apply in SMDPs.

### **Challenges and Open Problems**

- **Combining Temporal and State Abstraction**:
    - RL agents must **think at high levels** (e.g., airports instead of centimeters).
    - Ideally, **options and state abstraction** should work **together**, but designing this efficiently is **an open research problem**.
- **Where do Options come from?**
    - **Defining termination conditions** automatically remains an **unsolved** problem.
    - Researchers seek methods for **learning options dynamically** rather than manually specifying them.

### **Key Takeaways**

- **Procedural vs. Predictive Knowledge**: RL agents need **both** types for effective learning.
- **Temporal Abstraction** is critical for handling **real-world tasks** with long time horizons.
- **Options Framework** allows structured **multi-step planning**.
- **SMDPs generalize MDPs**, enabling RL agents to plan **efficiently with temporally extended actions**.
- **Future research**: Developing methods for **automatic option discovery** and **better integration with state abstraction**.