import torch.nn as nn


class OutreachNeuralNetwork(nn.Module):
    def __init__(self, input_size, num_classes=4):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )

    def forward(self, x):
        return self.network(x)