#!/bin/bash
set -euo pipefail

# Create necessary directories
mkdir -p data/raw data/processed data/model_ready

# Download and extract the dataset
cd data
curl -L -o raw/student-depression-dataset.zip \
  https://www.kaggle.com/api/v1/datasets/download/adilshamim8/student-depression-dataset
unzip -o raw/student-depression-dataset.zip -d raw

cd ..
ls -la