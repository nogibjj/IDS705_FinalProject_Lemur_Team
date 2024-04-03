# IDS705_FinalProject_Lemur_Team

Link Report:
https://docs.google.com/document/d/1HN4mchz_zsuOidYjAimyThBtTNHpZmfiyYBB70LaeJM/edit#heading=h.707ucl6d05og


Reminder

In order to use the same split for all of the models, please use:

```python
path = "https://raw.githubusercontent.com/nogibjj/IDS705_FinalProject_Lemur_Team/main/01_clean_data/adult_ohe.csv"

adult_ohe = pd.read_csv(path)

X = adult_ohe.drop(columns=["income"])
y = adult_ohe["income"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

```
