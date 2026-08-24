# Rain Prediction in Australia
## Machine Learning for Next-Day Rainfall Prediction

---

# English Version

## Project Overview

**Rain Prediction in Australia** is a Machine Learning project focused on predicting whether rainfall will occur on the following day (`RainTomorrow`) based on current and historical weather conditions across Australia.

Rainfall prediction is an important application of weather analytics, with potential relevance to agriculture, transportation, water resource management, and extreme weather preparedness.

This project applies a structured **Supervised Learning – Classification** workflow, covering data preprocessing, exploratory data analysis, feature engineering, model development, evaluation, optimization, and inference.

---

## Problem Background

Accurate rainfall prediction can support better decision-making across various sectors. Changes in weather conditions can directly affect agricultural activities, transportation, outdoor operations, water management, and public safety.

The primary objective of this project is to develop a classification model capable of estimating the probability of rainfall on the following day based on available weather conditions.

The prediction target is:

- `RainTomorrow = Yes` — Rain is expected tomorrow
- `RainTomorrow = No` — Rain is not expected tomorrow

The resulting model is designed to demonstrate how historical weather data can be transformed into predictive insights using Machine Learning.

---

## Project Objectives

The main objectives of this project are to:

- Analyze historical weather conditions across Australia
- Identify weather patterns associated with next-day rainfall
- Perform data preprocessing and feature engineering
- Develop and compare multiple classification algorithms
- Evaluate model performance using appropriate classification metrics
- Apply cross-validation and hyperparameter optimization
- Select and save the best-performing model for inference
- Provide an interactive interface for weather exploration and prediction

---

## Project Outputs

The project produces several outputs, including:

- A trained **XGBoost classification model** for predicting `RainTomorrow`
- A preprocessing pipeline used to transform input data consistently
- An inference notebook for generating predictions from new weather data
- An interactive Streamlit application for weather analysis and prediction
- Exploratory data visualizations and model evaluation results
- A serialized `.pkl` model ready to be integrated into an application

### Live Application

The trained model is also available through an interactive web application:

**[Rain Prediction in Australia – Streamlit Application](https://deploymentmilestone2bayuputradanahacktiv8.streamlit.app)**

The application provides functionality for:

- Exploring weather-related visualizations
- Reviewing key patterns in the dataset
- Entering weather conditions
- Generating next-day rainfall predictions

---

## Repository Structure

```text
Rain-Prediction-in-Australia/
│
├── README.md
├── description.md
├── P1M2_Bayu_Putradana.ipynb
├── P1M2_Bayu_Putradana.inf.ipynb
├── xgboost_best_model.pkl
├── preprocessor.pkl
├── list_cat_cols.txt
├── list_num_cols.txt
├── eda.py
├── prediction.py
├── streamlit_app.py
└── requirements.txt
