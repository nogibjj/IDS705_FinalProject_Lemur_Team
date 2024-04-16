import streamlit as st
import pandas as pd
import pickle
import path
import os

path = os.path.dirname(__file__)


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

education_read = {
    "Preschool": 1,
    "Grade 1-4": 2,
    "Grade 5-6": 3,
    "Grade 7-8": 4,
    "Grade 9": 5,
    "Grade 10": 6,
    "Grade 11": 7,
    "Grade 12": 8,
    "High School Graduate": 9,
    "Some College, No Degree": 10,
    "Associate of Vocational": 11,
    "Associate of Academic": 12,
    "Bachelor's": 13,
    "Master's": 14,
    "Professional School Degree": 15,
    "Doctorate Degree": 16,
}

feature_names = [
    "age",
    "marital-status",
    "hours-per-week",
    "occupation",
    "education-num",
    "workclass",
]

feature_names2 = [
    "age",
    "workclass",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country_United-States",
]


def create_input_form(short=True):
    inputs = {}
    fts = feature_names if short else feature_names2
    name = "simple" if short else "long"
    for feature in fts:
        if feature == "age":
            inputs[feature] = st.slider(
                "Age", min_value=18, max_value=100, step=1, value=30, key="1" + name
            )
        elif feature == "education-num":
            inputs[feature] = st.selectbox(
                "Education Level",
                [
                    "Preschool",
                    "Grade 1-4",
                    "Grade 5-6",
                    "Grade 7-8",
                    "Grade 9",
                    "Grade 10",
                    "Grade 11",
                    "Grade 12",
                    "High School Graduate",
                    "Some College, No Degree",
                    "Associate of Vocational",
                    "Associate of Academic",
                    "Bachelor's",
                    "Master's",
                    "Professional School Degree",
                    "Doctorate Degree",
                ],
                key="2" + name,
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
                key="3" + name,
            )
        elif feature == "hours-per-week":
            inputs[feature] = st.slider(
                "Hours Worked per Week",
                min_value=0,
                max_value=100,
                step=1,
                value=40,
                key="4" + name,
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
                key="5" + name,
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
                key="6" + name,
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
                key="7" + name,
            )
        elif feature == "race":
            inputs[feature] = st.selectbox(
                "Race",
                ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"],
                key="8" + name,
            )
        elif feature == "sex":
            inputs[feature] = st.selectbox(
                "Sex",
                ["Male", "Female"],
                key="9" + name,
            )
        elif feature == "capital-gain":
            inputs[feature] = st.number_input(
                "Capital Gain",
                key="10" + name,
            )
        elif feature == "capital-loss":
            inputs[feature] = st.number_input(
                "Capital Loss",
                key="12" + name,
            )
        elif feature == "native-country_United-States":
            inputs[feature] = st.selectbox(
                "Native Country",
                ["United States", "Outside of United States"],
                key="13" + name,
            )

    return inputs


# make website
def main():
    # add title
    st.title("Income Level Model Presentation")
    # add picture
    st.image(path + "/final.jpg")
    # add form
    tab1, tab2 = st.tabs(["Top-6 Common Features", "Full Catboost Model"])
    with tab1:
        inputs = create_input_form()
        submitted = st.button(
            "Submit",
            type="primary",
            key=3232,
        )
        if submitted:
            # convert the variables to the ones that were made readble to the models
            inputs["education-num"] = education_read[inputs["education-num"]]
            inputs["marital-status"] = ms_read[inputs["marital-status"]]
            inputs["occupation"] = occup_read[inputs["occupation"]]
            # inputs["relationship"] = relationship_read[inputs["relationship"]]
            inputs["workclass"] = workclass_read[inputs["workclass"]]
            pred_df = pd.DataFrame([inputs], columns=feature_names)
            print(pred_df)
            # load model
            path_to_model = path + "/websitemodel2.pkl"
            with open(path_to_model, "rb") as file:
                loaded_model = pickle.load(file)
            # make prediction
            y_pred_proba = loaded_model.predict_proba(pred_df)[:, 1]
            # write prediction
            st.write(
                f"Probability of being in the upper and middle income class: {round(float(y_pred_proba)*100, 2)}%"
            )
    with tab2:
        inputs2 = create_input_form(
            short=False,
        )
        submitted = st.button(
            "Submit",
            type="primary",
            key=12312,
        )
        if submitted:
            print(inputs2)
            # convert the variables to the ones that were made readble to the models
            inputs2["education-num"] = education_read[inputs2["education-num"]]
            inputs2["marital-status"] = ms_read[inputs2["marital-status"]]
            inputs2["occupation"] = occup_read[inputs2["occupation"]]
            inputs2["relationship"] = relationship_read[inputs2["relationship"]]
            inputs2["workclass"] = workclass_read[inputs2["workclass"]]
            inputs2["native-country_United-States"] = (
                1 if inputs2["native-country_United-States"] == "United States" else 0
            )
            pred_df = pd.DataFrame([inputs2], columns=feature_names2)
            # load model
            path_to_model = path + "/websitemodel1.pkl"
            with open(path_to_model, "rb") as file:
                loaded_model = pickle.load(file)
            # make prediction
            y_pred_proba = loaded_model.predict_proba(pred_df)[:, 1]
            # write prediction
            st.write(
                f"Probability of being in the upper and middle income class: {round(float(y_pred_proba)*100, 2)}%"
            )


if __name__ == "__main__":
    main()
