import pandas as pd
import sys
import os

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8-white")
plt.rc('axes', grid=False, facecolor="white")
plt.rcParams.update({'font.size': 14})

def get_values(path_data):

    list_to_check = ['fft_alpha_structure_gcn_explore_C.csv', 'bepler_gcn_explore_C.csv', 'physicochemical_secondary_structure_gcn_explore_C.csv']
    list_data = os.listdir(path_data)
    list_data = [value for value in list_data if value in list_to_check]

    list_df = []

    for element in list_data:
        df = pd.read_csv("{}{}".format(path_data, element))
        df = df.loc[df['Stage'] == 'test']
        df = df.reset_index()
        df = df[['Epochs', 'Loss(BCE)']]

        if "fft" in element:
            df['Strategy'] = "FFT-applications"
        elif "bepler" in element:
            df['Strategy'] = "NLP strategies"
        else:
            df['Strategy'] = "Physicochemical properties"
        list_df.append(df)
    
    df_concat = pd.concat(list_df, axis=0)
    return df_concat

path_affinity = sys.argv[1]
path_kd = sys.argv[2]
path_proximate_dg = sys.argv[3]
path_skempi_kon = sys.argv[4]
path_export = sys.argv[5]

df_affinity = get_values(path_affinity)
df_kd = get_values(path_kd)
df_dg = get_values(path_proximate_dg)
df_kon = get_values(path_skempi_kon)


fig, axes = plt.subplots(1, 3, figsize=(16, 8), sharex=True)

g = sns.lineplot(ax=axes[0], data=df_affinity, x="Epochs", y="Loss(BCE)", hue="Strategy")
axes[0].set_title("Skempi-Affinity")

g = sns.lineplot(ax=axes[1], data=df_kd, x="Epochs", y="Loss(BCE)", hue="Strategy")
axes[1].set_title("Proximate-Kd")


g = sns.lineplot(ax=axes[2], data=df_dg, x="Epochs", y="Loss(BCE)", hue="Strategy")
axes[2].set_title("Proximate-Dg")

plt.savefig("{}check_loss.svg".format(path_export))
plt.clf()
