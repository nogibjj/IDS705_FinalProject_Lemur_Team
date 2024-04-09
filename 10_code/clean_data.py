import pandas as pd
import sys
import os
import warnings
import matplotlib.pyplot as plt
from sklearn.exceptions import ConvergenceWarning
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
)
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
from scipy.stats import loguniform


warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=ConvergenceWarning)

if not sys.warnoptions:
    warnings.simplefilter("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore"

data = pd.read_csv("../00_original_data/adult.csv")
data = data.replace("?", None)
data["income"] = data["income"].replace(
    {"<=50K.": 0, "<=50K": 0, ">50K": 1, ">50K.": 1}
)
data.insert(0, "income", data.pop("income"))
data["native-country_United-States"] = (
    data["native-country"] == "United-States"
).astype(int)
data.drop("native-country", axis=1, inplace=True)

data.drop("fnlwgt", axis=1, inplace=True)
data.drop("education", axis=1, inplace=True)

# grab numeric cols
numeric_cols = [
    "age",
    "fnlwgt",
    "education-num",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
]
# grab categroical cols
categorical_cols = [
    "native-country_United-States",
    "workclass",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
]

feature_names = data.columns.tolist()[1:]

# define categorical and numerical indices for later preprocessing
categorical_columns_indices = [feature_names.index(cn) for cn in categorical_cols]
numerical_columns_indices = [
    feature_names.index(fn) for fn in feature_names if fn not in categorical_cols
]

encoder = OneHotEncoder(handle_unknown="ignore")
encoded_data = encoder.fit_transform(data[categorical_cols])

# Create DataFrame for encoded features with proper column naming
new_column_names = encoder.get_feature_names_out(categorical_cols)
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=new_column_names)

# Drop the original categorical columns and join the encoded data
data = data.drop(categorical_cols, axis=1)
data = pd.concat([data, encoded_df], axis=1)

import pandas as pd

# Assuming 'data' is your DataFrame
new_names = {
    'income': 'income',
    'age': 'Age',
    'education-num': 'Education Level',
    'capital-gain': 'Dollar gain of capital',
    'capital-loss': 'Dollar loss of capital',
    'hours-per-week': 'Working hours per week',
    'native-country_United-States_0': 'US Native: (No)',
    'native-country_United-States_1': 'US Native: (Yes)',
    'workclass_Federal-gov': 'Work Class: Federal Government',
    'workclass_Local-gov': 'Work Class: Local Government',
    'workclass_Never-worked': 'Work Class: Never Worked',
    'workclass_Private': 'Work Class: Private',
    'workclass_Self-emp-inc': 'Work Class: Self Employed (Incorporated)',
    'workclass_Self-emp-not-inc': 'Work Class: Self Employed (Not Incorporated)',
    'workclass_State-gov': 'Work Class: State Government',
    'workclass_Without-pay': 'Work Class: Without Pay',
    'workclass_None': 'Work Class: None',
    'workclass_nan': 'Work Class: Not Available',
    'marital-status_Divorced': 'Marital Status: Divorced',
    'marital-status_Married-AF-spouse': 'Marital Status: Married (AF Spouse)',
    'marital-status_Married-civ-spouse': 'Marital Status: Married (Civilian Spouse)',
    'marital-status_Married-spouse-absent': 'Marital Status: Married (Spouse Absent)',
    'marital-status_Never-married': 'Marital Status: Never Married',
    'marital-status_Separated': 'Marital Status: Separated',
    'marital-status_Widowed': 'Marital Status: Widowed',
    'occupation_Adm-clerical': 'Occupation: Administrative Clerical',
    'occupation_Armed-Forces': 'Occupation: Armed Forces',
    'occupation_Craft-repair': 'Occupation: Craft Repair',
    'occupation_Exec-managerial': 'Occupation: Executive Managerial',
    'occupation_Farming-fishing': 'Occupation: Farming Fishing',
    'occupation_Handlers-cleaners': 'Occupation: Handlers Cleaners',
    'occupation_Machine-op-inspct': 'Occupation: Machine Op Inspection',
    'occupation_Other-service': 'Occupation: Other Service',
    'occupation_Priv-house-serv': 'Occupation: Private House Service',
    'occupation_Prof-specialty': 'Occupation: Professional Specialty',
    'occupation_Protective-serv': 'Occupation: Protective Service',
    'occupation_Sales': 'Occupation: Sales',
    'occupation_Tech-support': 'Occupation: Tech Support',
    'occupation_Transport-moving': 'Occupation: Transport Moving',
    'occupation_None': 'Occupation: None',
    'occupation_nan': 'Occupation: Not Available',
    'relationship_Husband': 'Relationship: Husband',
    'relationship_Not-in-family': 'Relationship: Not in Family',
    'relationship_Other-relative': 'Relationship: Other Relative',
    'relationship_Own-child': 'Relationship: Own Child',
    'relationship_Unmarried': 'Relationship: Unmarried',
    'relationship_Wife': 'Relationship: Wife',
    'race_Amer-Indian-Eskimo': 'Race: Amer Indian Eskimo',
    'race_Asian-Pac-Islander': 'Race: Asian Pac Islander',
    'race_Black': 'Race: Black',
    'race_Other': 'Race: Other',
    'race_White': 'Race: White',
    'sex_Female': 'Sex: Female',
    'sex_Male': 'Sex: Male'
}

data = data.rename(columns=new_names)


data.to_csv("../01_clean_data/adult_ohe.csv", index=False)
