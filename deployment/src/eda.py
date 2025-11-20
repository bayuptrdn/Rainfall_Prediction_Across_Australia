import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    # ===============================
    # Title Section
    # ===============================
    st.title("Rain Prediction Across Australia Data Exploration")

    # Display image
    st.image(
        "https://live-production.wcms.abc-cdn.net.au/1fb3cca924190c06a8ad3865b14e81d1?impolicy=wcms_crop_resize&cropH=1080&cropW=1920&xPos=0&yPos=0&width=862&height=485",
        caption="Source: ABC News Australia"
    )

    # Header
    st.markdown("## Project Background")

    # Markdown Description
    st.markdown("""
    Rain prediction plays a crucial role in **meteorology, agriculture, transportation, and disaster management**.  
    This project aims to **predict the likelihood of rain on the next day (`RainTomorrow`)** across Australia 
    based on today’s weather conditions using a **Machine Learning Classification approach**.

    By developing this predictive system, the project seeks to assist **weather institutions and the public** 
    in making data-driven decisions — such as planning daily activities, managing agricultural operations, 
    or issuing early warnings for extreme weather events.

    The dataset used in this project is the **Weather Dataset in Australia**, available on Kaggle:  
    [Rain in Australia – Kaggle](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)

    The dataset contains **over 145,000 daily weather observations** collected over 10 years from multiple 
    meteorological stations across Australia, providing valuable insights into patterns of rainfall, temperature, 
    humidity, and wind conditions.
    """)

    # ===============================
    # Dataset Loading
    # ===============================
    st.header("Dataset Overview")

    df = pd.read_csv("weatherAUS.csv")

    st.write("Below is a sample of the dataset used for this project:")
    st.dataframe(df.head())

    st.markdown(f"**Dataset Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

    # ===============================
    # EDA 1: Distribution of Numerical Variables
    # ===============================
    st.subheader("EDA 1 — Distribution of Numerical Variables")

    numeric_cols = ['MinTemp','MaxTemp','Rainfall','Humidity9am','Humidity3pm','Temp9am','Temp3pm']
    selected_col = st.selectbox("Select a numeric column to visualize:", numeric_cols)

    fig = px.histogram(df, x=selected_col, nbins=40, marginal="box", color_discrete_sequence=["#1f77b4"])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    **Insight:** The distribution of `{selected_col}` helps us understand its central tendency and spread.  
    For example, temperature variables show a fairly normal distribution, while rainfall is highly right-skewed, 
    indicating that most days have little or no rain.
    """)

    # ===============================
    # EDA 2: Correlation Heatmap
    # ===============================
    st.subheader("EDA 2 — Correlation Between Numerical Features")

    corr = df[numeric_cols].corr()
    fig = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r", title="Correlation Heatmap")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Insight:** There is a strong positive correlation between `MaxTemp` and `Temp3pm`, 
    while rainfall has a moderate correlation with humidity levels.  
    This suggests that temperature and humidity are likely important predictors for rainfall.
    """)

    # ===============================
    # EDA 3: Average Conditions by Location
    # ===============================
    st.subheader("EDA 3 — Average Weather by Location")

    avg_by_loc = df.groupby("Location")[["Rainfall", "Humidity3pm", "Temp3pm"]].mean().reset_index()
    fig = px.bar(avg_by_loc.sort_values("Rainfall", ascending=False).head(10),
                 x="Location", y="Rainfall", color="Rainfall",
                 title="Top 10 Locations with Highest Average Rainfall",
                 color_continuous_scale="Blues")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Insight:** Certain coastal or tropical areas tend to experience higher rainfall, 
    while inland regions are generally drier.  
    This confirms the geographic diversity of Australia’s climate zones.
    """)

    # ===============================
    # EDA 4: Target Variable Distribution
    # ===============================
    st.subheader("EDA 4 — Distribution of Target: RainTomorrow")

    fig = px.histogram(df, x="RainTomorrow", color="RainTomorrow", text_auto=True,
                       title="RainTomorrow Distribution")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Insight:** The dataset is **imbalanced**, with more ‘No’ values than ‘Yes’.  
    This means most days do not have rain, and handling class imbalance during modeling will be important.
    """)

    # ===============================
    # EDA 5: Time Series Trends
    # ===============================
    st.subheader("EDA 5 — Time Series Trend of Temperature and Rainfall")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df_time = df.groupby("Date")[["Temp3pm", "Rainfall"]].mean().reset_index()

    fig = px.line(df_time, x="Date", y=["Temp3pm", "Rainfall"],
                  title="Average Temperature and Rainfall Over Time")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Insight:**  
    - Afternoon temperature (`Temp3pm`) shows a consistent seasonal cycle, rising and falling yearly.  
    - Rainfall appears more irregular, with occasional spikes — typical of tropical and monsoon influences.
    """)

    # ===============================
    # EDA 6: Wind Direction Distribution
    # ===============================
    st.subheader("EDA 6 — Wind Direction Distribution")

    wind_cols = ["WindGustDir", "WindDir9am", "WindDir3pm"]
    selected_wind = st.selectbox("Choose a wind direction feature:", wind_cols)

    fig = px.histogram(df, x=selected_wind, color=selected_wind,
                       title=f"Distribution of {selected_wind}", color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Insight:**  
    Wind direction is fairly evenly distributed, but certain directions such as `N`, `NW`, and `S` appear more frequently.  
    This variability can influence local weather conditions and rainfall likelihood.
    """)

    # ===============================
    # EDA 7: Relationship Between Temperature and Humidity
    # ===============================
    st.subheader("EDA 7 — Relationship Between Temperature and Humidity")

    fig = px.scatter(df, x="Temp3pm", y="Humidity3pm", color="RainTomorrow",
                     title="Temperature vs Humidity (3pm)",
                     category_orders={'RainTomorrow': ['Yes', 'No']},
                     color_discrete_map={
                         'Yes':'#0D47A1',  # biru tua = Rain (Yes)
                         'No': '#B0BEC5'    # abu muda = No Rain
                        }, opacity=0.7,labels={
                        "Temp3pm": "Temperature at 3pm (°C)",
                        "Humidity3pm": "Humidity at 3pm (%)",
                         "RainTomorrow": "Rain Tomorrow"
                        }
                    )
    fig.update_traces(marker=dict(size=6))
    st.plotly_chart(fig)

    st.markdown("""
    **Insight:**  
    The scatter plot above shows a clear relationship between **temperature and humidity** at 3pm.  
    When humidity is **high (>70%)** and temperature is **relatively low (<25°C)**, rain is more likely to occur the next day (`RainTomorrow = Yes`).  
    On the other hand, **dry and hot conditions** (high temperature, low humidity) are often followed by **no rain**.
    """)

    # ===============================
    # Summary
    # ===============================
    st.header("Final Summary of EDA Insights")
    st.markdown("""
    - Most numerical features show normal or right-skewed distributions.  
    - `MaxTemp`, `Temp3pm`, and `Humidity3pm` are key correlated variables with rainfall.  
    - The target variable `RainTomorrow` is imbalanced, requiring resampling or weighting.  
    - Temperature exhibits strong seasonal cycles, while rainfall is more erratic.  
    - Wind direction varies but may affect local precipitation patterns.  
    - Overall, the data shows **complex non-linear relationships**, confirming the need for machine learning approaches like XGBoost.
    """)

# Run app
if __name__ == '__main__':
    run()