import math
import torch
import torch.nn as nn

class CAMFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)
        avg_pool = nn.AdaptiveAvgPool2d(1)
        max_pool = nn.AdaptiveMaxPool2d(1)
        fc1 = nn.Conv2d(input.shape[1], input.shape[1] // 16, kernel_size=1, padding=0)
        relu = nn.ReLU(inplace=True)
        fc2 = nn.Conv2d(input.shape[1] // 16, input.shape[1], kernel_size=1, padding=0)
        sigmoid_channel = nn.Sigmoid()

        avg = avg_pool(input)
        mx = max_pool(input)
        avg = fc1(avg)
        mx = fc1(mx)
        avg = relu(avg)
        mx = relu(mx)
        avg = fc2(avg)
        mx = fc2(mx)
        x = avg + mx
        x = sigmoid_channel(x)
        x = input * x

        return x

    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        # Gradient computation not required for CAM, return None
        return None

class CAM(nn.Module):
    def __init__(self, channels, reduction):
        super(CAM, self).__init__()
        self.ch=channels

    def forward(self, x):
        # Channel attention module
        module_input = x
        x = CAMFunction.apply(x)
        return x
