import numpy as np


def gradient_descent_with_vectorization():
    w = np.array([1.1, 2.0, 2.9])
    d = np.array([1, 0, -1])
    alpha = 0.1
    w = w-alpha*d
    return w


def gradient_descent_without_vectorization():
    w = np.array([1.1, 2.0, 2.9])
    d = np.array([1, 0, -1])
    alpha = 0.1
    for i in range(len(w)):
        w[i] -= alpha*d[i]
    return w


if __name__ == "__main__":
    print(gradient_descent_with_vectorization())  # [1. 2. 3.] efficient
    print(gradient_descent_without_vectorization())  # [1. 2. 3.]
