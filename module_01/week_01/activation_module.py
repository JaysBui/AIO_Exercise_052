# Bài 2
import math


def is_number(x):
    try:
        float(x)
    except ValueError:
        print("Input variable must be Integer or Float")
        return False
    return True


def sigmoid_function(x):
    sigmoid = 1 / (1 + math.exp(-x))
    return sigmoid


def relu_function(x):
    if x <= 0:
        relu = 0
    else:
        relu = x
    return relu


def elu_function(x, alpha=0.01):
    if x <= 0:
        elu = alpha*(math.exp(x) - 1)
    else:
        elu = x
    return elu


def activation_function(x, f):
    act_func = ["sigmoid", "relu", "elu"]
    print(f"Input x = {x}")
    if not is_number(x):
        return False
    x = float(x)
    print(f"Input function (sigmoid|relu|elu): {f}")
    if f not in act_func:
        print(f"{f} is not supported")
        return None
    else:
        if f == "sigmoid":
            result = sigmoid_function(x)
            print(f"Sigmoid: f({x}) = {result}")
            return result
        elif f == "relu":
            result = relu_function(x)
            print(f"RELU function: f({x}) = {result}")
            return result
        elif f == "elu":
            result = elu_function(x)
            print(f"ELU function: f({x}) = {result}")
            return result


if __name__ == "__main__":
<<<<<<< HEAD
    activation_function(x=input("Input value:"), f=input(
        "Input function (sigmoid|relu|elu):2"))
=======
    activation_function(x = input("Input value:"), f = input("Input function (sigmoid|relu|elu):2"))
>>>>>>> 20b6b2fd7f0e4f1c79d6d5425caf097828dd9101
