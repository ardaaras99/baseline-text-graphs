# Baseline Text Graphs

![Build Status](https://img.shields.io/github/actions/workflow/status/ardaaras99/baseline-text-graphs/ci.yml?branch=main)
![License](https://img.shields.io/github/license/ardaaras99/baseline-text-graphs)

Baseline Text Graphs is a Python package designed to download, read, and transform raw data for text graph analysis. It provides utilities for handling raw datasets and transforming them into formats suitable for further analysis and modeling.

## Features

- **RawDataset**: Download and read raw data from various sources.
- **TransformedDataset**: Transform raw data into formats suitable for analysis.

## Installation

You can install the package via GitHub:

```bash
poetry add git+https://github.com/ardaaras99/baseline-text-graphs.git@main
```

**OR**

```bash
pip install git+https://github.com/ardaaras99/baseline-text-graphs.git@main

```

## Usage

```python
from baseline_text_graphs.transformed_dataset import TransformedDataset

# Initialize the TransformedDataset with raw data
transformed_dataset = TransformedDataset(dataset_name = "mr")

# Transform the data
transformed_data = transformed_dataset.transform()
print(transformed_data)

## Supported Datasets
options = ["mr","20ng", "R8", "R52", "Ohsumed"]

```
