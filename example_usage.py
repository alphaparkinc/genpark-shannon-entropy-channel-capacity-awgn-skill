from client import ShannonChannelAnalyzer

cap = ShannonChannelAnalyzer.shannon_hartley_capacity(bandwidth_hz=10000, snr_linear=31.0)
print(f"AWGN Shannon-Hartley Capacity (B=10kHz, SNR=31): {cap:.2f} bps")

bsc = ShannonChannelAnalyzer.bsc_capacity(error_prob=0.05)
print(f"Binary Symmetric Channel Capacity (p=0.05): {bsc:.4f} bits/channel use")
