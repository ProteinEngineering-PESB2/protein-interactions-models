import sys
import dgl
import os
import torch
import random
import argparse
import pandas as pd
import torch.nn as nn
import torch.optim as optim
from model_a import EdgeWeightPredictor
import torch.nn.functional as F

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def main():

    edges_file = sys.argv[1]
    weights_file = sys.argv[2]
    data_features = sys.argv[3]
    name_export = sys.argv[4]
    epochs = int(sys.argv[5])
    test_split = 0.3
    hidden_layers = int(sys.argv[6])
    feature = sys.argv[7]

    Dataframe = pd.read_csv(edges_file, na_filter = False, dtype={'edge_1': int, 'edge_2': int})
    edge_1 = Dataframe['edge_1'].values
    edge_2 = Dataframe['edge_2'].values
    Dataframe = pd.read_csv(weights_file, na_filter = False, dtype={'weights': float})
    weights = Dataframe['weights'].values
    transform = 'no_transform'
    Dataframe = pd.read_csv(data_features, na_filter = False, sep='|')
    
    nodes_features_df = Dataframe.values
    nodes_features = []
    for i, col in enumerate(nodes_features_df):
            array = []
            split = nodes_features_df[i][0].split(',')
            for j in split:
                array.append(float(j))
            nodes_features.append(array)

    df_losse = []
    df_stage = []
    df_method = []
    df_transform = []
    df_epochs = []
    
    nodes_features = torch.tensor(nodes_features)
    weights = torch.from_numpy(weights)

    g = dgl.graph((edge_1, edge_2))
    g.ndata['feat'] = nodes_features
    g.edata['weights'] = weights

    num_features = g.ndata['feat'][0].shape[0]
    num_edges = g.number_of_edges()

    # Definir hidden_layers si no se declararon
    if hidden_layers == '':
        hidden_layers = num_features

    # Dividir set de datos
    n = int(num_edges)
    ids_edges = list(range(num_edges))
    tamano_test = int(n * test_split) # Aquí se reserva un 20% de la muestra para el testeo
    # Dividir aleatoriamente la lista de edges
    random.seed(123)
    random.shuffle(ids_edges)
    set_entrenamiento = ids_edges[tamano_test:n]
    set_test = ids_edges[:tamano_test]

    sub_g = dgl.edge_subgraph(g, set_entrenamiento).to(device)
    sub_g_test = dgl.edge_subgraph(g, set_test).to(device)

    # SET ENTRENAMIENTO
    src, dst = sub_g.edges()
    train_edges = torch.cat([src.unsqueeze(0), dst.unsqueeze(0)], dim=0)

    # SET TEST
    src, dst = sub_g_test.edges()
    test_edges = torch.cat([src.unsqueeze(0), dst.unsqueeze(0)], dim=0)

    model = EdgeWeightPredictor(num_features, 1).to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    print('Iniciando entrenamiento...')
    # Ciclo de entrenamiento
    for epoch in range(epochs):
        df_epochs.append(epoch + 1)
        df_stage.append('train')
        df_method.append(feature)
        df_transform.append(transform)
        model.train()
        optimizer.zero_grad()
        out = model(sub_g.ndata['feat'], train_edges)
        loss = criterion(out.float(), sub_g.edata['weights'].float())
        loss.backward()
        df_losse.append(loss.item())
        # print(f'-----------------------------------------Epoch: {epoch:03d}')
        # print('Loss train: ', loss.item())
        optimizer.step()
        # Testeo
        with torch.no_grad():
            df_epochs.append(epoch + 1)
            df_stage.append('test')
            df_method.append(feature)
            df_transform.append(transform)
            model.eval()
            out = model(sub_g_test.ndata['feat'], test_edges)
            loss = criterion(out.float(), sub_g_test.edata['weights'].float())
            df_losse.append(loss.item())
            # print('------------------TEST--------------------')
            # print('Loss test: ', loss.item())
    # print('Entrenamiento termiando y modelo guardandose')
    # torch.save(model, 'modelos/trainned_model_edge_regressor_pip.pth')
    table = pd.DataFrame()
    table['Epochs'] = df_epochs
    table['Features_used'] = df_method
    table['Transform_method'] = df_transform
    table['Stage'] = df_stage
    table['Loss(BCE)'] = df_losse
    
    print('Entrenamiento finalizado...')
    table.to_csv(name_export, index=False)

if __name__ == "__main__":
    
    main()
