import sys
import os

path_input = sys.argv[1]
path_export = sys.argv[2]

list_strategies = os.listdir("{}no_transform/".format(path_input))

for element in list_strategies:
    command = "python gnn_edge_regression_pip.py {} {} {} {} {} {} {}".format(
        "{}edge_index.csv".format(path_input),
        "{}weights.csv".format(path_input),
        "{}no_transform/{}/nodes_features_.csv".format(path_input, element),
        "{}{}_gcn_explore_C.csv".format(path_export, element),
        100,
        15,
        element
    )
    print(command)
    os.system(command)
