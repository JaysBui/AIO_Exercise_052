# Bài 5
import math


def md_nre_function(y, y_hat, n, p):
    y = math.pow(y, 1/n)
    y_hat = math.pow(y_hat, 1/n)
    difference = y - y_hat
    loss = math.pow(difference, p)
    print(loss)
    return loss


if __name__ == "__main__":
    md_nre_function(y=100, y_hat=99.5, n=2, p=1)
    md_nre_function(y=50, y_hat=49.5, n=2, p=1)
    md_nre_function(y=20, y_hat=19.5, n=2, p=1)
    md_nre_function(y=0.6, y_hat=0.1, n=2, p=1)
