"""Shannon Channel Capacity and Mutual Information Engine.
100% Python Standard Library.
"""

import math

class ShannonChannelAnalyzer:
    """Shannon entropy, mutual information, and theoretical channel capacity."""
    @staticmethod
    def shannon_hartley_capacity(bandwidth_hz, snr_linear):
        return bandwidth_hz * math.log2(1.0 + snr_linear)

    @staticmethod
    def binary_entropy(p):
        if p <= 0.0 or p >= 1.0:
            return 0.0
        return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)

    @classmethod
    def bsc_capacity(cls, error_prob):
        return 1.0 - cls.binary_entropy(error_prob)

    @staticmethod
    def bec_capacity(erasure_prob):
        return max(0.0, 1.0 - erasure_prob)

    @staticmethod
    def mutual_information(joint_prob_matrix):
        px = [sum(row) for row in joint_prob_matrix]
        py = [sum(joint_prob_matrix[r][c] for r in range(len(joint_prob_matrix))) for c in range(len(joint_prob_matrix[0]))]
        mi = 0.0
        for r, row in enumerate(joint_prob_matrix):
            for c, pxy in enumerate(row):
                if pxy > 1e-12:
                    mi += pxy * math.log2(pxy / (px[r] * py[c]))
        return mi
