import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST


def get_dataset():
    batch_size = 256
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
    trainset = MNIST("data", train=True, download=True, transform=transform)
    trainloader = DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=4)

    testset = MNIST("data", train=False, download=True, transform=transform)
    testloader = DataLoader(testset, batch_size=batch_size * 2, shuffle=False, num_workers=0)

    return trainloader, testloader
