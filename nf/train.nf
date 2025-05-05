#!/usr/bin/env nextflow
nextflow.enable.dsl=2

process TrainModel {
    input:
    path model_input        // CSV file from feature extraction

    output:
    path 'metrics.json'
    path 'predictions.csv'
    path 'model.pkl'

    publishDir "${projectDir}/outputs", mode: 'copy'

    script:
    """
    pip install scikit-learn joblib
    python ${projectDir}/src/train.py ${model_input} .
    echo '✅ Contents of sandbox after train.py:'
    ls -lh
    """
}

workflow {
    // Input channels
    model_input = Channel.fromPath('data/model_ready/student_depression_dataset_model_ready.csv')

    // Execute training
    TrainModel(model_input)
}
