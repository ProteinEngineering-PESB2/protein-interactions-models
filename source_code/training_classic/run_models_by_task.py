import sys
import os

path_input = sys.argv[1]
path_export = sys.argv[2]

list_folders = os.listdir(path_input)

for element in list_folders:
    df = "{}{}/data_join.csv".format(path_input, element)
    name_export = "{}{}_normal_data.csv".format(path_export, element)

    command = "python training_ml_models.py {} {}".format(
        df,
        name_export
    )

    print(command)
    os.system(command)