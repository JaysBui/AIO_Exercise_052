import torch
import torch.nn as nn
import torch.nn.functional as F
from abc import ABC, abstractmethod


class MyActivationFunction(ABC, nn.Module):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def forward(self, data):
        pass


class Softmax(MyActivationFunction):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        return F.softmax(data, dim=-1)


class Softmaxstable(MyActivationFunction):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        max_data = torch.max(data, dim=-1, keepdim=True).values
        exp_data = torch.exp(data - max_data)
        result = exp_data / torch.sum(exp_data, dim=-1, keepdim=True)
        return result


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    result = softmax(data)
    print(result)
    print("\n")
    data = torch.Tensor([1, 2, 3])
    softmaxstable = Softmaxstable()
    result = softmaxstable(data)
    print(result)
