import pandas as pd
import json
import sys
import os

list_tasks = ['explore_proximate_dg', 'explore_proximate_kon', 'explore_skempi_koff' , 'explore_pip', 'explore_proximate_kd', 'explore_skempi_affinity' , 'explore_skempi_kon']

path_results = sys.argv[1]
path_to_save_summary = sys.argv[2]

matrix_data = []

for task in list_tasks:
    print("Processing task: ", task)
    path_to_process = "{}{}/".format(path_results, task)

    list_results = os.listdir(path_to_process)
    list_results = [element for element in list_results if ".json" in element]

    for element in list_results:

        with open("{}{}".format(path_to_process, element)) as doc_json:
            data_load = json.load(doc_json)
        
        row_data = [task, element.split(".")[0], data_load['arquitecture']]
        train_performance = [data_load['train_metrics'][metric] for metric in ['mse', 'mae', 'r2_score', 'kendalltau', 'pearsonr', 'spearmanr']]
        test_performance = [data_load['test_metrics'][metric] for metric in ['mse', 'mae', 'r2', 'kendalltau', 'pearsonr', 'spearmanr']]

        row_data = row_data + train_performance + test_performance

        matrix_data.append(row_data)

df_process = pd.DataFrame(matrix_data, columns=['task', 'strategy', 'architecture', 'train_mse', 'train_mae', 'train_r2_score', 'train_kendalltau', 'train_pearsonr', 'train_spearmanr', 'test_mse', 'test_mae', 'test_r2_score', 'test_kendalltau', 'test_pearsonr', 'test_spearmanr'])
df_process.to_csv("{}summary_cnn.csv".format(path_to_save_summary), index=False)