#!/usr/bin/env nextflow
nextflow.enable.dsl=2

process TrainModel {
    input:
    path model_input
    path train_script

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
    Channel.fromPath('data/model_ready/student_depression_dataset_model_ready.csv')
        .set { model_input }

    Channel.fromPath('src/train.py')
        .set { train_script }

    TrainModel(model_input, train_script)
}