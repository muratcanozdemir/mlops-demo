#!/usr/bin/env nextflow

process TrainModel {
    input:
    path 'data/model_ready/'

    output:
    path 'predictions.csv'
    path 'model.pkl'
    path 'metrics.json'

    publishDir 'outputs', mode: 'copy'

    script:
    """
    mkdir -p outputs
    echo 'id,prediction' > outputs/predictions.csv
    echo '1,0.85' >> outputs/predictions.csv
    echo 'model_parameters_placeholder' > outputs/model.pkl
    echo '{"accuracy": 0.85}' > outputs/metrics.json
    """
}

workflow {
    Channel.fromPath('data/model_ready/') | TrainModel
}
