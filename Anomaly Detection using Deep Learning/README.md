
# Network Traffic Anomaly Detection using Deep Learning

---

## 1. Overview & Objectives
The primary goal of this project is to detect malicious network activity (anomalies) by analyzing the sequence of communication ports used between systems. 

The core idea is to treat **network traffic as a sequence-based language**, where port numbers are "words" and a series of connections forms a "sentence." By learning the "grammar" of normal traffic, the model can identify "unnatural" sequences that indicate a cyber-attack.

### Key Objectives:
*   Parse complex XML-based network flow data.
*   Convert raw network logs into mathematical sequences.
*   Design a **Bidirectional LSTM** (Long Short-Term Memory) network using PyTorch.
*   Train the model to predict the next port in a sequence.
*   Use prediction errors to flag anomalies.

---

## 2. Dataset: ISCXIDS2012
The notebook utilizes the **ISCXIDS2012** dataset from the Canadian Institute for Cybersecurity. 
*   **Content**: Captures real network traffic flows.
*   **Labels**: Includes "Normal" behavior and various attack types (DDoS, Brute Force, etc.).
*   **Challenges**: The data is in large XML files and often contains malformed characters, requiring robust parsing techniques.

---

## 3. Data Engineering Pipeline

### Robust XML Parsing
Because real-world network data is often messy, the notebook uses the `lxml` library with `recover=True`. This ensures that if the XML contains illegal characters or malformed tokens, the parser can skip them without crashing the entire pipeline.

### Feature Engineering
1.  **IP Communication Pairs**: Traffic is grouped by a unique key: `Source_IP + Destination_IP + Hour`. This isolates the "conversation" between specific devices.
2.  **Port Standardization**:
    *   It identifies the "service port" by taking the lower of the source and destination ports.
    *   Ports above 10,000 are clamped to a single value ("10000") to reduce vocabulary size while keeping essential service information.
3.  **Label Encoding**: Port numbers (e.g., 80, 443, 22) are converted into unique integer indices for the neural network.

---

## 4. Model Architecture: Bidirectional LSTM
The model is built using PyTorch and consists of four main stages:

1.  **Embedding Layer**: Converts the integer port IDs into dense vectors (100-dimensional). This allows the model to learn relationships between ports (e.g., that ports 80 and 443 are both related to web traffic).
2.  **First Bi-LSTM**: Processes the 10-port sequence in both forward and backward directions.
3.  **Second Bi-LSTM**: A deeper layer that extracts high-level features from the sequence.
4.  **Fully Connected Layers**: Projects the LSTM output back into the "port space" to predict the probability of the next port.

> [!NOTE]
> **Why Bidirectional?** 
> Standard RNNs only look at past events. In network security, the entire context of a session is important. A Bi-LSTM captures patterns from both "what happened before" and "what happened after" to better understand the flow.

---

## 5. The Anomaly Detection Logic
Anomaly detection in this notebook is based on **statistical surprise**. 

### How the detection works:
1.  **Sliding Window**: The model takes the last 10 ports $P_1, P_2, \dots, P_{10}$.
2.  **Prediction**: It calculates the probability of the 11th port $P_{11}$.
3.  **Scoring**:
    *   If the actual port $P_{11}$ has a **high probability** (e.g., > 0.8), the traffic is **Normal**.
    *   If the actual port $P_{11}$ has a **very low probability** (the model is "surprised"), it is flagged as an **Anomaly**.

### Attack Scenarios:
| Attack Type | Why the model flags it |
| :--- | :--- |
| **Port Scanning** | A sequence of ports like `21 -> 22 -> 23 -> 25` is highly unusual for a normal machine, causing high prediction error. |
| **DDoS** | A sudden flood of identical or erratic port requests breaks the learned "rhythm" of the IP pair's traffic. |
| **Exfiltration** | Moving data over non-standard ports (e.g., DNS port 53 for bulk transfer) creates a sequence that the model hasn't seen before. |

---

## 6. Conclusion
By leveraging Natural Language Processing techniques for Cybersecurity, this model can detect "Zero-Day" attacks—threats it hasn't specifically been programmed to recognize—simply because they do not "look like" normal network behavior.

### Critical Takeaways:
1.  **Context Matters**: Sequential patterns are more informative than individual packets.
2.  **Unsupervised Potential**: While trained on data, the model's ability to flag "low probability" events makes it an effective tool for discovering unknown threats.
3.  **Robustness**: Handling malformed data at the parsing stage is just as important as the neural network design itself.
