# Video: Optimization Strategies for NNs

### **Introduction**

- Neural networks have become essential for **image classification, speech recognition, and natural language processing**.
- Advances in **data availability** and **computation** improved neural network training.
- **Optimization strategies** made training **faster and more effective**.

### **Importance of Initialization**

- Neural networks are trained through an **iterative optimization process**, requiring a **starting point**.
- **Choice of initial weights** affects training efficiency and final performance.
- Example: A **bad starting point** in a flat region makes gradient descent slow, while a better initialization can quickly find optimal points.

### **Weight Initialization Strategy**

- One effective method: **Randomly sample weights from a normal distribution with small variance**.
- Ensures neurons generate **diverse outputs**, improving feature representation.
- **Scaling variance** (by **1/√number of inputs**) prevents large output variations as network depth increases.

### **Gradient Descent with Momentum**

- Standard **stochastic gradient descent (SGD)** moves weights **toward a local minimum**.
- **Momentum modification** accelerates learning:
    - Maintains a history of past gradients.
    - **If gradients remain consistent**, momentum **increases step size**, speeding convergence.
    - **If gradients fluctuate**, momentum stabilizes updates.

### **Step Size Adaptation**

- Traditional **SGD uses a global step size**, which may be **too large for some weights** and **too small for others**.
- Solution: **Use separate step sizes per weight**, adjusting based on learning statistics.
- **Vector step size scaling** improves training speed and stability.

### **Key Takeaways**

- **Initialization affects training efficiency**—proper weight selection prevents slow learning.
- **Momentum speeds up gradient descent**, preventing oscillations.
- **Adaptive step sizes improve learning**, reducing sensitivity to poorly scaled updates.
- These strategies **optimize neural network training**, improving accuracy and reducing computational costs.