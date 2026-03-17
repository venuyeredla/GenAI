import torch

class TensorPlayGround:
    def __init__(self, data):
        self.data = data
    
    def print_torch_info(self):
        print(torch.__version__)
        print(torch.cuda.is_available())