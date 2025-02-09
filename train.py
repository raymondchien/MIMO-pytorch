from argparse import ArgumentParser

import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from mimo.config import Config
from mimo.model import MIMOModel
from mimo.trainer import MIMOTrainer

parser = ArgumentParser("MIMO Training")
parser.add_argument("--ensemble-num", type=int, default=3)


def main(args):
    # normal configuration stuff
    config = Config(ensemble_num=args.ensemble_num)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # set up the training data. in this case it is the MNIST dataset
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
    train_dataset = datasets.MNIST("../data", train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST("../data", train=False, transform=transform)
    # dataloaders are a datatype that helps accelerate the use of data
    train_dataloaders = [
        DataLoader(train_dataset, batch_size=config.batch_size, num_workers=config.num_workers, shuffle=True)
        for _ in range(config.ensemble_num)
    ]
    test_dataloader = DataLoader(test_dataset, batch_size=config.batch_size, num_workers=config.num_workers)
    # Create a MIMO model with config
    model = MIMOModel(ensemble_num=config.ensemble_num).to(device)
    trainer = MIMOTrainer(config, model, train_dataloaders, test_dataloader, device)
    trainer.train()


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
