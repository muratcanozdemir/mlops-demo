#!/usr/bin/env nextflow
nextflow.enable.dsl=2

process TrainModel {
    input:
    path model_input        // CSV file from feature extraction
    path train_script       // Python script that runs training

    output:
    path 'outputs/metrics.json'
    path 'outputs/predictions.csv'
    path 'outputs/model.pkl'

    publishDir "${projectDir}/outputs", mode: 'copy'

    script:
    """
    mkdir -p outputs
    python train.py ${model_input} outputs
    """
}

workflow {
    // Input channels
    model_input = Channel.fromPath('data/model_ready/student_depression_dataset_model_ready.csv')
    train_script = Channel.fromPath('src/train.py')

    // Execute training
    TrainModel(model_input, train_script)
}
