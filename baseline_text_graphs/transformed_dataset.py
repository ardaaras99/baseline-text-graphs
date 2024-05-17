from typing import List

import torch

from baseline_text_graphs.raw_dataset import RawDataset


class LabelEncoder:
    label_to_int = {}

    def __init__(self, raw_labels):
        self.raw_labels = raw_labels
        self.y = self._create_label_mapping()

    def _create_label_mapping(self):
        sorted_labels = sorted(set(self.raw_labels))
        LabelEncoder.label_to_int = {label: i for i, label in enumerate(sorted_labels)}
        return [LabelEncoder.label_to_int[label] for label in self.raw_labels]


class TransformedDataset:
    def __init__(self, dataset_name: str) -> None:
        self.raw_dataset = RawDataset(dataset_name)
        self.docs = self.raw_dataset.docs
        self.n_class = self.raw_dataset.n_class

        self.transform()

    def transform(self):
        train_ids = self.raw_dataset.train_ids
        test_ids = self.raw_dataset.test_ids

        train_mask = ids_to_mask(train_ids, len(self.docs))
        test_mask = ids_to_mask(test_ids, len(self.docs))

        self.train_mask = train_mask
        self.test_mask = test_mask

        self.label_encoder = LabelEncoder(self.raw_dataset.raw_labels)
        self.y = torch.tensor(self.label_encoder.y).reshape(-1, 1)


def ids_to_mask(ids: List[int], total_size: int) -> torch.Tensor:
    return torch.tensor([1 if i in ids else 0 for i in range(total_size)]).reshape(-1)
