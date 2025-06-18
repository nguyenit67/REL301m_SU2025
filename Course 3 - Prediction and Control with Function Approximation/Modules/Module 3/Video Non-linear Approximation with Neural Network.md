# Video: Non-linear Approximation with Neural Networks

### **Introduction**

- Neural networks provide a strategy for **learning useful features**, unlike tile coding, which uses predefined features.
- The video explains **how neural networks construct features** and how they act as **non-linear function approximators** for state representations.

### **Feedforward Neural Networks**

- When building a neural network, **initial weights** are assigned (often randomly).
- As an input vector passes through the network:
    - Each **node** multiplies its inputs by weights.
    - The **weighted sum** is passed through a **non-linear activation function**.
    - Each node’s output forms a **feature representation**.
- The network **learns** by adjusting weights, improving its feature representation dynamically.

### **Comparison Between Tile Coding and Neural Networks**

- **Tile Coding**:
    - Uses **fixed** parameters like tile size and number of tilings.
    - These parameters **do not change** during learning.
- **Neural Networks**:
    - Have similar **fixed parameters** (layers, nodes, activation functions).
    - But they also include **adjustable parameters** (weights) that evolve with data.

### **Non-linear Feature Construction**

- Tile coding and neural networks both **map inputs to new features**, but neural networks allow **smooth, adaptive generalization**.
- The **hidden layers** of neural networks create **complex, non-linear features**.
- Visualization of a trained agent in a **continuous 2D space** shows how feature activations reflect **environment structures** like walls.

### **Key Takeaways**

- Neural networks **learn flexible feature representations**, unlike static tile coding.
- Feature activations are **non-linear** and **smoothly adjustable**.
- Learning **from data** improves feature generalization and adaptability.
- Trained neural networks reveal **structured feature activations**, identifying environment elements dynamically.