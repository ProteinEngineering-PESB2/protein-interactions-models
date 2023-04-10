import pandas as pd
import sys
import os

path_input = sys.argv[1]
path_export = sys.argv[2]

list_data = os.listdir(path_input)

for element in list_data:
    command = "mkdir -p {}{}".format(
        path_export,
        element
    )

    print(command)
    os.system(command)

    command = "python apply_pca_process.py {}{}/data_join.csv {}{}/".format(
        path_input,
        element,
        path_export,
        element
    )
    print(command)
    os.system(command)