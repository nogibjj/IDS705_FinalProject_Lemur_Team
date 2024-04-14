import streamlit as st
import pandas as pd
import numpy as np
import pickle


# list of dicts to convert readable to options model was trained on
ms_read = {
    "Never Married": "Never-married",
    "Married, Civilian Spouse": "Married-civ-spouse",
    "Divorced": "Divorced",
    "Married, Spouse Absent": "Married-spouse-absent",
    "Separated": "Separated",
    "Married, Armed Forces Spouse": "Married-AF-spouse",
    "Widowed": "Widowed",
}

occup_read = {
    "Transportation & Moving": "Transport-moving",
    "Professional Specialty": "Prof-specialty",
    "Farming & Fishing": "Farming-fishing",
    "Craft & Repair": "Craft-repair",
    "Sales": "Sales",
    "Other Service": "Other-service",
    "Protective Services": "Protective-serv",
    "Executive & Managerial": "Exec-managerial",
    "Unknown": "Unknown",
    "Handlers & Cleaners": "Handlers-cleaners",
    "Machine Operation & Inspection": "Machine-op-inspct",
    "Administrative & Clerical": "Adm-clerical",
    "Technical Support": "Tech-support",
    "Private Household Service": "Priv-house-serv",
    "Armed Forces": "Armed-Forces",
}

relationship_read = {
    "Husband": "Husband",
    "Unmarried": "Unmarried",
    "Not in Family": "Not-in-family",
    "Other Relative": "Other-relative",
    "Own Child": "Own-child",
    "Wife": "Wife",
}

workclass_read = {
    "Private": "Private",
    "State Government": "State-gov",
    "Local Government": "Local-gov",
    "Self-Employed (Non-Incorporated)": "Self-emp-not-inc",
    "Unknown": "Unknown",
    "Self-Employed (Incorporated)": "Self-emp-inc",
    "Federal Government": "Federal-gov",
    "Without Pay": "Without-pay",
    "Never Worked": "Never-worked",
}

feature_names = [
    "age",
    "marital-status",
    "hours-per-week",
    "occupation",
    "relationship",
    "workclass",
]


def create_input_form(short=True):
    inputs = {}
    for feature in feature_names:
        if feature == "age":
            inputs[feature] = st.slider(
                "Age", min_value=18, max_value=100, step=1, value=30
            )
        elif feature == "marital-status":
            inputs[feature] = st.selectbox(
                "Marital Status",
                [
                    "Never Married",
                    "Married, Civilian Spouse",
                    "Divorced",
                    "Married, Spouse Absent",
                    "Separated",
                    "Married, Armed Forces Spouse",
                    "Widowed",
                ],
            )
        elif feature == "hours-per-week":
            inputs[feature] = st.slider(
                "Hours per Week", min_value=0, max_value=100, step=1, value=40
            )
        elif feature == "occupation":
            inputs[feature] = st.selectbox(
                "Occupation",
                [
                    "Transportation & Moving",
                    "Professional Specialty",
                    "Farming & Fishing",
                    "Craft & Repair",
                    "Sales",
                    "Other Service",
                    "Protective Services",
                    "Executive & Managerial",
                    "Unknown",
                    "Handlers & Cleaners",
                    "Machine Operation & Inspection",
                    "Administrative & Clerical",
                    "Technical Support",
                    "Private Household Service",
                    "Armed Forces",
                ],
            )
        elif feature == "relationship":
            inputs[feature] = st.selectbox(
                "Relationship",
                [
                    "Husband",
                    "Unmarried",
                    "Not in Family",
                    "Other Relative",
                    "Own Child",
                    "Wife",
                ],
            )
        elif feature == "workclass":
            inputs[feature] = st.selectbox(
                "Workclass",
                [
                    "Private",
                    "State Government",
                    "Local Government",
                    "Self-Employed (Non-Incorporated)",
                    "Unknown",
                    "Self-Employed (Incorporated)",
                    "Federal Government",
                    "Without Pay",
                    "Never Worked",
                ],
            )

    return inputs


# make website
def main():
    # add title
    st.title("Income Level Predictor")
    # add picture
    # add form
    tab1, tab2 = st.tabs(["Top-6 Features Catboost Model", "Full Catboost Model"])
    with tab1:
        inputs = create_input_form()
        submitted = st.button("Submit", type="primary")
        if submitted:
            print("pressed")
            print(inputs)
            # convert the variables to the ones that were made readble to the models
            inputs["marital-status"] = ms_read[inputs["marital-status"]]
            inputs["occupation"] = occup_read[inputs["occupation"]]
            inputs["relationship"] = relationship_read[inputs["relationship"]]
            inputs["workclass"] = workclass_read[inputs["workclass"]]
            pred_df = pd.DataFrame([inputs], columns=feature_names)
            print(pred_df)
            # load model
            loaded_model = pickle.load(open("../websitemodel2.pkl", "rb"))
            # make prediction
            y_pred_proba = loaded_model.predict_proba(pred_df)[:, 1]
            # write prediction
            st.write(
                f"Probability of being in the upper and middle income class: {round(float(y_pred_proba)*100, 2)}%"
            )


if __name__ == "__main__":
    main()
