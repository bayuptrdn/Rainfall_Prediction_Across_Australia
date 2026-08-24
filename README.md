# Rain Prediction in Australia

### Machine Learning for Next-Day Rainfall Prediction

---

# English Version

## Project Overview

This project develops a **Machine Learning classification model** to predict the probability of rainfall on the following day (`RainTomorrow`) in Australia based on current weather conditions.

Rainfall prediction is an important application of meteorological data analysis, with potential implications for **agriculture, transportation, water resource management, and extreme weather risk mitigation**.

Using a **Supervised Learning – Classification** approach, this project processes historical weather observations to identify patterns associated with next-day rainfall and develops a predictive model suitable for practical application.

---

## Background

Weather conditions can have a significant impact on human activities, infrastructure, and economic operations. Reliable rainfall forecasts can support better planning and help reduce the potential impact of unfavorable weather conditions.

This project focuses on using historical weather data to:

* Identify weather patterns associated with next-day rainfall
* Understand the relationship between meteorological variables and rainfall
* Develop a data-driven rainfall prediction system
* Evaluate different machine learning approaches for classification

---

## Objectives

The main objectives of this project are to:

* Analyze historical weather observations from Australia
* Perform data preprocessing and feature engineering
* Develop and compare multiple Machine Learning classification models
* Apply Cross-Validation and Hyperparameter Tuning
* Select the most suitable model based on evaluation metrics
* Provide an inference pipeline and web-based prediction interface

---

## Dataset

### Source

**Rain in Australia Dataset**

The dataset is available on Kaggle:

[Rain in Australia Dataset](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)

### Dataset Description

The dataset contains historical daily weather observations collected from multiple locations across Australia.

Key characteristics include:

* Approximately **145,460 records**
* **23 variables**
* Target variable: `RainTomorrow` (`Yes` / `No`)

Key features include:

* Maximum and minimum temperature
* Atmospheric pressure
* Humidity
* Rainfall
* Wind speed and direction
* Other weather-related observations

### Data Preprocessing

Several preprocessing techniques are applied to prepare the dataset for modeling:

* Missing values are handled using **median and mode imputation**
* Outliers are controlled using **winsorization**
* The dataset is resampled to **10% of the original data** to improve computational efficiency while retaining the primary patterns within the dataset

---

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) is conducted to understand the distribution of the target variable and identify relationships between weather conditions and next-day rainfall.

### Key Insights

Several notable patterns were identified:

* The target variable is relatively imbalanced, with non-rainy days occurring more frequently than rainy days
* **Afternoon humidity** shows a strong relationship with rainfall on the following day
* **Lower atmospheric pressure** is associated with a higher likelihood of rainfall
* Relationships between weather variables and rainfall are often **non-linear**

These findings support the use of **tree-based ensemble and boosting algorithms**, which are capable of capturing complex and non-linear relationships between features.

---

## Machine Learning Methodology

The prediction task is formulated as a **Supervised Learning – Binary Classification** problem.

Several machine learning algorithms are evaluated:

| Model                            | Description                                                                                                |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Decision Tree**                | A rule-based classification model used as a baseline                                                       |
| **Random Forest**                | An ensemble of decision trees designed to improve generalization and reduce overfitting                    |
| **K-Nearest Neighbors (KNN)**    | A distance-based classification algorithm                                                                  |
| **Support Vector Machine (SVM)** | A classification algorithm that separates classes using an optimal decision boundary                       |
| **XGBoost**                      | A gradient boosting algorithm designed to capture complex patterns with strong regularization capabilities |

---

## Model Evaluation

Model performance is evaluated using several classification metrics:

* **Accuracy**
* **F1-Score**
* **ROC-AUC**

The modeling workflow includes:

1. Baseline model development
2. Cross-Validation
3. Hyperparameter Tuning using `GridSearchCV`
4. Model comparison
5. Selection of the best-performing model

### Best Model

**XGBoost** was selected as the best-performing model based on the evaluation results.

