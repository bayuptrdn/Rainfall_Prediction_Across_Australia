import streamlit as st
import pandas as pd
import pickle
import json
import numpy as np

# =========================
# Load model & column info
# =========================
@st.cache_resource
def load_model_files():
    try:
        with open('xgboost_best_model.pkl', 'rb') as f:
            model = pickle.load(f)

        with open('list_num_cols.txt', 'r') as f:
            list_num_cols = json.load(f)

        with open('list_cat_cols.txt', 'r') as f:
            list_cat_cols = json.load(f)

        return model, list_num_cols, list_cat_cols
    except Exception as e:
        st.error(f"Error loading model files: {e}")
        return None, None, None


# =========================
# Streamlit UI
# =========================
def run():
    st.title("Rain Prediction Across Australia")

     # Display image
    st.image(
        "https://live-production.wcms.abc-cdn.net.au/1fb3cca924190c06a8ad3865b14e81d1?impolicy=wcms_crop_resize&cropH=1080&cropW=1920&xPos=0&yPos=0&width=862&height=485",
        caption="Source: ABC News Australia"
    )

    st.markdown("### Predict whether it will rain tomorrow based on today's weather conditions.")
    
    model, list_num_cols, list_cat_cols = load_model_files()
    if model is None:
        return

    # Default values for form
    default_values = {
        'MinTemp': 12.0, 'MaxTemp': 24.0, 'Rainfall': 2.0, 'Evaporation': 5.0,
        'Sunshine': 7.5, 'WindGustSpeed': 35.0, 'WindSpeed9am': 15.0, 'WindSpeed3pm': 20.0,
        'Humidity9am': 65.0, 'Humidity3pm': 50.0, 'Pressure9am': 1015.0, 'Pressure3pm': 1010.0,
        'Cloud9am': 4.0, 'Cloud3pm': 5.0, 'Temp9am': 18.0, 'Temp3pm': 23.0,
        'Location': 'Sydney', 'WindGustDir': 'NW', 'WindDir9am': 'N', 'WindDir3pm': 'SE',
        'RainToday': 'No'
    }

    with st.form(key='rain_form'):
        st.subheader("Input Today's Weather Data")

        num_data = {col: st.number_input(col, value=float(default_values[col])) for col in list_num_cols}
        cat_data = {col: st.text_input(col, value=default_values[col]) for col in list_cat_cols}

        submit = st.form_submit_button("Predict Rain Tomorrow")

    if submit:
        try:
            # Gabung input user jadi DataFrame mentah
            data_inf = {**num_data, **cat_data}
            data_inf = pd.DataFrame([data_inf])

            st.markdown("### Input Data")
            st.dataframe(data_inf)

            # Langsung prediksi tanpa transformasi tambahan
            y_pred = model.predict(data_inf)
            y_pred_label = "Yes" if y_pred[0] == 1 else "No"

            st.markdown("## Rain Prediction Result")
            st.success(f"Will it rain tomorrow? **{y_pred_label}**")

        except Exception as e:
            st.error(f"Error predicting: {e}")


if __name__ == "__main__":
    run()



