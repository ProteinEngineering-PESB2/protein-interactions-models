from nlp_via_pretrained_models import using_bioembedding
import pandas as pd

df_data = pd.read_csv("../unique_seq/unique_sequences.csv")

using_bioembedding_instance = using_bioembedding(
    dataset=df_data,
    id_seq='name',
    column_seq='sequence',
    is_reduced=True,
    device = 'cuda'
)

#apply bepler
print("Bepler")
#using_bioembedding_instance.apply_bepler()

#header = ["p_{}".format(i) for i in range(len(using_bioembedding_instance.np_data[0]))]
#df_data_encode = pd.DataFrame(using_bioembedding_instance.np_data, columns=header)
#df_data_encode['id'] = df_data['id']
#df_data_encode.to_csv("../nlp_encoding/bepler/dataset_encoding.csv", index=False)

#apply esm
print("esm1b")
try:
    using_bioembedding_instance.apply_esm1b()

    header = ["p_{}".format(i) for i in range(len(using_bioembedding_instance.np_data[0]))]
    df_data_encode = pd.DataFrame(using_bioembedding_instance.np_data, columns=header)
    df_data_encode['id'] = df_data['id']
    df_data_encode.to_csv("../nlp_encoding/esm1b/dataset_encoding.csv", index=False)
except:
    pass

#apply esm
try:
    print("esme")
    using_bioembedding_instance.apply_esme()

    header = ["p_{}".format(i) for i in range(len(using_bioembedding_instance.np_data[0]))]
    df_data_encode = pd.DataFrame(using_bioembedding_instance.np_data, columns=header)
    df_data_encode['id'] = df_data['id']
    df_data_encode.to_csv("../nlp_encoding/esme/dataset_encoding.csv", index=False)
except:
    pass

#apply fasttext
print("fasttext")
using_bioembedding_instance.apply_fasttext()

header = ["p_{}".format(i) for i in range(len(using_bioembedding_instance.np_data[0]))]
df_data_encode = pd.DataFrame(using_bioembedding_instance.np_data, columns=header)
df_data_encode['id'] = df_data['id']
df_data_encode.to_csv("../nlp_encoding/fasttext/dataset_encoding.csv", index=False)

#apply one hot
print("One hot")
try:
    using_bioembedding_instance.apply_onehot()

    header = ["p_{}".format(i) for i in range(len(using_bioembedding_instance.np_data[0]))]
    df_data_encode = pd.DataFrame(using_bioembedding_instance.np_data, columns=header)
    df_data_encode['id'] = df_data['id']
    df_data_encode.to_csv("../nlp_encoding/onehot/dataset_encoding.csv", index=False)
except:
    pass

#apply glove
print("Glove")
try:
    using_bioembedding_instance.apply_glove()

    header = ["p_{}".format(i) for i in range(len(using_bioembedding_instance.np_data[0]))]
    df_data_encode = pd.DataFrame(using_bioembedding_instance.np_data, columns=header)
    df_data_encode['id'] = df_data['id']
    df_data_encode.to_csv("../nlp_encoding/glove/dataset_encoding.csv", index=False)
except:
    pass

#apply glove
print("Plusrnn")
try:
    using_bioembedding_instance.apply_plus_rnn()

    header = ["p_{}".format(i) for i in range(len(using_bioembedding_instance.np_data[0]))]
    df_data_encode = pd.DataFrame(using_bioembedding_instance.np_data, columns=header)
    df_data_encode['id'] = df_data['id']
    df_data_encode.to_csv("../nlp_encoding/plusrnn/dataset_encoding.csv", index=False)
except:
    pass