import pandas as pd
import sys
import os

list_tasks = ['explore_proximate_dg', 'explore_proximate_kon', 'explore_skempi_koff' , 'explore_proximate_kd', 'explore_skempi_affinity' , 'explore_skempi_kon']

path_results = sys.argv[1]
path_to_save_summary = sys.argv[2]

list_df = []

for task in list_tasks:
    print("Processing task: ", task)
    path_to_process = "{}{}/".format(path_results, task)

    list_files = os.listdir(path_to_process)

    for element in list_files:
        df_data = pd.read_csv("{}{}".format(path_to_process, element))
        df_data['task'] = task
        df_data['strategy'] = element.split(".")[0]

        list_df.append(df_data)

df_concat = pd.concat(list_df, axis=0)
df_concat.to_csv("{}summary_ml.csv".format(path_to_save_summary), index=False)