# Video: What is a Neural Network?

### **Introduction**

- Neural networks are **powerful nonlinear function approximators** used in reinforcement learning (RL).
- Applied in various fields, including **game-playing AI (Go, Atari), autonomous vehicles, and deep RL**.

### **Feedforward Neural Networks**

- A **feedforward neural network** consists of layers of interconnected nodes.
- **Structure**:
    - **Input Layer**: Receives data.
    - **Hidden Layers**: Process information using weighted connections.
    - **Output Layer**: Produces final results.
- Information **moves forward** without looping back (no recurrent connections).

### **Neural Network Computation**

- **Each node** in the network:
    - Receives inputs **weighted** by connection strengths.
    - Computes a **weighted sum** of inputs.
    - Applies an **activation function** to introduce **nonlinearity**.

### **Activation Functions**

- Activation functions help **transform inputs** and allow neural networks to **learn complex patterns**.
- Common types:
    - **Sigmoidal functions** (e.g., tanh, logistic function) – smooth curves for gradual changes.
    - **Rectified Linear Unit (ReLU)** – allows efficient training by keeping positive values.
    - **Threshold units** – simple binary activations.

### **Mathematical Representation**

- The feedforward process is represented using **matrix-vector multiplication**:
    - **Inputs** → Multiplied by **weights** → Processed by activation function.
    - The resulting **output vector** moves to the next layer.
- Each layer’s output **becomes the input for the next layer**, forming a **deep network**.

### **Neural Networks as Parameterized Functions**

- A neural network is essentially a **learnable mathematical function**.
- **Weights and biases** define the function’s parameters.
- Training involves **adjusting these parameters** to improve performance.

### **Key Takeaways**

- **Neural networks process data layer by layer**, applying **weights and activation functions**.
- **Feedforward networks** move data **strictly forward**, unlike recurrent networks.
- **Activation functions introduce nonlinearity**, enabling neural networks to learn **complex relationships**.
- The network is trained by **optimizing weights**, making it a **parametric model**.