After hyperparameter tuning, the F1-Score improved from:

```text
Baseline F1-Score : 0.5969
Tuned F1-Score    : 0.6071
```

The improvement indicates better balance between **precision and recall**, which is particularly relevant for rainfall prediction where correctly identifying rainy days is important.

---

## Deployment

The trained model is deployed as an interactive **web application using Streamlit**.

### Deployment

[Open the Rain Prediction Application](https://deploymentmilestone2bayuputradanahacktiv8.streamlit.app)

The application provides users with the ability to:

* Explore selected EDA results
* Input new weather conditions
* Generate next-day rainfall predictions

The deployment demonstrates how a trained Machine Learning model can be integrated into an accessible web-based prediction interface.

---

## Repository Structure

```text
Rain-Prediction-in-Australia/
│
├── README.md
├── P1M2_Bayu_Putradana.ipynb
├── P1M2_Bayu_Putradana.inf.ipynb
│
├── xgboost_best_model.pkl
├── preprocessor.pkl
│
├── list_cat_cols.txt
├── list_num_cols.txt
│
├── P1M2_Bayu_Putradana_conceptual.txt
│
├── eda.py
├── prediction.py
├── streamlit_app.py
│
└── requirements.txt
```

---

## Technology Stack

| Category                 | Tools / Libraries     |
| ------------------------ | --------------------- |
| **Programming Language** | Python                |
| **Data Processing**      | pandas, NumPy         |
| **Data Visualization**   | Matplotlib, Seaborn   |
| **Machine Learning**     | scikit-learn, XGBoost |
| **Model Serialization**  | Pickle                |
| **Deployment**           | Streamlit             |

---

## Conclusion

This project demonstrates the application of Machine Learning to a real-world weather prediction problem using historical meteorological observations.

The analysis indicates that rainfall prediction involves complex and non-linear relationships among weather variables. Ensemble-based approaches, particularly **XGBoost**, provide a suitable solution for capturing these patterns.

The final model achieved an improved **F1-Score of 0.6071** after hyperparameter tuning, demonstrating better balance between precision and recall compared with the baseline model.

The trained model has also been integrated into a **Streamlit web application**, providing an accessible interface for generating rainfall predictions from new weather observations.

---

## Author

**Bayu Putradana**
Data Analyst | Machine Learning Enthusiast

---

## References

* **Dataset:** [Rain in Australia Dataset – Kaggle](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)
* **Scikit-learn Documentation:** https://scikit-learn.org/
* **XGBoost Documentation:** https://xgboost.readthedocs.io/
* **Streamlit Documentation:** https://docs.streamlit.io/

---

# Versi Bahasa Indonesia

## Gambaran Umum Proyek

Proyek ini mengembangkan **model Machine Learning berbasis klasifikasi** untuk memprediksi kemungkinan terjadinya hujan pada hari berikutnya (`RainTomorrow`) di Australia berdasarkan kondisi cuaca pada hari sebelumnya.

Prediksi curah hujan merupakan salah satu penerapan penting dalam analisis data meteorologi karena dapat memberikan manfaat bagi berbagai sektor, termasuk **pertanian, transportasi, pengelolaan sumber daya air, serta mitigasi risiko cuaca ekstrem**.

Dengan menggunakan pendekatan **Supervised Learning – Classification**, proyek ini memanfaatkan data cuaca historis untuk mengidentifikasi pola yang berkaitan dengan kemungkinan hujan pada hari berikutnya dan menghasilkan model prediktif yang dapat diterapkan dalam konteks praktis.

---

## Latar Belakang

Kondisi cuaca dapat memberikan dampak yang signifikan terhadap aktivitas manusia, infrastruktur, dan kegiatan ekonomi. Prediksi hujan yang lebih baik dapat membantu proses perencanaan dan mengurangi potensi dampak dari kondisi cuaca yang tidak menguntungkan.

Proyek ini memanfaatkan data historis cuaca untuk:

* Mengidentifikasi pola cuaca yang berkaitan dengan hujan pada hari berikutnya
* Memahami hubungan antara variabel meteorologi dan kejadian hujan
* Mengembangkan sistem prediksi hujan berbasis data
* Membandingkan berbagai pendekatan Machine Learning untuk permasalahan klasifikasi

---

## Tujuan

Tujuan utama dari proyek ini adalah:

* Menganalisis data historis cuaca dari berbagai wilayah di Australia
* Melakukan preprocessing dan feature engineering terhadap data
* Mengembangkan dan membandingkan beberapa model Machine Learning
* Menerapkan Cross-Validation dan Hyperparameter Tuning
* Memilih model yang paling sesuai berdasarkan metrik evaluasi
* Menyediakan pipeline inference dan antarmuka prediksi berbasis web

---

## Dataset

### Sumber Data

**Rain in Australia Dataset**

Dataset tersedia melalui Kaggle:

[Rain in Australia Dataset](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)

### Deskripsi Dataset

Dataset berisi observasi cuaca harian historis yang dikumpulkan dari berbagai lokasi di Australia.

Karakteristik utama dataset meliputi:

* Sekitar **145.460 baris data**
* **23 variabel**
* Target variable: `RainTomorrow` (`Yes` / `No`)

Beberapa fitur utama yang tersedia antara lain:

* Suhu maksimum dan minimum
* Tekanan udara
* Kelembapan
* Curah hujan
* Kecepatan dan arah angin
* Berbagai variabel observasi cuaca lainnya

### Data Preprocessing

Beberapa teknik preprocessing diterapkan untuk mempersiapkan data sebelum digunakan dalam proses pemodelan:

* Missing values ditangani menggunakan **median dan mode imputation**
* Outlier dikendalikan menggunakan metode **winsorization**
* Dataset di-*resample* menjadi **10% dari ukuran data awal** untuk meningkatkan efisiensi komputasi dengan tetap mempertahankan pola utama dalam dataset

---

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) dilakukan untuk memahami distribusi target variable serta mengidentifikasi hubungan antara kondisi cuaca dan kemungkinan hujan pada hari berikutnya.

