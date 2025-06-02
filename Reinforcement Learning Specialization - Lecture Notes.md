# Course 1 - Fundamentals of Reinforcement Learning

## Module 2

New terms:

short/long-term reward

policies

planning methods

dynamic programming

reward 

time steps

#### Video: Sequential Decision Making with Evaluative Feedback

##### Action-Value function

- Giá trị của hành động ($q_*$) là giá trị kỳ vọng của tất cả các giá trị khả thi khi thực hiện hành động *a*
  
  $$
  \begin{align*}
q_*(a) &\doteq \mathbb{E}[R_t \mid A_t = a] \quad \forall a \in \{1, \ldots, k\} \\
&= \sum_{r} p(r \mid a)\, r
\end{align*}
  $$
  
  Giá trị của hành động $q$ là số chưa biết -> cần được ước tính!
  $q_*$: giá trị kỳ vọng thực sự
  $q$: giá trị kỳ vọng ước tính

- Mục tiêu là chọn hành động *a* để tối đa hóa phần thưởng/giá trị kỳ vọng của hành động
  
  $$
  \underset{a}{\arg\max}\; q_*(a)
  $$

![69ddb2b8-9454-4cf4-9c3f-c35c67177e87](file:///D:/Disk/Computer/Pictures/Typedown/69ddb2b8-9454-4cf4-9c3f-c35c67177e87.png) 

![98116610-cbc8-4a9f-81f0-fbd2d5c5ef17](file:///D:/Disk/Computer/Pictures/Typedown/98116610-cbc8-4a9f-81f0-fbd2d5c5ef17.png)

How is the bandit problem similar to or different from the supervised learning problem?

**Vietnamese**

Giống: cả 2 đều có mục tiêu đạt được kết quả tối ưu được đo lường bởi 1 hàm số (supervised: loss function, bandit problem: q*/reward function), supervised được train trên 1 tập data hữu hạn và cố định, bandit problem thì có số lượng action là 1 tập hữu hạn các action (K).

Khác: supervised learning tối đa hóa hàm mất mát trên 1 tập data cố định, ko thay đổi, label là cố định; bandit problem thì có label là giá trị kỳ vọng trên 1 phân phối xác suất.

**English**

##### **Similarities**

1. ###### **Optimization Objective**
   
   * Both aim to optimize a measurable function:
     
     * _Supervised Learning_: Minimizes a **loss function** (e.g., cross-entropy, MSE).
     
     * _Bandit Problems_: Maximizes a **reward function** (e.g., Q*-value, expected reward).

2. ###### **Finite Action Space**
   
   * Supervised learning uses a fixed, finite dataset.
   
   * Bandit problems assume a finite set of **K actions** (e.g., choosing between K ad variants).

##### **Key Differences**

| **Aspect**               | **Supervised Learning**                        | **Bandit Problems**                                                   |
| ------------------------ | ---------------------------------------------- | --------------------------------------------------------------------- |
| **Data Dynamics**        | Static dataset with fixed labels               | Dynamic, stochastic rewards from a distribution                       |
| **Feedback Type**        | Full feedback (labels for all inputs)          | Partial feedback (reward only for chosen action)                      |
| **Exploration Strategy** | No exploration needed (deterministic training) | Requires **exploration-exploitation trade-off** (e.g., ε-greedy, UCB) |
| **Objective**            | Generalize to unseen data                      | Maximize cumulative reward over interactions                          |

#### Video: Learning Action Values

##### Sample-Average Method

$$
\begin{align*}
Q_t(a) &\doteq \frac{\text{sum of rewards when } a \text{ taken prior to } t}{\text{number of times } a \text{ taken prior to } t} \\\\
      &= \frac{\sum_{i=1}^{t-1} R_i}{t - 1}
\end{align*}
$$

##### Greedy action

Method of choosing action: choosing the **greedy action** a.k.a the action currently has the largest estimated value

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/282fccc4-37e6-4625-a43f-cd80ab15de68.png" alt="282fccc4-37e6-4625-a43f-cd80ab15de68" data-align="center">

#### Video: Estimating Action Values Incrementally

##### <u><mark>Incremental update rule</mark></u>

![701f6f29-67dd-4d85-88e1-8f29879f9ba7](file:///D:/Disk/Computer/Pictures/Typedown/701f6f29-67dd-4d85-88e1-8f29879f9ba7.png)

$$
\textit{NewEstimate} \gets \textit{OldEstimate} + \textit{StepSize} \left[ \textit{Target} - \textit{OldEstimate} \right] 
\\ \\
Q_{n+1} = Q_n + \alpha_n \left( R_n - Q_n \right)
\\ \\
\alpha_n \to [0,1]

$$

Sample average method

$$
\alpha_n = \frac{1}{n} \\[1.5em]
\alpha \space \text{(step size),} \space \text{là 1 hằng số}
$$

##### **Non-stationary bandit problem (rewad ko cố định và có thể thay đổi  theo thời gian)**

Trong các bài toán non-stationary (có tính thay đổi theo thời gian, học trực tuyến a.k.a online learning), stepsize là 1 hằng số cố định sẽ giúp estimate và điều chỉnh $q$ tốt và nhanh hơn là 1 step size giảm dần theo thời gian (decaying: $\frac{1}{n}$)

![a10bd3be-0c30-49bc-9b6e-ee49677ad36f](file:///D:/Disk/Computer/Pictures/Typedown/a10bd3be-0c30-49bc-9b6e-ee49677ad36f.png)

the most recent rewards affect the estimate more than older rewards (các reward mới nhất ảnh hưởng đến giá trị ước lượng hơn các reward ở các bước xa hơn)



##### **Decaying past rewards**

$$
\begin{align*}
Q_{n+1} &= Q_n + \alpha_n \left( R_n - Q_n \right) \\
        &= \alpha_n R_n + Q_n - \alpha_n Q_n \\
        &= \alpha_n R_n + (1 - \alpha_n) Q_n \\
        &= \alpha_n R_n + (1 - \alpha_n)\left[\alpha_n R_{n-1} + (1 - \alpha_n) Q_{n-1}\right] \\
        &= \alpha_n R_n + (1 - \alpha_n)\alpha_n R_{n-1} + (1 - \alpha_n)^2 Q_{n-1} \\
        &= \alpha_n R_n + (1 - \alpha_n)\alpha_n R_{n-1} + (1 - \alpha_n)^2\alpha_n R_{n-2} + \dots \\
        &\quad + (1 - \alpha_n)^{n-1}\alpha_n R_1 + (1 - \alpha_n)^n Q_1 \\[\quad]
        &= (1 - \alpha)^n Q_1 + \sum_{i=1}^{n} \alpha (1 - \alpha)^{n-i} R_i

    &\\\\
    &Q_1 \to \textbf{initial action-value}

\end{align*}
$$

Đóng góp của Q_1 với giá trị ước tính tại bước $n+1$ giảm dần theo cấp lũy thừa theo thời gian, các giá trị reward ở các bước cũ đóng góp theo cấp lũy thừa ít hơn. Sự ảnh hưởng của giá trị khởi tạo ($Q_1$) tiến gần về $0$ khi càng có thêm nhiều data, các giá trị mới nhất quyết định giá trị ước tính hiện tại ($Q_{n+1}$) 

### Exploration vs. Exploitation Tradeoff

#### Video: What is the trade-off?

##### Exploration and Exploitation

- **Exploration** - **improve** knowledge for **long-term** benefit

- **Exploitation** - **exploit** knowledge for **short-term** benefit (being greedy w.r.t estimated values, may not actually get the most reward)

- Round Robin fashion: tuần tự theo chu kỳ

Các phương pháp để cân bằng giữa Exploration và Exploitation

##### Epsilon-Greedy Action Selection

$$
A_t \leftarrow
\begin{cases}
    \displaystyle \arg\max_{a} Q_t(a) & \text{with probability } 1 - \epsilon \\\\
    a \sim \mathrm{Uniform}(\{a_1, \ldots, a_k\}) & \text{with probability } \epsilon
\end{cases}
$$

Lựa chọn khám phá (explore) ngẫu nhiên 1 hành động với xác suất $\epsilon$ từ xác suất phân phối đều, và lựa chọn greedy hành động có ước tính phần thưởng $Q_t$ lớn nhất trong số các hành động (exploit)

#### Video: Optimistic Initial Values

![8c330cdf-be2e-4b0f-bd53-34a7666ded27](file:///D:/Disk/Computer/Pictures/Typedown/8c330cdf-be2e-4b0f-bd53-34a7666ded27.png)

Khởi tạo giá trị kỳ vọng ước lượng khởi đầu cao và thực hiện chiến thuật lựa chọn tham lam (greedy selection) giúp agent có thể explore các lựa chọn khác nhau ở các timestep đầu tiên và update dần về giá trị hành động thực tế

![9b941a14-20b5-436c-b00f-75df53c628d4](file:///D:/Disk/Computer/Pictures/Typedown/9b941a14-20b5-436c-b00f-75df53c628d4.png)

**Giới hạn**:

- Chỉ explore ở các bước đầu tiên, sau khi đến bước nào đó sẽ dừng explore

- Ko phù hợp với các bài toán có reward thay đổi theo thời gian (non-stationary problems)

- Không thể biết được giá trị khởi đầu lạc quan nên để là bao nhiêu (vì không biết giá trị tối đa của reward)

#### Video: Upper-Confidence Bound (UCB) Action Selection

<img src="file:///D:/Disk/Computer/Pictures/Typedown/9708c4b5-0bd3-469e-990d-4a21f65f0bef.png" title="" alt="9708c4b5-0bd3-469e-990d-4a21f65f0bef" data-align="center">**Optimism in the Face of Uncertainty**

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/5b9c12ec-9468-4456-9a09-08757586c767.png" alt="5b9c12ec-9468-4456-9a09-08757586c767" data-align="center" style="zoom:67%;">

##### Upper-Confidence Bound (UCB) Action Selection

chọn action có cận trên của giá trị hành động là cao nhất

$$
A_t \doteq \argmax_a \left[ Q_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \;\right]
$$

$c \sqrt{\frac{\ln t}{N_t(a)}}\;$ is upper-confidence bound (UCB) exploration term

$c$ is user-specified parameter that controls the amount of exploration

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/18a97f24-8a9d-4624-87b0-638931dc1d9f.png" alt="18a97f24-8a9d-4624-87b0-638931dc1d9f" style="zoom:50%;" data-align="center">

#### Video: Jonathan Langford: Contextual Bandits for Real World Reinforcement Learning

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/8910efa2-9370-488b-8f87-bb6e540c075d.png" alt="8910efa2-9370-488b-8f87-bb6e540c075d" style="zoom:25%;" data-align="center">

There's is a gap between the simulator and the reality.

##### **Real World Reinforcement Learning**

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/b4fa794d-6953-4b4e-b544-cf66fcd002f9.png" alt="b4fa794d-6953-4b4e-b544-cf66fcd002f9" style="zoom:25%;" data-align="center">

##### **An example: Contextual Bandits**

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/823786ac-433a-4e44-916a-9145bc55d585.png" alt="823786ac-433a-4e44-916a-9145bc55d585" data-align="center" style="zoom:33%;">

Having a set of possible news articles in interest today, suggest news article for new user come to website that they maybe have interest in, get feedback about whether or not they actually read the article. 

Repeatedly:

1. Observe features $\textcolor{red}{x}$ (user geolocation, past profile behaviour, features of available actions,...)

2. Choose action $\textcolor{red}{a \in A}$

3. Observe reward $\textcolor{red}{r}$

**Goal: Maximize reward**

Major caveat: No credit assignment (for selected action, what's the reward if we had chosen a different action?)

#### Video: Week 1 Summary

Exploration vs Exploitation strategies

- ε-Greedy Action Selection

- Optimistic Initial Values

- Upper-Confidence Bound (UCB) Action Selection

## Module 3

### Introduction to Markov Decision Processes

#### Video: Markov Decision Processes

* Các tình huống khác nhau sẽ xuất hiện các lựa chọn hành động khác nhau

* Hành động dẫn đến trạng thái của thế giới thay đổi action -> state

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/83a0a0d4-1bee-4ab7-ad10-a54f882c84d9.png" alt="83a0a0d4-1bee-4ab7-ad10-a54f882c84d9" data-align="center" style="zoom:50%;">

**Markov Decision Processes (MDPs)** là các khung toán học được sử dụng để mô hình hóa các vấn đề ra quyết định, trong đó một tác nhân tương tác với một môi trường trong một chuỗi các bước thời gian riêng biệt (discrete time steps).

##### Markov Decision Processes terms:

- **Agent**: là thực thể mà chúng ta đang huấn luyện để đưa ra các quyết định chính xác.

- **Environment**: môi trường xung quanh mà agent tương tác.
* **State**: (thông tin) trạng thái hiện tại của agent trong môi trường để đưa ra quyết định.

* **Action**: lựa chọn mà agent thực hiện tại mỗi bước thời gian hiện tại.

* **Policy**: Policy là quá trình suy nghĩ hoặc chiến lược đứng sau việc lựa chọn một action.

* **P (Transition Probability):** `P(s'|s, a)` cho biết xác suất chuyển sang trạng thái `s'` khi thực hiện hành động `a` tại trạng thái `s`. Điều này thể hiện tính ngẫu nhiên của môi trường.

* **R (Reward Function):** `R(s, a, s')` xác định phần thưởng nhận được ngay lập tức sau khi chuyển từ trạng thái `s` sang trạng thái `s'` do thực hiện hành động `a`.

Sometimes:

* **γ (Discount Factor):** Một giá trị trong khoảng từ 0 đến 1, quyết định mức độ quan trọng của các phần thưởng trong tương lai.

##### How MDPs Work

Ở mỗi bước thời gian:

* Agent quan sát trạng thái hiện tại.

* Chọn một action dựa trên policy (một ánh xạ từ state đến action).

* Environment chuyển sang một state mới dựa trên xác suất chuyển tiếp (transition probabilities).

* Agent nhận được reward tương ứng với action đã thực hiện.

Mục tiêu là tìm ra một **chính sách tối ưu**  để tối đa hóa tổng phần thưởng kỳ vọng (expected cumulative reward) theo thời gian.

##### The dynamics of an MDP (Markov property)

**Khi agent thực hiện hành động `a` trong trạng thái `s`**, sẽ có nhiều trạng thái kế tiếp $s'$ và phần thưởng $r$ có thể xảy ra. Hàm động lực chuyển tiếp $P(s', r | s, a)$ mô tả xác suất của từng kết quả $(s', r)$.

**Công thức:**

$$
P(s', r | s, a) = ℙ(S_{t+1}=s', R_{t+1}=r | S_t=s, A_t=a)
$$

$p(s',r|s,a)$ là xác suất xảy ra trạng thái $s'$ và nhận được phần thưởng $r$ với hành động $a$ từ trạng thái $s$

**Giải thích:** 

- Hàm này định nghĩa "luật chơi" của môi trường:
  
  - **Đầu vào:** Trạng thái hiện tại `s` + hành động `a`.
  - **Đầu ra:** Phân phối xác suất cho tất cả cặp `(s', r)` có thể.

- Ví dụ: Robot di chuyển nhưng có 10% khả năng trượt (sang trạng thái khác ngoài dự định).

**Tính chất:**

* ∑ₛ',ᵣ P(s', r | s, a) = 1 (tổng xác suất bằng 1)
  
  $$
  \begin{gather*}
p : \mathcal{S} \times \mathcal{R} \times \mathcal{S} \times \mathcal{A} \to [0, 1] \\
\sum_{s' \in \mathcal{S}} \sum_{r \in \mathcal{R}} p(s', r \mid s, a) = 1, \forall s \in \mathcal{S},\ a \in \mathcal{A}(s)
\end{gather*}
  $$

* Môi trường **deterministic** là trường hợp đặc biệt: $P(s', r | s, a) = 1$ cho một cặp $(s', r)$ duy nhất.

* Tính chất Markov: trạng thái tương lai chỉ phụ thuộc vào trạng thái và hành động hiện tại, không phải vào chuỗi các sự kiện trước nó (ghi nhớ về các trạng thái trước đó không giúp cải thiện cho dự đoán về tương lai)

#### Video: Examples of MDPs

**Dynamics of the Recycling Robot**

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/8897e08c-f373-457e-8eb2-42848d7d5536.png" alt="8897e08c-f373-457e-8eb2-42848d7d5536" data-align="center" style="zoom:33%;">

state, action có thể đơn giản, chi tiết (low-level) hoặc abstract (high-level)

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/d792b477-04bc-403d-84aa-779489a71c20.png" alt="d792b477-04bc-403d-84aa-779489a71c20" style="zoom:67%;" data-align="center">

### Goal of Reinforcement Learning

#### Video: The Goal of Reinforcement Learning

##### Goal of an Agent: Formal definition

Mục tiêu của agent là tối đa hóa tổng phần thưởng nhận về (return a.k.a giá trị tích lũy) trong tương lai

$$
G_t \doteq R_{t+1} + R_{t+2} + R_{t+3} + ...
$$

$G_t$ là 1 biến ngẫu nhiên

$$
\begin{gather*}
\mathbb{E}[G_t] = \mathbb{E}[\ R_{t+1} + R_{t+2} + R_{t+3} + \dots + R_T \ ]

\\\\
\textbf{\textcolor{red}{maximize the expected return}}
\end{gather*}
$$

Tối đa hóa giá trị mong đợi cho phần thưởng nhận được trong tương lai (tổng các phần thưởng phải là 1 số hữu hạn)

$T$ là thời điểm kết thúc (final timestep)

##### Epsodic Tasks (tập hành động)

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/b77e2e6c-1f87-478c-bf13-236ad4ebfed4.png" alt="b77e2e6c-1f87-478c-bf13-236ad4ebfed4" data-align="center" style="zoom:67%;">

Các tương tác được chia thành các đoạn nhỏ gọi là các episode,  mỗi episode bắt đầu độc lập với kết thúc của episode trước đó, khi 1 episode kết thúc, agent được đặt lại về trạng thái bắt đầu, mỗi episode sẽ có 1 trạng thái kết thúc.

Ví dụ: 

* Chơi một ván cờ (mỗi ván là một episode) -> trạng thái kết thúc: thắng, hòa, đầu hàng

* Một lần robot di chuyển từ vị trí xuất phát đến đích

##### Discussion Prompt: Is the reward hypothesis sufficient?

- Multi-objective tasks: Can’t balance goals like speed and safety in self-driving cars.

- Risk-sensitive tasks: Ignores risk, e.g., investors want to avoid rare catastrophic losses, not just maximize average return.

- Modal/counterfactual tasks: Can’t reason about what could have happened, e.g., a robot must maintain the ability to avoid collisions.

- Dynamic/subjective preferences: Can’t adapt to changing or conflicting values, e.g., recommenders may need to shift from engagement to well-being.

- Non-Markovian dependencies: Can’t encode history-based requirements, e.g., loan systems must ensure fairness over time.

#### Video: Michael Littman: The Reward Hypothesis

##### Whence Behavior?

- give a man a fish and he'll eat for a day
  
  - Programming (GOFAI -  Good-old fashioned AI)

- teach a man to fish and he'll eat for a lifetime
  
  - Examples (LfD)

- give a man a taste for fish and he'll figure out how to get fish, even if the details change!
  
  - Optimization (RL)

##### Goals as Rewards

- 1 for goal, 0 otherwise
  
  - goal-reward representation

- -1 for not goal, 0 once goal reached
  
  - action-penalty representation

##### Whence Rewards?

- Programming 
  
  - Coding
  
  - Human-in-the-loop (con người hay thay đổi câu trả lời của mình tùy theo cách mà agent đang học - non-stationary reward)

- Examples
  
  - Mimic reward (đưa ra ví dụ về phần thưởng bởi ví dụ, agent sẽ học cách "sao chép" phần thưởng được cung cấp, reward -> behavior)
  
  - Inverse reinforcement learning (trainer cho agent học bằng việc cung cấp ví dụ về "hành vi" mong muốn để agent tự suy luận ra reward mục tiêu cần đạt được tối ưu tương đương cho "hành vi" được cung cấp, behavior -> reward)

- Optimization
  
  - Evolutionary optimization: cho nhiều model cùng học và model nào "sống sót" (có kết quả và thuật toán tốt hơn 1 ngưỡng) thì sẽ được giữ lại cho các bước học tiếp theo
  
  - Meta RL

##### Challenges to the Hypothesis (Những thách thức của giả thuyết phần thưởng)

- Mục tiêu không phải là giá trị kỳ vọng của phần thưởng tích lũy 
  
  - Risk-averse problem (giảm thiểu rủi ro): chọn kết quả tốt nhất mà ít khả năng có biến cố xảy ra nhất, có thể mô hình hóa bằng việc khuếch đại các kết quả tiêu cực trong phần thưởng
  
  - Cân bằng đa dạng hóa

- Có thể tương thích với cách học như của con người không?
  
  - Theo đuổi 1 nhiệm vụ mù quáng không phải luôn luôn tốt
  
  - Mục tiêu có thể thay đổi, phát triển theo thời gian

### Continuing Tasks

#### Video: Continuing Tasks

| Episodic Tasks                                         | Continuing Tasks                                 |
| ------------------------------------------------------ | ------------------------------------------------ |
| Interaction breaks naturally into episodes             | Interaction goes on continually                  |
| Each episode ends in a terminal state                  | No terminal state                                |
| Episodes are independent                               | Results are dependent                            |
| $G_t \doteq R_{t+1} + R_{t+2} + R_{t+3} + \dots + R_T$ | $G_t \doteq R_{t+1} + R_{t+2} + R_{t+3} + \dots$ |

##### Example: Smart thermostat which regulates the temperature of a building

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/6958a5bb-ad70-4072-83bf-e07cc16209c3.png" alt="6958a5bb-ad70-4072-83bf-e07cc16209c3" data-align="center" style="zoom:33%;">

##### Discounting

$$
\begin{align*}
G_t &\doteq R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots + \gamma^{k-1} R_{t+k} + \dots  
\\
&= \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
\end{align*}
$$

$G_t$ luôn là hữu hạn khi $0 \leq \gamma < 1$, $\gamma$ là tỷ số chiết khấu

###### Chứng minh rằng $G_t$ hữu hạn khi $0 \leq \gamma < 1$

Giả sử $R_{max}$ là phần thưởng tối đa mà agent  có thể nhận được

$$
\begin{align*}
G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}
   \leq \sum_{k=0}^{\infty} \gamma^k R_{\max}
   &= R_{\max} \sum_{k=0}^{\infty} \gamma^k \\
   &= R_{\max} \times \frac{1}{1 - \gamma}
\end{align*}


$$

Mà $\sum_{k=0}^{\infty} \gamma^k$ là tổng của 1 chuỗi hình học hội tụ (chuỗi có tổng tiến tới một giá trị hữu hạn) khi $\gamma < 1$ có tổng hội tụ về $\frac{1}{1 - \gamma}$.

$\Rightarrow R_{\max} \times \frac{1}{1 - \gamma}$ là hữu hạn và là cận trên của $G_t$ 

$\Rightarrow G_t$ là hữu hạn

##### Effect of $\gamma$ on agent behavior

- $\gamma = 0$
  
  $$
  \begin{align*}
G_t &\doteq R_{t+1} + \textcolor{red}\gamma R_{t+2} + \textcolor{red}{\gamma^2} R_{t+3} + \dots + \textcolor{red}{\gamma^{k-1}} R_{t+k} + \dots \\
&= R_{t+1} + \textcolor{red}{0} R_{t+2} + \textcolor{red}{0^2} R_{t+3} + \dots + \textcolor{red}{0^{k-1}} R_{t+k} + \dots \\
&= R_{t+1}
\end{align*}
  $$
  
  Khi  $\gamma = 0$, giá trị tích lũy $G_t$ sẽ chỉ đơn giản là reward ở bước tiếp theo, agent sẽ có tầm nhìn ngắn hạn và chỉ quan tâm đến phần thưởng mong đợi tức thời 

- $\gamma \to 1 $
  
  $$
  \begin{align*}
G_t &\doteq R_{t+1} + \textcolor{red}\gamma R_{t+2} + \textcolor{red}{\gamma^2} R_{t+3} + \dots + \textcolor{red}{\gamma^{k-1}} R_{t+k} + \dots \\
&\approx R_{t+1} + \textcolor{red}{1} R_{t+2} + \textcolor{red}{1^2} R_{t+3} + \dots + \textcolor{red}{1^{k-1}} R_{t+k} + \dots \\
&= R_{t+1} + R_{t+2} + R_{t+3} + \dots + R_{t+k} + \dots
\end{align*}
  $$
  
  Phần thưởng tức thời và trong tương lai có độ quan trọng gần bằng nhau nên agent sẽ có tầm nhìn xa hơn 

##### Recursive nature of returns (tính đệ quy của giá trị tích lũy)

$$
\begin{align*}
G_t &\doteq R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \gamma^3 R_{t+4} + \dots \\
&= R_{t+1} + \gamma \left( R_{t+2} + \gamma R_{t+3} + \gamma^2 R_{t+4} + \dots \right) \\
G_t &= R_{t+1} + \gamma G_{t+1}
\end{align*}
$$

## Module 4

### Policies and Value Functions

#### Video: Specifying Policies

##### Deterministic Policy (chính sách xác định)

$\pi$ (policy: chính sách) là phương pháp lựa chọn (ánh xạ) hành động $a$ từ trạng thái $s$.<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/f4b45efa-e490-418c-b1ad-25f60e0dafee.png" alt="f4b45efa-e490-418c-b1ad-25f60e0dafee" style="zoom:50%;" data-align="center">

##### Stochastic Policy (chính sách ngẫu nhiên)

$\pi(a|s)$ là xác suất lựa chọn hành động $a$ khi đang ở trạng thái $s$, tổng xác suất của tất cả hành động $a$ trong trạng thái $s$ phải bằng 1 và không có xác suất hành động nào được là số âm.

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/2e5e7d2e-9819-4919-8b95-43ba543e7f5f.png" alt="2e5e7d2e-9819-4919-8b95-43ba543e7f5f" style="zoom:33%;" data-align="center">

###### Stochastic Policy Example

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/1f2e3f92-db5d-40a3-843f-d83d2a35d86b.png" alt="1f2e3f92-db5d-40a3-843f-d83d2a35d86b" style="zoom:33%;" data-align="center">

##### Valid and invalid policies

Policy trong MDPs chỉ quyết định hành động tiếp theo dựa trên trạng thái $s$ hiện tại, không phụ thuộc vào các hành động hay trạng thái trước đó. Trong MDPs, trạng thái hiện tại luôn chứa đầy đủ thông tin cho việc ra quyết định cho hành động tiếp theo.

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/34469551-a1f8-4cfa-9f07-8da576c60176.png" alt="34469551-a1f8-4cfa-9f07-8da576c60176" style="zoom:33%;" data-align="center">

#### Video: Value Functions

##### State-value functions

Giá trị tích lũy kỳ vọng khi bắt đầu ở trạng thái $s$ với chính sách $\pi$ 

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/04183a6a-c14a-4fd5-a7f7-c34e7f583bc6.png" alt="04183a6a-c14a-4fd5-a7f7-c34e7f583bc6" style="zoom:50%;" data-align="center">

##### Action-value functions

Giá trị tích lũy kỳ vọng khi bắt đầu ở trạng thái $s$, thực hiện hành động $a$ với chính sách $\pi$

$$
q_{\pi}(s, a) \doteq \mathbb{E}_{\pi} \left[ G_t \mid S_t = s, A_t = a \right]
$$

Value functions represent how good it is for the agent to be in a given state or take a particular action in a given state under a particular policy.

Value functions are crucial for reinforced learning because they allow the agent to query the quality of the current situations instead of waiting to observe the long-term outcome:

- The return is not immediately available

- The return can be random due to stochasticity in both the policy and environment dynamics

#### Video: Bellman Equation

##### State-value Bellman equation

$$
\begin{align*}
v_\pi(s) &\doteq \mathbb{E}_\pi[G_t \mid S_t = s] \\
         &= \mathbb{E}_\pi[R_{t+1} + \gamma G_{t+1} \mid S_t = s] \\
         &= \sum_a \pi(a|s) \sum_{s'} \sum_r p(s', r \mid s, a) \left[ r + \gamma \mathbb{E}[G_{t+1} \mid S_{t+1} = s'] \right] \\
         &= \sum_a \pi(a|s) \sum_{s'} \sum_r p(s', r \mid s, a) \left[ r + \gamma v_\pi(s') \right]
\end{align*}
$$

##### Action-value Bellman equation

$$
\begin{align*}
q_\pi(s, a) &\doteq \mathbb{E}_\pi[G_t \mid S_t = s, A_t = a] \\
&= \sum_{s'} \sum_{r} p(s', r \mid s, a) \left[ r + \gamma \mathbb{E}_\pi[G_{t+1} \mid S_{t+1} = s'] \right] \\
&= \sum_{s'} \sum_{r} p(s', r \mid s, a) \left[ r + \gamma \sum_{a'} \pi(a' \mid s') \mathbb{E}_\pi[G_{t+1} \mid S_{t+1} = s', A_{t+1} = a'] \right] \\
&= \sum_{s'} \sum_{r} p(s', r \mid s, a) \left[ r + \gamma \sum_{a'} \pi(a' \mid s') q_\pi(s', a') \right]
\end{align*}
$$

### Optimality (Optimal Policies & Value Functions)

#### Video: Optimal Policies

The role of policies in Reinforcement Learning (RL) is pivotal as they dictate the behavior of an agent within its environment.

- Action Selection: Policies determine how an agent selects actions in different states of the environment. 

- Learning Objective: Policies define the learning objective for the RL agent.

- Exploration vs. Exploitation: Policies balance exploration and exploitation

##### Bellman Optimality Equation

An optimal policy $\pi_∗$ is a policy that maximizes the expected cumulative reward over time. 

The Bellman optimality equation expresses the optimal value of a state (or state-action pair) in terms of the maximum expected immediate reward plus the discounted value of the successor states.

###### State-value Bellman optimality function $v_*(s)$

$$
v_*(s) = \max_a \sum_{s'} \sum_r p(s', r \mid s, a) \left[ r + \gamma v_*(s') \right]
$$

$v_*(s)$ represents the optimal value of state $s$ under the optimal policy

###### Action-value Bellman optimality function $q_*(s)$

$$
q_*(s, a) = \sum_{s'} \sum_{r} p(s', r \mid s, a) \left[ r + \gamma \max_{a'} q_*(s', a') \right]
$$

$q_*(s, a)$ represents the optimal value of taking action $a$ in state $s$ under the optimal policy.

##### Relationship

$v_*$ is equal to the maximum of the boxed term over all actions. $\pi_*$ is the argmax, which simply means the particular action which achieves this maximum.

$$
\pi_*(s) = \underset{a}{\operatorname{argmax}} \sum_{s'} \sum_r p(s',r|s,a)[r + \gamma v_*(s')]
$$

## Module 5

### Policy Evaluation (Prediction)

#### Video: Policy Evaluation vs. Control

![802a1bb6-a96a-4cdf-8695-6dd34b87cdfe](file:///D:/Disk/Computer/Pictures/Typedown/802a1bb6-a96a-4cdf-8695-6dd34b87cdfe.png)

* **Policy Evaluation**: Determines the value function of a given policy, assessing how good it is.

* **Policy Control**: Improves the policy to maximize future rewards, finding the optimal strategy.

* **Relative Value**: A policy is considered as good as or better than a policy if the value function under is greater than or equal to the value function under for every state. If there exists at least one state where has a strictly higher value, then is strictly better than .

#### Video: Iterative Policy Evaluation

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/6f612517-4a8f-4112-b8d4-7ba29a6468cf.png" alt="6f612517-4a8f-4112-b8d4-7ba29a6468cf" style="zoom:33%;" data-align="center">

The **dynamics of the environment** in reinforcement learning refer to how the agent interacts with the environment and how the environment responds. This is typically modeled as a **Markov Decision Process (MDP)** with the following components:

1. **States ($S$)**: The possible situations the agent can be in.

2. **Actions ($A$)**: The choices available to the agent in each state.

3. **Transition Probabilities ($𝑃(𝑠′∣𝑠,𝑎)$)**: The probability of moving to a new state given the current state and action .

4. **Reward Function ($R(s,a,s')$)**: The numerical feedback given to the agent when transitioning between states due to an action.

5. **Policy ($\pi(𝑎∣𝑠)$)**: The strategy the agent follows when choosing actions.

### Policy Iteration (Control)

We can find the optimal policy by choosing the Greedy action. The Greedy action maximizes the Bellman's optimality equation in each state. 

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/07025877-8be9-4474-b900-90bdaf27b332.png" alt="07025877-8be9-4474-b900-90bdaf27b332" style="zoom:50%;" data-align="center">

$$
\begin{aligned}
    q_{\pi'}(s, \pi'(s)) &\geq q_{\pi}(s, \pi(s)) && \text{for all } s \in \mathcal{S}
    &\boldsymbol{\rightarrow} \pi' \geq \pi  \\

    q_{\pi'}(s, \pi'(s)) &> q_{\pi}(s, \pi(s)) && \text{for at least one } s \in \mathcal{S} 
    &\boldsymbol{\rightarrow} \pi' > \pi
\end{aligned}

$$

Suppose you have two policies and their value functions for all states:

* If $v_{π_2}(s)≥v_{π_1}(s)$ for every $s$, $π_2$ is at least as good as $π_1$.

* If for some state $s∗$, $v_{π_2}(s*)>v_{π_1}(s*)$, then $π_2$ is **strictly** better.

##### Policy Iteration

Policy iteration consists of two distinct steps: evaluation and improvement. 

1. **Evaluation Step**: We first evaluate our current policy $\pi_1$, which gives us a new value function $v_{\pi_1}$ that accurately reflects the value of $\pi_1$. 

2. **Improvement Step**: The improvement step then uses $v_{\pi_1}$ to produce a greedy policy $\pi_2$. At this point, $\pi_2$ is greedy with respect to the value function of $\pi_1$, but $v_{\pi_1}$ no longer accurately reflects the value of $\pi_2$, so we need to re-calculate again.
   
   

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/0c6ebbb3-7c3a-49fc-be37-5d1e54ccf497.png" alt="0c6ebbb3-7c3a-49fc-be37-5d1e54ccf497" data-align="center" style="zoom:67%;">

###### Policy Iteration pseudo code using iterative policy evaluation for estimate pi ~ pi*

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/dac15803-10d2-4744-bfb2-f0086a74d759.png" alt="dac15803-10d2-4744-bfb2-f0086a74d759" data-align="center" style="zoom:50%;">

### Generalized Policy Iteration

#### Value Iteration

Value Iteration for estimating p~p*

<img title="" src="file:///D:/Disk/Computer/Pictures/Typedown/2c77e425-8795-4a5e-8e69-812065a7fb0d.png" alt="2c77e425-8795-4a5e-8e69-812065a7fb0d" style="zoom:50%;" data-align="center">


