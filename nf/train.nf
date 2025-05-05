#!/usr/bin/env nextflow

process TrainModel {
    input:
    path 'data/model_ready/student_depression_dataset_model_ready.csv'

    output:
    path 'outputs/predictions.csv'
    path 'outputs/model.pkl'
    path 'outputs/metrics.json'

    script:
    """
    pip install scikit-learn joblib
    python src/train.py
    """
}

workflow {
    Channel.fromPath('data/model_ready/student_depression_dataset_model_ready.csv') | TrainModel
}
