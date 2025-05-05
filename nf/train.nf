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
    echo 'id,prediction' > predictions.csv
    echo '1,0.85' >> predictions.csv
    echo 'model_parameters_placeholder' > model.pkl
    echo '{"accuracy": 0.85}' > metrics.json
    """
}

workflow {
    Channel.fromPath('data/model_ready/') | TrainModel
}
