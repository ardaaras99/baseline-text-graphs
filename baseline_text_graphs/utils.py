import zipfile

import gdown


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
