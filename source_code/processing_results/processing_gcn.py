import pandas as pd
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
    list_results = [element for element in list_results if ".csv" in element]

    for element in list_results:
        df_data = pd.read_csv("{}{}".format(path_to_process, element))
        train = df_data.loc[(df_data['Stage'] == 'train') & (df_data['Epochs'] == 100)]
        test = df_data.loc[(df_data['Stage'] == 'test') & (df_data['Epochs'] == 100)]

        train = train.reset_index()
        test = test.reset_index()

        row = [task, train['Features_used'][0], train['Loss(BCE)'][0], test['Loss(BCE)'][0]]
        matrix_data.append(row)

df_export = pd.DataFrame(matrix_data, columns=['task', 'strategy', 'train', 'test'])
df_export.to_csv("{}summary_gcn.csv".format(path_to_save_summary), index=False)

