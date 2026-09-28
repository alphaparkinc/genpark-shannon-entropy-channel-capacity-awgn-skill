# genpark-shannon-entropy-channel-capacity-awgn-skill

Agent Skill implementing the **Shannon-Hartley Theorem and Channel Capacity Metrics** for AWGN channels, Binary Symmetric Channels (BSC), and Binary Erasure Channels (BEC).

## Architectural Overview
```mermaid
flowchart TD
    Bandwidth["Bandwidth B (Hz)"] & SNR["Signal-to-Noise Ratio (SNR)"] --> AWGN["C = B * log2(1 + SNR)"]
    P_error["Bit Transition Probability p"] --> BinaryEntropy["Binary Entropy H_2(p)"]
    BinaryEntropy --> BSC["C_BSC = 1 - H_2(p)"]
    P_erasure["Erasure Probability Epsilon"] --> BEC["C_BEC = 1 - Epsilon"]
```
