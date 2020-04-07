import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset

from catalyst import dl, utils


class Projector(nn.Module):
    """
    Simpler neural network example - Projector.
    """

    def __init__(self, input_size: int):
        """
        Init method.

        Args:
            input_size(int): number of features in projected space.
        """
        super().__init__()
        self.linear = nn.Linear(input_size, 1)

    def forward(self, X: torch.Tensor) -> torch.Tensor:
        """
        Forward method.

        Args:
            X(torch.Tensor): input tensor.

        Returns:
            (torch.Tensor): output projection.
        """
        return self.linear(X).squeeze(-1)


# example  7 - distibuted training  datasets preparation
# and utils.distributed_cmd_run
def train():
    """
    Training loop function.
    """
    X = torch.rand(int(1e4), 10)
    y = torch.rand(X.shape[0])
    model = Projector(X.shape[1])
    dataset = TensorDataset(X, y)
    # loader = DataLoader(dataset, batch_size=32, num_workers=1)

    runner = dl.SupervisedRunner()
    runner.train(
        model=model,
        # loaders={"train": loader, "valid": loader},
        datasets={
            "batch_size": 32,
            "num_workers": 1,
            "train": dataset,
            "valid": dataset,
        },
        criterion=nn.MSELoss(),
        optimizer=optim.Adam(model.parameters()),
        logdir="logs/log_example_08",
        num_epochs=10,
        verbose=True,
        check=True,
        fp16=False,
        distributed=False,
    )


utils.distributed_cmd_run(train)