import sys
import os

path_input = sys.argv[1]
path_export = sys.argv[2]

list_data = os.listdir(path_input)

for element in list_data:
    print("Processing element: ", element)
    df_input = "{}{}/data_join.csv".format(
        path_input,
        element
    )

    command = "python cnn_explore.py {} {} {} {}".format(
        df_input,
        30,
        path_export,
        element
    )
    print(command)
    os.system(command)
    
