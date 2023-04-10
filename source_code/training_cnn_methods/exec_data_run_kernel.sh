#!/usr/bin/bash

python run_by_folder_kernel.py ../../processed_dataset_transform/kd_pdbbind/ ../../results/explore_kd_pdbbind/
python run_by_folder_kernel.py ../../processed_dataset_transform/proximate_dg/ ../../results/explore_proximate_dg/
python run_by_folder_kernel.py ../../processed_dataset_transform/proximate_kd/ ../../results/explore_proximate_kd/
python run_by_folder_kernel.py ../../processed_dataset_transform/proximate_kon/ ../../results/explore_proximate_kon/
python run_by_folder_kernel.py ../../processed_dataset_transform/skempi_affinity/ ../../results/explore_skempi_affinity/
python run_by_folder_kernel.py ../../processed_dataset_transform/skempi_koff/ ../../results/explore_skempi_koff/
python run_by_folder_kernel.py ../../processed_dataset_transform/skempi_kon/ ../../results/explore_skempi_kon/ 

python run_by_folder_pca.py ../../processed_dataset_transform/kd_pdbbind/ ../../results/explore_kd_pdbbind/
python run_by_folder_pca.py ../../processed_dataset_transform/proximate_dg/ ../../results/explore_proximate_dg/
python run_by_folder_pca.py ../../processed_dataset_transform/proximate_kd/ ../../results/explore_proximate_kd/
python run_by_folder_pca.py ../../processed_dataset_transform/proximate_kon/ ../../results/explore_proximate_kon/
python run_by_folder_pca.py ../../processed_dataset_transform/skempi_affinity/ ../../results/explore_skempi_affinity/
python run_by_folder_pca.py ../../processed_dataset_transform/skempi_koff/ ../../results/explore_skempi_koff/
python run_by_folder_pca.py ../../processed_dataset_transform/skempi_kon/ ../../results/explore_skempi_kon/ 