### Insight Utama

Beberapa pola penting yang ditemukan antara lain:

* Target variable relatif tidak seimbang, dengan jumlah hari tanpa hujan lebih tinggi dibandingkan hari dengan hujan
* **Kelembapan pada sore hari** memiliki hubungan yang kuat dengan kemungkinan hujan pada hari berikutnya
* **Tekanan udara yang lebih rendah** berkaitan dengan probabilitas hujan yang lebih tinggi
* Hubungan antara variabel cuaca dan kejadian hujan cenderung bersifat **non-linear**

Temuan tersebut mendukung penggunaan algoritma **ensemble berbasis decision tree dan boosting**, yang mampu menangkap hubungan kompleks dan non-linear antarvariabel.

---

## Metodologi Machine Learning

Permasalahan prediksi diformulasikan sebagai **Supervised Learning – Binary Classification**.

Beberapa algoritma Machine Learning yang dibandingkan meliputi:

| Model                            | Deskripsi                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Decision Tree**                | Model klasifikasi berbasis aturan yang digunakan sebagai baseline                                      |
| **Random Forest**                | Ensemble dari beberapa decision tree untuk meningkatkan generalisasi dan mengurangi overfitting        |
| **K-Nearest Neighbors (KNN)**    | Algoritma klasifikasi berbasis jarak antarobservasi                                                    |
| **Support Vector Machine (SVM)** | Algoritma klasifikasi yang mencari decision boundary optimal untuk memisahkan kelas                    |
| **XGBoost**                      | Algoritma gradient boosting yang mampu menangkap pola kompleks dengan kemampuan regularisasi yang kuat |

---

## Evaluasi Model

Performa model dievaluasi menggunakan beberapa metrik klasifikasi:

* **Accuracy**
* **F1-Score**
* **ROC-AUC**

Workflow pemodelan meliputi:

