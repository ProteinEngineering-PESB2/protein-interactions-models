import sys
import os

path_input = sys.argv[1]
path_export = sys.argv[2]

list_data = os.listdir(path_input)

for element in list_data:
    print("Processing element: ", element)
    df_input = "{}{}/pca_data.csv".format(
        path_input,
        element
    )

    suffix = "{}_pca".format(
        element
    )

    command = "python cnn_explore.py {} {} {} {}".format(
        df_input,
        50,
        path_export,
        suffix
    )
    print(command)
    os.system(command)