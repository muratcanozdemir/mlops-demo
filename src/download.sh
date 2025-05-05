#!/bin/bash
mkdir -p data/raw && \
mkdir -p data/processed && \
mkdir -p data/model_ready
cd data &&
curl -L -o raw/student-depression-dataset.zip\
  https://www.kaggle.com/api/v1/datasets/download/adilshamim8/student-depression-dataset
unzip raw/student-depression-dataset.zip -d raw
cd ..