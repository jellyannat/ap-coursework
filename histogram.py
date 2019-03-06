import math
from inspect import signature
import numpy as np


class Descriptor():
    """Class to provide a descriptor for the histogram function"""

    def __init__(self, lower, upper, ncell):
        """Constructor for a descriptor class"""
        self.lower = lower
        self.upper = upper
        self.ncell = ncell


def histogram(x):
    """Function to estimate a histogram by taking in a vector of values and its descriptor"""

    # makes sure the input arguments are correct
    sig = signature(histogram)
    if len(sig.parameters) != 1:
        raise TypeError("You have inputted the wrong number of arguments")

    # Computes the upper/lower bounds and the number of cells
    minx = min(x)
    maxx = max(x)
    delta = (maxx - minx) / (len(x) - 1)
    ncell = math.ceil(math.sqrt(len(x)))
    descriptor = Descriptor(minx - delta / 2, maxx + delta / 2, ncell)

    # Error catching to safely assume ncell >= 1 and lower bound > upper bound
    if ncell < 1:
        raise Exception("Number of cells should be at least 1")

    if descriptor.upper() <= descriptor.lower():
        raise Exception("Invalid bounds")

    # Excludes element x(i) if the index is out of range (1 <= index <= ncell)
    ncol_x = len(x)
    result = []  # vector to store the result
    for i in range(ncol_x):
        x0 = x[i]  # one particular point in window x
        # Calculates the index of the histogram cells
        bin_idx = round((x0 - descriptor.lower()) / (descriptor.upper - descriptor.lower) * ncell + 0.25)
        if (bin_idx >= 1) & (bin_idx <= ncell):
            result[bin_idx] = result[bin_idx] + 1

    # return descriptors & row vector containing the histogram
    return result, descriptor


def entropy(x):
    """Function that estimates the entropy of a stationary signal with independent samples"""

    result, descriptor = histogram(x)

    # # Tests to ensure the input arguments are right
    # if not isinstance(descriptor, Descriptor):
    #     raise TypeError("The descriptor is not of class Descriptor")
    #
    # lower = descriptor.lower()  # Lower and upper bounds
    # upper = descriptor.upper()
    # ncell = descriptor.ncell()
    #
    # # initialising the return values
    # estimate = 0    # The entropy estimate
    # sigma = 0   # The standard error of the estimate
    # count = 0
    #
    # # Produce estimate for entropy with an unbiased approach and use of logarithm base e
    # for j in range(0, len(ncell)):
    #   if result[j] != 0:
    #     log_f = math.log(result[j])
    #   else:
    #     log_f = 0
    #   count = count + result[j]
    #   estimate = estimate - result[j] * log_f   # Updates the estimate for each bin
    #   sigma = sigma + result[j] * log_f^2
    #
    # # Generates biased estimate
    # estimate = estimate / count
    # sigma = math.sqrt( (sigma/count-estimate^2) / (count-1))
    # estimate = estimate + math.log(count) + math.log((upper-lower)/ncell)
    # n_bias = -(ncell-1) / (2 * count)
    #
    # # Conversion to unbiased estimate
    # estimate = estimate - n_bias
    # n_bias = 0
    #
    # # base transformation
    # base = math.exp(1)
    # estimate = estimate / math.log(base)    # Estimate for the entropy
    # sigma = sigma / math.log(base)        # Standard error of the estimate
    #
    # return estimate, sigma, descriptor


def main():
    # Retrieves the traces from the files
    files = ["010403ba_0007_1.asc", "010403ba_0007_2.asc", "010403ba_0007_3.asc",
         "010403ba_0007_4.asc", "010403ba_0007_5.asc", "010403ba_0007_6.asc"]
    trace = []
    sampling_rate = 256
    file_count = -1
    t = []

# Store the traces and time vectors in cell arrays
    for f in files:
        file_count = file_count + 1
        data = (open(f, "r"))  # want this to load the raw data
        trace = np.append(trace, data.read())
        t.append(np.divide(range(1, len(trace[file_count])), sampling_rate))  # the time vector (in seconds)

# Calculate entropy over sliding window (non-overlapping)
    win_seconds = 0.5  # window size of one second
    window_size = sampling_rate * win_seconds   # convert window from seconds to samples
    ent = []
    for i in trace:
        for j in range(1, len(i), int(window_size)):
            ent.append(entropy(i[j:j + window_size]))