1. Pengembangan baseline model
2. Cross-Validation
3. Hyperparameter Tuning menggunakan `GridSearchCV`
4. Perbandingan performa model
5. Pemilihan model terbaik

### Model Terbaik

**XGBoost** dipilih sebagai model dengan performa terbaik berdasarkan hasil evaluasi.

Setelah proses hyperparameter tuning, F1-Score meningkat dari:

```text
Baseline F1-Score : 0.5969
Tuned F1-Score    : 0.6071
```

Peningkatan tersebut menunjukkan keseimbangan **precision dan recall** yang lebih baik dibandingkan model baseline. Hal ini penting dalam konteks prediksi hujan karena kemampuan mengidentifikasi hari yang berpotensi mengalami hujan merupakan salah satu aspek utama dalam sistem prediksi.

---

## Deployment

Model yang telah dilatih diimplementasikan sebagai **web application menggunakan Streamlit**.

### Deployment

[Open the Rain Prediction Application](https://deploymentmilestone2bayuputradanahacktiv8.streamlit.app)

Aplikasi memungkinkan pengguna untuk:

* Melihat hasil analisis EDA
* Memasukkan kondisi cuaca baru
* Menghasilkan prediksi hujan pada hari berikutnya

Deployment ini menunjukkan bagaimana model Machine Learning yang telah dilatih dapat diintegrasikan ke dalam aplikasi berbasis web sehingga dapat digunakan melalui antarmuka yang lebih mudah diakses.

---

## Struktur Repository

```text
Rain-Prediction-in-Australia/
│
├── README.md
├── P1M2_Bayu_Putradana.ipynb
├── P1M2_Bayu_Putradana.inf.ipynb
│
├── xgboost_best_model.pkl
├── preprocessor.pkl
│
├── list_cat_cols.txt
├── list_num_cols.txt
│
├── P1M2_Bayu_Putradana_conceptual.txt
│
├── eda.py
├── prediction.py
├── streamlit_app.py
│
└── requirements.txt
```

---

## Technology Stack

| Kategori                | Tools / Library       |
| ----------------------- | --------------------- |
| **Bahasa Pemrograman**  | Python                |
| **Data Processing**     | pandas, NumPy         |
| **Data Visualization**  | Matplotlib, Seaborn   |
| **Machine Learning**    | scikit-learn, XGBoost |
| **Model Serialization** | Pickle                |
| **Deployment**          | Streamlit             |

---

## Kesimpulan

Proyek ini menunjukkan penerapan Machine Learning pada permasalahan prediksi cuaca menggunakan data meteorologi historis.

Hasil analisis menunjukkan bahwa prediksi hujan melibatkan hubungan yang kompleks dan non-linear antarvariabel cuaca. Pendekatan berbasis ensemble, khususnya **XGBoost**, mampu menjadi solusi yang sesuai untuk menangkap pola tersebut.

Model akhir menghasilkan peningkatan **F1-Score menjadi 0.6071** setelah proses hyperparameter tuning, yang menunjukkan keseimbangan precision dan recall yang lebih baik dibandingkan baseline model.

Model yang telah dilatih juga telah diintegrasikan ke dalam **aplikasi web berbasis Streamlit**, sehingga pengguna dapat melakukan prediksi hujan berdasarkan kondisi cuaca baru melalui antarmuka yang interaktif.

---

## Author

**Bayu Putradana**
Data Analyst | Machine Learning Enthusiast

---

## Referensi

* **Dataset:** [Rain in Australia Dataset – Kaggle](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)
* **Scikit-learn Documentation:** https://scikit-learn.org/
* **XGBoost Documentation:** https://xgboost.readthedocs.io/
* **Streamlit Documentation:** https://docs.streamlit.io/

- Rain in Australia Dataset – Kaggle  
- Dokumentasi XGBoost: https://xgboost.readthedocs.io/  
- Scikit-learn Documentation: https://scikit-learn.org/stable/  
- Pandas Documentation: https://pandas.pydata.org/docs/  

