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

data.to_csv("../01_clean_data/adult_ohe.csv", index=False)
