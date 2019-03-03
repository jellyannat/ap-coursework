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

    # make sure the input arguments are correct
    # dims = [nrowx, ncolx]
    # dims[nrowx, ncolx] = x.shape

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

    # Excludes element x(i) if the index is out of range
    #result(1:ncell) = 0
    w = round((x-descriptor.lower()) / (descriptor.upper-descriptor.lower) * ncell + 0.25)
    for i in len(x):
        index = w(i)
        if (index >= 1) & (index <= ncell):
            result(index) = result(index) + 1


    # return descriptors & row vector containing the histogram
## MAKE A FUNCTION THAT CALCULATES THE ENTROPY USING THE HISTOGRAM


