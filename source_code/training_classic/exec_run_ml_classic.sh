#!/bin/bash

python run_models_by_task.py ../../processed_dataset/kd_pdbbind/ ../../results/explore_kd_pdbbind/
python run_models_by_task.py ../../processed_dataset/proximate_dg/ ../../results/explore_proximate_dg/
python run_models_by_task.py ../../processed_dataset/proximate_kd/ ../../results/explore_proximate_kd/
python run_models_by_task.py ../../processed_dataset/proximate_kon/ ../../results/explore_proximate_kon/
python run_models_by_task.py ../../processed_dataset/skempi_affinity/ ../../results/explore_skempi_affinity/
python run_models_by_task.py ../../processed_dataset/skempi_koff/ ../../results/explore_skempi_koff/
python run_models_by_task.py ../../processed_dataset/skempi_kon/ ../../results/explore_skempi_kon/