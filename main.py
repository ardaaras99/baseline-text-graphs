from baseline_text_graphs import VALID_DATASETS
from baseline_text_graphs.raw_dataset import RawDataset

for dataset_name in VALID_DATASETS.keys():
    d = RawDataset(dataset_name)

d = RawDataset("mr2")
