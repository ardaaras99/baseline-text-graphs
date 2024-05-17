from baseline_text_graphs import DATA_PATH, DOWNLOAD_LINK
from baseline_text_graphs.utils import download_and_unzip_file


class RawDataset:
    def __init__(self, dataset_name) -> None:
        self.dataset_name = dataset_name
        if DATA_PATH.joinpath("raw-data").exists():
            print("Data already exists")
        else:
            download_and_unzip_file(DOWNLOAD_LINK, DATA_PATH)
        self.read_data()
        self.calculate_statistics()

    def read_data(self) -> None:
        raw_labels, train_ids, test_ids = [], [], []
        docs = []

        label_info_path = DATA_PATH.joinpath(
            f"raw-data/label-info/{self.dataset_name}.txt"
        )
        corpus_path = DATA_PATH.joinpath(
            f"raw-data/corpus/clean/{self.dataset_name}.txt"
        )

        # Reading label info
        with open(label_info_path) as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                parts = line.strip().split("\t")
                raw_labels.append(parts[2])
                if "test" in parts[1]:
                    test_ids.append(i)
                elif "train" in parts[1]:
                    train_ids.append(i)

        # Reading corpus
        with open(corpus_path) as file:
            lines = file.readlines()
            for line in lines:
                docs.append(line.strip())

        self.docs = docs
        self.raw_labels = raw_labels
        self.train_ids = train_ids
        self.test_ids = test_ids

    def calculate_statistics(self) -> None:
        self.n_train = len(self.train_ids)
        self.n_test = len(self.test_ids)
        self.n_docs = len(self.docs)
        self.n_class = len(set(self.raw_labels))

    def __repr__(self) -> str:
        t = (
            f"RawDataset class for {self.dataset_name.upper()} dataset  with {len(self.docs)} documents \n"
            + "Statistics: \n"
            + f"Number of training samples: {self.n_train} \n"
            + f"Number of test samples: {self.n_test} \n"
            + f"Number of total samples: {self.n_docs} \n"
            + f"Number of unique labels: {self.n_class} \n"
        )
        return t
