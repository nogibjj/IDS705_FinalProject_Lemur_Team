import pandas as pd
from patsy import dmatrices
from sklearn.preprocessing import StandardScaler

path = "https://raw.githubusercontent.com/nogibjj/IDS705_FinalProject_Lemur_Team/main/00_original_data/adult.csv"
data = pd.read_csv(path)

data =  data.replace('?', None)
data['income'] = data['income'].replace({'<=50K.': 0, '<=50K': 0,  '>50K': 1,  '>50K.': 1})

data.insert(0, 'income', data.pop('income'))
data['native-country_United-States'] = (data['native-country'] == 'United-States').astype(int)
data.drop('native-country', axis=1, inplace=True)

numeric_cols = ['age', 'fnlwgt', 'education-num', 'capital-gain',
       'capital-loss', 'hours-per-week', 'native-country_United-States']
scaler = StandardScaler()
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

categorical_cols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex']
data_ohe = pd.get_dummies(data, columns=categorical_cols)

output_path = "../01_clean_data/adult_ohe.csv" 
data_ohe.to_csv(output_path, index=False)

