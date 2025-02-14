# Financial Dataset Loader

A Python module for efficiently loading financial datasets from various sources including AWS S3.

## Features

- Load financial datasets from AWS S3
- Flexible data source configuration
- Path management and organization
- File name formatting utilities

## Installation

```bash
pip install financial-dataset-loader
```

## Usage

```python
from financial_dataset_loader import dataset_loader_s3, data_source

# Configure your data source
source = data_source.DataSource(
    bucket_name="your-bucket",
    base_path="your/base/path"
)

# Create a loader
loader = dataset_loader_s3.DatasetLoaderS3(source)

# Load your dataset
dataset = loader.load_dataset("your_dataset_name")
```

## Requirements

- Python >= 3.11
- aws-s3-controller

## License

MIT License

## Author

June Young Park (juneyoungpaak@gmail.com)
