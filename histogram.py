import math
from inspect import signature
#import numpy as np


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

    ncol_x = len(x)
    result = []        #vector to store the result
    # Excludes element x(i) if the index is out of range (1 <= index <= ncell)
    for i in range(ncol_x):
        x0 = x[i]      #one particular point in window x
        # Calculates the index of the histogram cells
        bin_idx = round((x0 - descriptor.lower()) / (descriptor.upper - descriptor.lower) * ncell + 0.25)
        if (bin_idx >= 1) & (bin_idx <= ncell):
            result[bin_idx] = result[bin_idx] + 1

    # return descriptors & row vector containing the histogram
    return result, descriptor


def entropy(x):
    """Function that estimates the entropy of a stationary signal with independent samples"""

    result, descriptor = histogram(x)

#     # Tests to ensure the input arguments are right
#     sig = signature(entropy)
#     if len(sig.parameters) > 2:
#         raise Exception("Too many input arguments")
#
#     if not isinstance(descriptor, Descriptor):
#         raise TypeError("The descriptor is not of class Descriptor")
#
#     lower_bound = descriptor.lower()
#     upper_bound = descriptor.upper()
#     ncell = descriptor.ncell()
#
#     # initialising the return values
#     estimate = 0
#     sigma = 0
#     count = 0
#
#     for j in range(ncell):
#       if result(j)
#
#     # base transformation
#     estimate = estimate / math.log(base)
#     # n_bias = n_bias/math.log(base)         only if the approach is biased
#     sigma = sigma / math.log(base)
#
#
#############       MAIN        #############
# Retrieves the traces from the files
files = ["010403ba_0007_1.asc", "010403ba_0007_2.asc", "010403ba_0007_3.asc",
         "010403ba_0007_4.asc", "010403ba_0007_5.asc", "010403ba_0007_6.asc"]
trace = []
sampling_rate = 256
file_count = 0
# Store the traces and time vectors in cell arrays
for f in files:
    file_count = file_count + 1
    trace.append(open(f, "r"))        #want this to load the raw data
    #t[file_count] = np.divide(range(1,(trace[file_count]))), sampling_rate)     #the time vector (in seconds)

# for f in files:
#     file_count = file_count + 1
#     trace[file_count] = open(f, "r")        #want this to load the raw data
#     #t[file_count] = numpy.divide(range(1,(trace[file_count]))), sampling_rate)     #the time vector (in seconds)

# for count, f in enumerate(files):
#     trace[count] = open(f, "r")
#     t[count] = numpy.divide((1:len(trace[count])), sampling_rate)


