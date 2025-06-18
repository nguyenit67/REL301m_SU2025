# Video: Comparing TD and Monte Carlo with State Aggregation

### **Introduction**

- The lecture focuses on the differences between **Temporal Difference (TD)** and **Monte Carlo (MC)** methods in **function approximation**.
- **Key questions** explored:
    - How does bias impact TD learning?
    - How do TD and MC perform in practical experiments?
    - Why might TD be preferred despite its bias?

### **Monte Carlo (MC) Learning**

- Uses **full episode returns** to update value estimates.
- Converges to a **local minimum of the Mean Squared Value Error** under reasonable assumptions.
- Requires a **large number of samples** and step-size decay for precise convergence.
- In practice, uses a **constant step size**, leading to slight oscillation around an optimum.

### **Temporal Difference (TD) Learning**

- Updates values using **future state estimates**—which introduces **bias**.
- The **TD target depends on estimated value**, meaning inaccuracies propagate.
- Even with infinite data, TD’s approximation **may remain biased**.
- TD cannot guarantee convergence to a perfect local minimum, but **bias reduces as estimates improve**.

### **Performance Comparison in Practice**

- The experiment tested **semi-gradient TD** against **Monte Carlo** using a **1,000-state Random Walk**.
- **Findings:**
    - **Long-run accuracy**: MC produced more **accurate** estimates.
    - **Early learning speed**: TD was **faster** at improving estimates.
    - **Short-term experiments matter**: In practical applications, early learning speed is **often more useful**.

### **Step-Size Experiment**

- Tested different step-size values (**Alpha**) for **TD** and **MC**:
    - **TD optimal step size**: **0.22**
    - **MC optimal step size**: **0.01**
- **Result:** TD **learned faster**, reducing error more quickly.
- **Reasoning:** TD learns **within** episodes and has **lower variance updates**, while MC relies on full returns, making it slower in early learning.

### **Key Takeaways**

- **TD vs. MC trade-off**:
    - TD **learns faster** but is biased.
    - MC **is unbiased** but slower in practical settings.
- **Real-world impact**: TD’s **fast learning** makes it preferable when resources are limited.
- **Practical preference**: Despite bias, TD is often **the better choice** when early learning performance is crucial.

Would you like me to expand on any concept?