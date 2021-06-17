import torch
from torch import nn, optim
import cnn_model
import data
from ignite.engine import create_supervised_trainer, create_supervised_evaluator
from ignite.contrib.handlers import FastaiLRFinder, ProgressBar
from ignite.metrics import Accuracy, Loss

if __name__ == '__main__':
    trainloader, testloader = data.get_dataset()
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    # criterion = nn.NLLLoss()
    criterion = nn.CrossEntropyLoss()
    model = cnn_model.Cnn()
    model.to(device)
    optimizer = optim.SGD(model.parameters(), lr=3e-4, momentum=0.9)
    trainer = create_supervised_trainer(model, optimizer, criterion, device=device)
    ProgressBar(persist=True).attach(trainer, output_transform=lambda x: {"batch loss": x})
    lr_finder = FastaiLRFinder()
    to_save = {'model': model, 'optimizer': optimizer}
    with lr_finder.attach(trainer, to_save, diverge_th=1.5) as trainer_with_lr_finder:
        trainer_with_lr_finder.run(trainloader)
    trainer.run(trainloader, max_epochs=8)
    tester = create_supervised_evaluator(model=model,
                                         metrics={"acc": Accuracy(), 'Loss': Loss(criterion, device=device)})
    tester.run(testloader)

    print(tester.state.metrics)
