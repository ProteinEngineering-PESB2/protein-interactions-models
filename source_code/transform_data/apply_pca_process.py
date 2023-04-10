import pandas as pd
import sys
from pca_process import transformation_data

df_data = pd.read_csv(sys.argv[1])
path_export = sys.argv[2]

response = df_data['response']
df_data = df_data.drop(columns=['response'])

transformation_instance = transformation_data()
print("Apply PCA")
transform_data, pca_instance = transformation_instance.apply_pca_linear(dataset=df_data)

header = ["p_{}".format(i) for i in range(len(transform_data[0]))]
df_pca = pd.DataFrame(transform_data, columns=header)
df_pca = df_pca.round(decimals=5)
df_pca['response'] = response

print("Apply kernel PCA")
transform_data, kernel_pca_instance = transformation_instance.apply_kernel_pca(dataset=df_data)

header = ["p_{}".format(i) for i in range(len(transform_data[0]))]
df_pca_kernel = pd.DataFrame(transform_data, columns=header)
df_pca_kernel = df_pca_kernel.round(decimals=5)
df_pca_kernel['response'] = response

print("Export data")
df_pca.to_csv("{}pca_data.csv".format(path_export), index=False)
df_pca_kernel.to_csv("{}kernel_pca_data.csv".format(path_export), index=False)
