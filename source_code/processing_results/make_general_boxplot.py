import pandas as pd
import sys
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-white")
plt.rc('axes', grid=False, facecolor="white")
plt.rcParams.update({'font.size': 14})

cnn_summary = pd.read_csv(sys.argv[1])
ml_summary = pd.read_csv(sys.argv[2])
gcn_summary = pd.read_csv(sys.argv[3])

path_export = sys.argv[4]

list_tasks = {'explore_proximate_dg': "Proximate-Dg", 'explore_proximate_kon':"Proximate-Kon", 'explore_skempi_koff':"skempi:Koff" , 
              'explore_proximate_kd': "Proximate-Kd", 'explore_skempi_affinity':"skempi-Affinity" , 'explore_skempi_kon':"skempi-Kon"}

list_dfs = []

fig, axes = plt.subplots(3, 2, figsize=(15, 5), sharey=True, sharex=True)
i = 0
j = 0
index =0

for task in list_tasks:
    index +=1

    print("Processing task: ", task)
    cnn_summary_filter = cnn_summary.loc[(cnn_summary['task'] == task) & (cnn_summary['train_mse'] <= 10000)]
    performance_cnn = cnn_summary_filter['train_mse']

    df_cnn = pd.DataFrame()
    df_cnn['performance'] = performance_cnn
    df_cnn['training'] = "CNN architectures"

    ml_summary_filter = ml_summary.loc[(ml_summary['task'] == task) & (ml_summary['test_mean_squared_error'] <= 10000)]
    performance_ml = ml_summary_filter['test_mean_squared_error']
    
    df_ml = pd.DataFrame()
    df_ml['performance'] = performance_ml
    df_ml['training'] = "ML classic"

    gcn_summary_filter = gcn_summary.loc[(gcn_summary['task'] == task) & (gcn_summary['train'] <= 10000)]
    performance_gcn = gcn_summary_filter['train']

    df_gcn = pd.DataFrame()
    df_gcn['performance'] = performance_gcn
    df_gcn['training'] = "GCN architectures"

    df_concat = pd.concat([df_cnn, df_gcn, df_ml], axis=0)
    df_concat['task'] = task

    list_dfs.append(df_concat)

    df_summary = pd.concat(list_dfs, axis=0)
    df_summary = df_summary.reset_index()

    g = sns.boxplot(ax=axes[i][j], data=df_summary, x="performance", y="training", hue="training", showfliers = False)
    axes[i][j].set_title(list_tasks[task])

    if index == 2 or index==4:
        i += 1
        j = 0
    else:
        j+=1

plt.savefig("{}summary_performances.svg".format(path_export, task))
plt.clf()
