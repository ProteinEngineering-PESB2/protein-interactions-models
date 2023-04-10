import pandas as pd
import sys

def search_sequence_encode(seq, unique_sequences, data_coded):
    df_seq = unique_sequences.loc[unique_sequences['sequence'] == seq]
    df_seq = df_seq.reset_index()

    id_seq1 = df_seq['id'][0]

    data_filter = data_coded.loc[data_coded['id'] == id_seq1]
    data_filter = data_filter.reset_index()

    row = [data_filter[key][0] for key in data_filter.columns if "p_" in key]

    return row   

print("Process data")
raw_data = pd.read_csv(sys.argv[1])
encoded_dataset = pd.read_csv(sys.argv[2])
unique_sequences = pd.read_csv(sys.argv[3])
path_export = sys.argv[4]
column_response = sys.argv[5]

matrix_data_seq1= []
matrix_data_seq2= []

responses = []

print("Searching sequences in encoded elements")
for index in raw_data.index:
    
    #get sequences and response
    seq1 = raw_data['seq_1'][index]
    seq2 = raw_data['seq_2'][index]

    try:
        row_seq1 = search_sequence_encode(seq1, unique_sequences, encoded_dataset)
        row_seq2 = search_sequence_encode(seq2, unique_sequences, encoded_dataset)

        matrix_data_seq1.append(row_seq1)
        matrix_data_seq2.append(row_seq2)
        responses.append(raw_data[column_response][index])
    except:
        pass

print("Creating header")
header1 = ["p1_{}".format(i) for i in range(len(matrix_data_seq1[0]))]
header2 = ["p2_{}".format(i) for i in range(len(matrix_data_seq2[0]))]

df_seq1 = pd.DataFrame(matrix_data_seq1, columns=header1)
df_seq2 = pd.DataFrame(matrix_data_seq2, columns=header2)

#concat 
print("Concat")
df_concat = pd.concat([df_seq1, df_seq2], axis=1)
df_concat['response'] = responses

df_concat.to_csv("{}data_join.csv".format(path_export), index=False)