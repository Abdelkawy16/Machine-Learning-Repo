import numpy as np

def dot_product_with_vectorization():
    w = np.array([1, 2, 3])
    b = 4
    x = np.array([1, 2, 3])
    return np.dot(w, x) + b

def dot_product_without_vectorization():
    w = np.array([1, 2, 3])
    b = 4
    x = np.array([1, 2, 3])
    f = 0
    for i in range(len(w)):
        f += w[i] * x[i]
    return f + b

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
    
    print(dot_product_with_vectorization()) # 18 efficient
    print(dot_product_without_vectorization()) # 18

    print(gradient_descent_with_vectorization())  # [1. 2. 3.] efficient
    print(gradient_descent_without_vectorization())  # [1. 2. 3.]