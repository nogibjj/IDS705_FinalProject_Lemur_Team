import pandas as pd
from patsy import dmatrices

path = "https://raw.githubusercontent.com/nogibjj/IDS705_FinalProject_Lemur_Team/main/00_original_data/adult.csv"
data = pd.read_csv(path)

data =  data.replace('?', None)
data['income'] = data['income'].replace({'<=50K.': 0, '<=50K': 0,  '>50K': 1,  '>50K.': 1})

categorical_cols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']

data_ohe = pd.get_dummies(data, columns=categorical_cols)

data_ohe.info()

output_path = "../01_transformed_data/adult_ohe.csv" 
data_ohe.to_csv(output_path, index=False)