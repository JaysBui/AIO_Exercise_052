# Bài 3:
import random
import math


def mae_function(lst):
    result = sum(lst) / len(lst)
    return result


def mse_function(lst):
    lst = [math.sqrt(x) for x in lst]
    result = sum(lst) / len(lst)
    return result


def rmse_function(lst):
    result = math.sqrt(
        mse_function(lst)
    )
    return result


def reg_loss_function(nbr_samples, func_name):
    print(
        f"Input number off samples (integer number) which are generated: {nbr_samples}")
    print(f"Input loss name: {func_name}")
    if not str(nbr_samples).isnumeric():
        print("Number of samples must be an Integer")
        return None
    else:
        lst = []
        nbr_samples = int(nbr_samples)
        for idx in range(nbr_samples):
            tg_val = random.uniform(0, 10)
            prd_val = random.uniform(0, 10)
            loss = abs(prd_val - tg_val)
            lst.append(loss)
            print(
                f"Loss name: {func_name}, sample: {idx}, predict: {prd_val}, target: {tg_val}, loss: {loss}")
    if func_name == "MAE":
        print(f"Final MAE: {mae_function(lst)}")
        return mae_function(lst)
    elif func_name == "MSE":
        print(f"Final MSE: {mse_function(lst)}")
        return mse_function(lst)
    elif func_name == "RMSE":
        print(f"Final RMSE: {rmse_function(lst)}")
        return rmse_function(lst)
    else:
        print("Unknown loss function name")
        return None


if __name__ == "__main__":
<< << << < HEAD
reg_loss_function(nbr_samples=input("Input number: "),
                  func_name=input("Input loss function: "))
== == == =
reg_loss_function(nbr_samples=input("Input number: "),
                  func_name=input("Input loss function: "))
>>>>>> > 20b6b2fd7f0e4f1c79d6d5425caf097828dd9101
