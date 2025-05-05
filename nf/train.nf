#!/usr/bin/env nextflow
nextflow.enable.dsl=2

process TrainModel {
    input:
    path model_input        // CSV file from feature extraction
    path train_script

    output:
    path 'metrics.json'
    path 'predictions.csv'
    path 'model.pkl'

    publishDir "${workflow.projectDir}/outputs", mode: 'copy'

    script:
    """
    pip install scikit-learn joblib
    cp ${train_script} train.py
    python train.py ${model_input} .
    echo '✅ Contents of sandbox after train.py:'
    ls -lh
    """
}

workflow {
    // Input channels
    model_input = Channel.fromPath('data/model_ready/student_depression_dataset_model_ready.csv')
    train_script = Channel.fromPath('src/train.py')
    // Execute training
    TrainModel(model_input, train_script)
}
