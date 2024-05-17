from pathlib import Path
from typing import List, Tuple

from baseline_text_graphs import DATA_PATH, DOWNLOAD_LINK, VALID_DATASETS
from baseline_text_graphs.utils import download_and_unzip_file


class RawDataset:
    """
    A class to represent a raw dataset.

    Attributes:
    ----------
    dataset_name : str
        Name of the dataset.
    docs : List[str]
        List of documents in the dataset.
    raw_labels : List[str]
        List of raw labels corresponding to the documents.
    train_ids : List[int]
        List of indices for training samples.
    test_ids : List[int]
        List of indices for test samples.
    """

    def __init__(self, dataset_name: str) -> None:
        """
        Initializes the RawDataset class with the given dataset name.

        Parameters:
        ----------
        dataset_name : str
            Name of the dataset.

        Raises:
        ------
        ValueError
            If the dataset name is not valid.
        """
        if dataset_name not in VALID_DATASETS:
            raise ValueError(
                f"Invalid dataset name. Choose from {list(VALID_DATASETS.keys())}"
            )

        self.dataset_name = dataset_name

        if not DATA_PATH.joinpath("raw-data").exists():
            download_and_unzip_file(DOWNLOAD_LINK, DATA_PATH)
        else:
            print("Data already exists")

        self.read_data()

    def read_data(self) -> None:
        """
        Reads the data for the dataset, including labels and documents.
        """
        self.raw_labels: List[str] = []
        self.train_ids: List[int] = []
        self.test_ids: List[int] = []
        self.docs: List[str] = []

        label_info_path: Path = DATA_PATH.joinpath(
            f"raw-data/label-info/{self.dataset_name}.txt"
        )
        corpus_path: Path = DATA_PATH.joinpath(
            f"raw-data/corpus/clean/{self.dataset_name}.txt"
        )

        self._read_labels(label_info_path)
        self._read_corpus(corpus_path)

    def _read_labels(self, label_info_path: Path) -> None:
        """
        Reads the label information from the specified file.

        Parameters:
        ----------
        label_info_path : Path
            Path to the label information file.
        """
        try:
            with open(label_info_path) as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    parts = line.strip().split("\t")
                    self.raw_labels.append(parts[2])
                    if "test" in parts[1]:
                        self.test_ids.append(i)
                    elif "train" in parts[1]:
                        self.train_ids.append(i)
        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Label information file not found: {label_info_path}"
            ) from e
        except Exception as e:
            raise Exception(
                f"An error occurred while reading the label information file: {e}"
            ) from None

    def _read_corpus(self, corpus_path: Path) -> None:
        """
        Reads the corpus from the specified file.

        Parameters:
        ----------
        corpus_path : Path
            Path to the corpus file.
        """
        try:
            with open(corpus_path) as file:
                lines = file.readlines()
                for line in lines:
                    self.docs.append(line.strip())
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Corpus file not found: {corpus_path}") from e
        except Exception as e:
            raise Exception(
                f"An error occurred while reading the corpus file: {e}"
            ) from None

    def calculate_statistics(self) -> Tuple[int, int, int, int]:
        """
        Calculates and stores basic statistics about the dataset.
        """
        n_train: int = len(self.train_ids)
        n_test: int = len(self.test_ids)
        n_docs: int = len(self.docs)
        n_class: int = len(set(self.raw_labels))
        return n_train, n_test, n_docs, n_class

    def __repr__(self) -> str:
        """
        Returns a string representation of the RawDataset object.

        Returns:
        -------
        str
            String representation of the RawDataset object.
        """
        n_train, n_test, n_docs, n_class = self.calculate_statistics()
        return (
            f"RawDataset class for {self.dataset_name.upper()} dataset with {len(self.docs)} documents\n"
            f"Statistics:\n"
            f"Number of training samples: {n_train}\n"
            f"Number of test samples: {n_test}\n"
            f"Number of total samples: {n_docs}\n"
            f"Number of unique labels: {n_class}\n"
        )
