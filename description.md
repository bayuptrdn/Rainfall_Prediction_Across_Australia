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

* `RainTomorrow = Yes` — Rain is expected tomorrow
* `RainTomorrow = No` — Rain is not expected tomorrow

The resulting model is designed to demonstrate how historical weather data can be transformed into predictive insights using Machine Learning.

---

## Project Objectives

The main objectives of this project are to:

* Analyze historical weather conditions across Australia
* Identify weather patterns associated with next-day rainfall
* Perform data preprocessing and feature engineering
* Develop and compare multiple classification algorithms
* Evaluate model performance using appropriate classification metrics
* Apply cross-validation and hyperparameter optimization
* Select and save the best-performing model for inference
* Provide an interactive interface for weather exploration and prediction

---

## Project Outputs

The project produces several outputs, including:

* A trained **XGBoost classification model** for predicting `RainTomorrow`
* A preprocessing pipeline used to transform input data consistently
* An inference notebook for generating predictions from new weather data
* An interactive Streamlit application for weather analysis and prediction
* Exploratory data visualizations and model evaluation results
* A serialized `.pkl` model ready to be integrated into an application

### Live Application

The trained model is also available through an interactive web application:

**[Rain Prediction in Australia – Streamlit Application](https://rainfallpredictionacrossaustralia-ab3apdumhqvuwcxxuwappkh.streamlit.app)**

The application provides functionality for:

* Exploring weather-related visualizations
* Reviewing key patterns in the dataset
* Entering weather conditions
* Generating next-day rainfall predictions

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
```

---

# Versi Bahasa Indonesia

## Gambaran Umum Proyek

**Rain Prediction in Australia** merupakan proyek **Machine Learning** yang berfokus pada prediksi apakah hujan akan terjadi pada hari berikutnya (`RainTomorrow`) berdasarkan kondisi cuaca saat ini dan historis di berbagai wilayah Australia.

Prediksi hujan merupakan salah satu penerapan penting dalam analisis data cuaca yang memiliki potensi manfaat di berbagai sektor, seperti pertanian, transportasi, pengelolaan sumber daya air, serta kesiapsiagaan terhadap kondisi cuaca ekstrem.

Proyek ini menerapkan alur kerja **Supervised Learning – Classification** secara terstruktur, yang mencakup data preprocessing, exploratory data analysis, feature engineering, pengembangan model, evaluasi, optimasi, hingga inference.

---

## Latar Belakang Permasalahan

Prediksi hujan yang akurat dapat mendukung pengambilan keputusan yang lebih baik di berbagai sektor. Perubahan kondisi cuaca dapat memberikan dampak langsung terhadap aktivitas pertanian, transportasi, kegiatan operasional di luar ruangan, pengelolaan sumber daya air, serta keselamatan masyarakat.

Tujuan utama proyek ini adalah mengembangkan model klasifikasi yang mampu memperkirakan kemungkinan terjadinya hujan pada hari berikutnya berdasarkan kondisi cuaca yang tersedia.

Target prediksi yang digunakan adalah:

* `RainTomorrow = Yes` — Diprediksi akan terjadi hujan pada hari berikutnya
* `RainTomorrow = No` — Diprediksi tidak akan terjadi hujan pada hari berikutnya

Model yang dihasilkan dirancang untuk menunjukkan bagaimana data historis cuaca dapat diolah menjadi insight prediktif menggunakan Machine Learning.

---

## Tujuan Proyek

Tujuan utama proyek ini adalah untuk:

* Menganalisis kondisi cuaca historis di berbagai wilayah Australia
* Mengidentifikasi pola cuaca yang berkaitan dengan kemungkinan hujan pada hari berikutnya
* Melakukan data preprocessing dan feature engineering
* Mengembangkan dan membandingkan beberapa algoritma klasifikasi
* Mengevaluasi performa model menggunakan metrik klasifikasi yang sesuai
* Menerapkan cross-validation dan hyperparameter optimization
* Memilih dan menyimpan model dengan performa terbaik untuk inference
* Menyediakan antarmuka interaktif untuk eksplorasi cuaca dan prediksi

---

## Output Proyek

Proyek ini menghasilkan beberapa output, antara lain:

* Model klasifikasi **XGBoost** yang telah dilatih untuk memprediksi `RainTomorrow`
* Preprocessing pipeline yang digunakan untuk mentransformasi data input secara konsisten
* Inference notebook untuk menghasilkan prediksi berdasarkan data cuaca baru
* Aplikasi interaktif berbasis Streamlit untuk analisis dan prediksi cuaca
* Visualisasi exploratory data analysis dan hasil evaluasi model
* Model dalam format `.pkl` yang telah diserialisasi dan siap diintegrasikan ke dalam aplikasi

### Aplikasi Live

Model yang telah dilatih juga tersedia melalui aplikasi web interaktif:

**[Rain Prediction in Australia – Streamlit Application](https://rainfallpredictionacrossaustralia-ab3apdumhqvuwcxxuwappkh.streamlit.app)**

Aplikasi ini menyediakan beberapa fungsi, antara lain:

* Mengeksplorasi visualisasi yang berkaitan dengan kondisi cuaca
* Melihat pola-pola utama yang terdapat dalam dataset
* Memasukkan kondisi cuaca
* Menghasilkan prediksi hujan pada hari berikutnya

---

## Struktur Repository

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
```

