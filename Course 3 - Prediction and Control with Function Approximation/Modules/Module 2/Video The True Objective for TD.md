# Video: The True Objective for TD

### **Introduction**

- **Semi-gradient TD** was previously introduced as **approximate gradient descent** in Mean Squared Value Error.
- **Key correction**: TD does not precisely optimize this objective but instead converges to a well-defined approximation called the **TD fixed point**.
- Goal of the lecture: Explain **TD’s actual objective** and its theoretical guarantees.

### **TD Update and Fixed Point**

- **TD value function** is represented as an **inner product** of state features and a learned weight vector.
- **Expected TD update**:
    - TD update consists of the **expected update** + a **noise term**.
    - The expected update largely determines convergence behavior.
- **Convergence Condition**:
    - The weights **converge** when the **expected TD update** equals zero.
    - The solution is termed **W_TD**.
    - If a matrix **A** (derived from state features) is invertible, then the **TD fixed point** can be expressed as **A⁻¹ b**.

### **The True Objective of TD**

- TD **does not minimize Mean Squared Value Error (MSVE)** directly.
- Instead, TD minimizes an objective based on **projected Bellman error**.
- **Key insight**:
    - In **tabular settings**, TD approximates the Bellman equation.
    - In **function approximation**, TD converges to the **TD fixed point**.
- The projected Bellman error connects TD updates to the broader **principles of reinforcement learning**.

### **Difference Between TD Fixed Point and Minimum MSVE Solution**

- The difference between TD’s solution and the **true value error solution** depends on:
    1. **Gamma (discount factor)**:
        - If **Gamma ≈ 1**, the difference can be **large**.
        - If **Gamma ≈ 0**, the TD fixed point is **very close** to the minimum value error solution.
    2. **Quality of Features**:
        - Limited feature representation can make **both solutions inaccurate**.
        - If the function approximator **perfectly represents the value function**, the two solutions become **equivalent**.

### **Why Does TD Diverge from the Minimum MSVE Solution?**

- **Bootstrapping under function approximation**:
    - TD updates **toward an estimate of future value**.
    - If the estimate of the next state is **persistently inaccurate**, TD **forever updates toward an inaccurate target**.
    - If function approximation is **high quality**, TD error remains **small**, and the solution is close to the **minimum value error solution**.

### **Key Takeaways**

- **TD does not minimize MSVE** but instead converges to a well-defined **TD fixed point**.
- The **quality of function approximation** impacts how close the TD fixed point is to the **minimum MSVE solution**.
- **Bootstrapping effects** cause persistent errors when function approximation is **poor**.
- TD remains a **powerful method** with solid theoretical guarantees, despite its divergence from MSVE minimization.