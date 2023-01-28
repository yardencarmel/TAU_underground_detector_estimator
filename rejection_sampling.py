from math import *
from random import *
# import sympy as sy


def my_formula(*args, formula):
    """
    :return: Returns formula evaluated at args
    :param args: Variable arguments to be evaluated by formula
    :param formula: Formula to evaluated variables
    """
    return formula(*args)


class RejectionSampling:
    def __init__(self):
        self.sample = 0

    def generate_number(self, dist_func, support_boundary):
        """
        Generate a number using a specified distribution function. A number x is more likely to be generated if the
        distribution function's value when x is applied is higher. I.e, P(0)>P(pi/2) for PDF of cos(x)^2
        :param dist_func: The distribution function as a lambda function of 1 variable
        :param support_boundary: The support boundaries of the distribution functon, mirrored around 0
        :return: A random number from the PDF represented by dist_func
        """
        self.sample = uniform(-support_boundary, support_boundary)
        sample_value = my_formula(self.sample, dist_func)
        accept_value = uniform(0, 1)
        while accept_value > sample_value:
            self.sample = uniform(-support_boundary, support_boundary)
            sample_value = cos(self.sample) ** 2
            accept_value = uniform(0, 1)
        return sample_value
