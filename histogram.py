import math
from inspect import signature
import numpy as np


class Descriptor():
    """Class to provide a descriptor for the histogram function"""

    def __init__(self, lower, upper, ncell):
        """Constructor for a descriptor class, including lower/upper bounds, and number of cells"""
        self.lower = lower
        self.upper = upper
        self.ncell = ncell

    def __repr__(self):
        return "Descriptor (lower bound: {}, upper bound: {}, no. cells: {})".format\
            (self.lower, self.upper, self.ncell)


# Reference: http://www.cs.rug.nl/~rudy/matlab/doc/histogram.html
def histogram(x):
    """Function to estimate a histogram of a signals and descriptor by taking in a vector of values"""

    # makes sure the input arguments are correct
    sig = signature(histogram)
    if len(sig.parameters) != 1:
        raise TypeError("You have inputted the wrong number of arguments")

    # Computes the lower/upper bounds and the number of cells of descriptor
    minx = int(min(x))
    maxx = int(max(x))
    delta = (maxx - minx) / (len(x) - 1)
    ncell = math.ceil(math.sqrt(len(x)))
    descriptor = Descriptor(minx - delta / 2, maxx + delta / 2, ncell)

    # Error catching to safely assume ncell >= 1 and lower bound > upper bound
    if ncell < 1:
        raise Exception("Number of cells should be at least 1")

    if descriptor.upper <= descriptor.lower:
        raise Exception("Invalid bounds")

    # Excludes element x(i) if the index is out of range (1 <= index <= ncell)
    ncol_x = len(x)
    result = []  # vector to store the result
    for i in range(ncol_x):
        x0 = x[i]  # one particular point in window x
        # Calculates the index of the histogram cells
        bin_idx = round((int(x0) - descriptor.lower) / (descriptor.upper - descriptor.lower) * descriptor.ncell + 0.5)
        if (bin_idx >= 1) & (bin_idx <= ncell):
            result.append(bin_idx)

    # return descriptors & row vector containing the histogram
    return result, descriptor


# The function below does not work and is thus commented out
# Reference: http://www.cs.rug.nl/~rudy/matlab/doc/entropy.html
# def entropy(x):
#     """Function that estimates the entropy of a stationary signal with independent samples"""
#
#     result, descriptor = histogram(x)
#
#     # Tests to ensure the input arguments are right
#
#     lower = descriptor.lower  # Lower and upper bounds
#     upper = descriptor.upper
#     ncell = descriptor.ncell
#
#     # initialising the return values
#     estimate = 0    # The entropy estimate
#     sigma = 0   # The standard error of the estimate
#     count = 0
#
#     # Produce estimate for entropy with an unbiased approach and use of logarithm base e
#     for j in range(0, len(ncell)):
#         if result[j] != 0:
#             log_f = math.log(result[j])
#         else:
#             log_f = 0
#       count = count + result[j]
#       estimate = estimate - result[j] * log_f   # Updates the estimate for each bin
#       sigma = sigma + result[j] * log_f^2
#
#     # Generates biased estimate
#     estimate = estimate / count
#     sigma = math.sqrt( (sigma/count-estimate^2) / (count-1))
#     estimate = estimate + math.log(count) + math.log((upper-lower)/ncell)
#     n_bias = -(ncell-1) / (2 * count)
#
#     # Conversion to unbiased estimate
#     estimate = estimate - n_bias
#     n_bias = 0
#
#     # base transformation
#     base = math.exp(1)
#     estimate = estimate / math.log(base)    # Estimate for the entropy
#     sigma = sigma / math.log(base)        # Standard error of the estimate
#
#     return estimate, sigma, descriptor


# Retrieves the traces from the files
files = ["010403ba_0007_1.asc", "010403ba_0007_2.asc", "010403ba_0007_3.asc",
         "010403ba_0007_4.asc", "010403ba_0007_5.asc", "010403ba_0007_6.asc"]
trace = []  # empty list to store the 6 full traces
sampling_rate = 256  # In Hz
file_count = -1
t = []  # empty list to store time vector in s

# Store the traces and time vectors in cell arrays
for f in files:
    file = open(f, "r")  # want this to load the raw data
    lines = file.readlines()
    inner_array = []
    for line in lines:
        inner_array.append(line.strip())
    trace.append(inner_array)
    file.close()
    t.append(np.divide(range(0, len(trace[file_count])), sampling_rate))  # the time vector (in seconds)

print(histogram(trace[0]))


