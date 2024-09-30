import numpy as np


def make_array_from_list(some_list):
    np_array = np.array(some_list)
    return np_array


def make_array_from_number(num):
    np_array = np.array([num])
    return np_array


class NumpyBasics:
    def add_arrays(self, a, b):
        sum_array = np.add(a, b)
        return sum_array

    def add_array_number(self, a, num):
        sum_array = np.add(a, num)
        return sum_array

    def multiply_elementwise_arrays(self, a, b):
        multiply_array = np.multiply(a, b)
        return multiply_array

    def dot_product_arrays(self, a, b):
        dot_array = np.dot(a, b)
        return dot_array

    def dot_1d_array_2d_array(self, a, m):
        # consider the 2d array to be like a matrix
        dot_product = []
        for row in m:
            print(row)
            dot_product.append(np.dot(a, row))
        return dot_product