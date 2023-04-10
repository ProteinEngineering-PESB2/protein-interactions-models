import pandas as pd
import sys

cnn_summary = pd.read_csv(sys.argv[1])
ml_summary = pd.read_csv(sys.argv[2])
gcn_summary = pd.read_csv(sys.argv[3])
path_export = sys.argv[4]

list_tasks = {'explore_proximate_dg': "Proximate-Dg", 'explore_proximate_kon':"Proximate-Kon", 'explore_skempi_koff':"skempi:Koff" , 
              'explore_proximate_kd': "Proximate-Kd", 'explore_skempi_affinity':"skempi-Affinity" , 'explore_skempi_kon':"skempi-Kon"}

matrix_data = []

for task in list_tasks:
    print("Processing task: ", task)
    cnn_summary_filter = cnn_summary.loc[(cnn_summary['task'] == task) & (cnn_summary['train_mse'] <= 10000)]
    cnn_summary_filter = cnn_summary_filter[['train_mse', 'strategy']]
    cnn_summary_filter = cnn_summary_filter.sort_values(by='train_mse')
    cnn_summary_filter = cnn_summary_filter.reset_index()
    cnn_best = cnn_summary_filter.iloc[0].tolist()
    cnn_best.insert(0, "CNN")
    cnn_best.insert(0, task)
    
    ml_summary_filter = ml_summary.loc[(ml_summary['task'] == task) & (ml_summary['test_mean_squared_error'] <= 10000)]
    ml_summary_filter = ml_summary_filter[['test_mean_squared_error', 'strategy']]
    ml_summary_filter = ml_summary_filter.sort_values(by='test_mean_squared_error')
    ml_summary_filter = ml_summary_filter.reset_index()
    ml_best = ml_summary_filter.iloc[0].tolist()
    ml_best.insert(0, "ML")
    ml_best.insert(0, task)
    
    gcn_summary_filter = gcn_summary.loc[(gcn_summary['task'] == task) & (gcn_summary['train'] <= 10000)]
    gcn_summary_filter = gcn_summary_filter[['train', 'strategy']]
    gcn_summary_filter = gcn_summary_filter.sort_values(by='train')
    gcn_summary_filter = gcn_summary_filter.reset_index()
    gcn_best = gcn_summary_filter.iloc[0].tolist()
    gcn_best.insert(0, "GCN")
    gcn_best.insert(0, task)

    matrix_data.append(cnn_best)
    matrix_data.append(ml_best)
    matrix_data.append(gcn_best)

df_export = pd.DataFrame(matrix_data, columns=['task', 'method', 'strategy', 'MSE'])
df_export.to_csv("{}best_methods.csv".format(path_export), index=False)