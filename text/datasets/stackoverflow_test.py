import torch

from text.datasets.stackoverflow_dataset import StackOverflowDataset
from text.datasets.text_dataset import collate_fn

train_dataset = StackOverflowDataset('./data/stackoverflow', partition='train', download=True)

cuda = False
kwargs = {'num_workers': 1, 'pin_memory': True}

train_loader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=256,
    shuffle=True,
    collate_fn=collate_fn,
    **kwargs)