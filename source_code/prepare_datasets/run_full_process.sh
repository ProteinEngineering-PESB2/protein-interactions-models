#!/bin/bash

python run_merge.py ../../encoded_sequences/ ../../unique_seq/unique_sequences.csv kon ../../processed_dataset/proximate_kon/ ../../datasets/proximate_kon.csv
python run_merge.py ../../encoded_sequences/ ../../unique_seq/unique_sequences.csv affinity ../../processed_dataset/skempi_affinity/ ../../datasets/skempi_affinity.csv
python run_merge.py ../../encoded_sequences/ ../../unique_seq/unique_sequences.csv koff ../../processed_dataset/skempi_koff/ ../../datasets/skempi_koff.csv
python run_merge.py ../../encoded_sequences/ ../../unique_seq/unique_sequences.csv kon ../../processed_dataset/skempi_kon/ ../../datasets/skempi_kon.csv

