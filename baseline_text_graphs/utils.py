import zipfile
from typing import List

import gdown
import torch


def download_and_unzip_file(download_url, output_dir):
    # Download the file
    output_zip_path = output_dir / "downloaded_file.zip"
    gdown.download(download_url, str(output_zip_path), quiet=False)

    # Unzip the file
    with zipfile.ZipFile(output_zip_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)

    # Remove the downloaded zip file
    output_zip_path.unlink()

    print(f"File downloaded and extracted to {output_dir}")


def ids_to_mask(ids: List[int], total_size: int) -> torch.Tensor:
    return torch.tensor([1 if i in ids else 0 for i in range(total_size)]).reshape(-1)
