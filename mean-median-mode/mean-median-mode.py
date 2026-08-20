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
    print(Counter(M).most_common(1)[0][0])
    mode = float(Counter(M).most_common(1)[0][0])

    return (mean, median, mode)
    pass