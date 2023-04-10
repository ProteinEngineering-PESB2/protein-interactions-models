import os
import sys

path_input_encode = sys.argv[1]
unique_sequences = sys.argv[2]
column_response = sys.argv[3]
path_export = sys.argv[4]
raw_data = sys.argv[5]

list_path = os.listdir(path_input_encode)

for element in list_path:

    command = "mkdir -p {}{}".format(path_export, element)
    print(command)
    os.system(command)

    encoded_dataset = "{}{}/df.csv".format(path_input_encode, element)
    path_export_result = "{}{}/".format(path_export, element)

    command = "python merge_dataset.py {} {} {} {} {}".format(
        raw_data,
        encoded_dataset,
        unique_sequences,
        path_export_result,
        column_response
    )

    print(command)
    #os.system(command)
