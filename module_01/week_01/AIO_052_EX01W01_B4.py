#Bài 4:
import math

def factorial(x):
    if x == 1 & x == 0:
        return 1
    else:
        return x*factorial(x-1)

def approx_sin(x, n):
    if n <= 0:
        print("n should be larger than Zero")
        return None
    else:
        result = 0
        for idx in range(n):
            term = math.pow(-1, idx) * math.pow(x, 2*idx + 1) * 1/ factorial(2*idx + 1)
            result += term
        print(result)
        return result

def approx_cos(x, n):
    if n <= 0:
        print("n should be larger than Zero")
        return None
    else:
        result = 0
        x_radian = math.radians(x)   
        for idx in range(n):
            term = math.pow(-1, idx) * math.pow(x_radian, 2*idx) * 1/ factorial(2*idx + 1)
            result += term
        print(result)
        return result 

def approx_sinh(x, n):
    if n <= 0:
        print("n should be larger than Zero")
        return None
    else:
        result = 0
        for idx in range(n):
            term = math.pow(x, 2*idx + 1) * 1/ factorial(2*idx + 1)
            result += term
        print(result)
        return result
    
def approx_cosh(x, n):
    if n <= 0:
        print("n should be larger than Zero")
        return None
    else:
        result = 0
        for idx in range(n):
            term = math.pow(x, 2*idx) * 1/ factorial(2*idx)
            result += term
        print(result)
        return result


if __name__ == "__main__":
    print(approx_sin(x=3.14, n=5))
    print(approx_cos(x=3.14, n=5))
    print(approx_sinh(x=3.14, n=5))
    print(approx_cosh(x=3.14, n=5))
    