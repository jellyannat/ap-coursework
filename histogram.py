import math
from inspect import signature


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

    # Excludes element x(i) if the index is out of range            NEEDS WORK
    # ncol_x = len(x)
    # result = [None] * len(ncell)
    # w = round((x-descriptor.lower()) / (descriptor.upper-descriptor.lower) * ncell + 0.25)
    # for i in ncol_x:
    #     index = w(i)
    #     if (index >= 1) & (index <= ncell):
    #         result(index) = result(index) + 1

    # return descriptors & row vector containing the histogram


def entropy(x, descriptor, approach, base):
    """Function that estimates the entropy of a stationary signal with independent samples"""

    sig = signature(entropy)
    if len(sig.parameters) > 4:
        raise Exception("Too many input arguments")

    # sort out how many input arguments your function is going to take (will it take approach & base types?)

    if not isinstance(descriptor, Descriptor):
        raise TypeError("The descriptor is not of class Descriptor")

    lower_bound = descriptor.lower()
    upper_bound = descriptor.upper()
    ncell = descriptor.ncell()

    # initialising the return values
    estimate = 0
    sigma = 0
    count = 0

    #add options for different approaches and biases

    # calculate entropy equation

    # base transformation
    estimate = estimate / math.log(base)
    # n_bias = n_bias/math.log(base)         only if the approach is biased
    sigma = sigma / math.log(base)
