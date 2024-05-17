from pathlib import Path

# from baseline_text_graphs.raw_dataset import RawDataset
# from baseline_text_graphs.transformed_dataset import TransformedDataset

PROJECT_PATH = Path.cwd()
print("Project path: ", PROJECT_PATH)

DATA_PATH = PROJECT_PATH.joinpath("data")
DATA_PATH.mkdir(parents=True, exist_ok=True)
print("Data path: ", DATA_PATH)

# TRANSFORMED_DATA_PATH = PROJECT_PATH.joinpath("data/transformed-data")
# TRANSFORMED_DATA_PATH.mkdir(parents=True, exist_ok=True)

FILE_ID = "19jy8pu4GVUKq7FvrscmitmTUZl3eI1Wa"
DOWNLOAD_LINK = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

__all__ = ["TransformedDataset", "RawDataset"]
