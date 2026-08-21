import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    M = np.asarray(x)
    # Write code here
    mean = float(np.mean(M))
    median = float(np.median(M))
    count = Counter(x)
    mode = float(max(count, key=lambda k: (count[k],-k) ))

    return (mean, median, mode)
    