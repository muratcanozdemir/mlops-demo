#!/usr/bin/env nextflow

process TrainModel {
    input:
    path model_input from 'data/model_ready/student_depression_dataset_model_ready.csv'
    path train_script from 'src/train.py'

    output:
    path 'outputs/predictions.csv'
    path 'outputs/model.pkl'
    path 'outputs/metrics.json'

    script:
    """
    ls -R .
    pwd
    pip install scikit-learn joblib
    python train.py
    """
}

workflow {
    Channel.fromPath('data/model_ready/student_depression_dataset_model_ready.csv') | TrainModel
}
