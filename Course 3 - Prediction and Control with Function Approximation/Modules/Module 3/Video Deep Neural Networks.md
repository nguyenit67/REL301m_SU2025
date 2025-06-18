# Video: Deep Neural Networks

### **Introduction**

- Neural networks consist of layers of interconnected nodes that process data.
- **Depth** refers to the number of **hidden layers** in a network.
- The lecture explores **how depth affects learning**, including **feature composition** and **abstraction**.

### **Universal Approximation Property**

- A **single-layer network** can approximate any continuous function **if sufficiently wide**.
- However, deeper networks make it **easier** to approximate complex functions in practice.
- **Depth enables hierarchical learning**, where features are built progressively.

### **Feature Composition in Deep Networks**

- Each layer acts as a **module**, transforming inputs into **higher-level representations**.
- Example: Image recognition process in a neural network:
    1. **Early layers** detect **simple features** (lines, edges).
    2. **Middle layers** combine features into **shapes**.
    3. **Final layers** recognize **objects** (e.g., an owl).
- Depth allows networks to **compose modular components**, improving feature specialization.

### **Abstraction in Neural Networks**

- **Successive layers** contribute to increasingly **abstract representations**.
- Example:
    - Instead of detecting individual pixels, the network eventually learns **concepts** like an owl.
    - The highest layer might **encode an owl as a single bit** (1 = owl, 0 = no owl).
- Abstraction removes unnecessary details, making predictions more **efficient**.

### **Bottleneck Layers for Feature Selection**

- **Bottleneck layers** are designed to **filter key details**.
- These layers progressively **reduce the number of nodes**, retaining only essential information.
- Helps remove irrelevant input details, improving generalization.

### **Key Takeaways**

- **Depth improves feature composition**, allowing neural networks to **build structured representations**.
- **Hierarchical abstraction** enables efficient learning of complex patterns.
- **Bottleneck layers focus learning** on the most relevant features.
- Choosing the right architecture is **critical** for performance.