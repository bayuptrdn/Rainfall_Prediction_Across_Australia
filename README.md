# Rain Prediction in Australia

## Gambaran Umum Proyek

Proyek ini bertujuan untuk membangun **model Machine Learning** yang mampu memprediksi **kemungkinan terjadinya hujan pada hari berikutnya (`RainTomorrow`) di Australia** berdasarkan kondisi cuaca hari ini.

Prediksi hujan merupakan permasalahan penting dalam bidang meteorologi karena berdampak langsung terhadap **pertanian, transportasi, manajemen sumber daya air, serta mitigasi bencana cuaca ekstrem**. Dengan pendekatan **Supervised Learning (Classification)**, proyek ini mengolah data cuaca historis untuk menghasilkan sistem prediksi yang akurat dan siap digunakan.

---

## Latar Belakang Masalah

Cuaca ekstrem, khususnya hujan, memiliki dampak signifikan terhadap aktivitas manusia. Keterlambatan atau ketidakakuratan prediksi hujan dapat menyebabkan kerugian ekonomi maupun risiko keselamatan.

Proyek ini dikembangkan untuk:
- Membantu proses **pengambilan keputusan berbasis data**
- Mengidentifikasi pola cuaca yang berpengaruh terhadap hujan
- Menyediakan sistem prediksi otomatis yang dapat digunakan oleh masyarakat maupun institusi terkait

---

## Tujuan Proyek

Tujuan utama dari proyek ini adalah:

- Menganalisis data cuaca historis Australia
- Melakukan preprocessing dan feature engineering untuk data cuaca
- Membangun dan membandingkan beberapa model Machine Learning
- Melakukan **Cross Validation** dan **Hyperparameter Tuning**
- Memilih model terbaik berdasarkan metrik evaluasi
- Menyediakan **model inference** dan **deployment berbasis web**

---

## Data

### Sumber Dataset
- **Rain in Australia Dataset**
- Sumber: Kaggle  
  https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package

### Deskripsi Dataset
- Jumlah baris: ±145.460
- Jumlah kolom: 23
- Target: `RainTomorrow` (Yes / No)
- Fitur utama:
  - Suhu maksimum & minimum
  - Tekanan udara
  - Kelembapan
  - Curah hujan
  - Kecepatan & arah angin
  - Kondisi visual cuaca

### Penanganan Data
- Missing values ditangani menggunakan **median / mode imputation**
- Outlier dikendalikan dengan **winsorization**
- Dataset di-*resample* sebesar **10%** untuk efisiensi komputasi tanpa kehilangan pola utama

---

## Exploratory Data Analysis (EDA) – Ringkasan Insight

Beberapa temuan utama dari EDA antara lain:

- Distribusi target relatif seimbang, dengan dominasi hari tanpa hujan
- Nilai **kelembapan sore hari** memiliki korelasi kuat dengan hujan esok hari
- **Tekanan udara rendah** berkaitan erat dengan probabilitas hujan
- Hubungan antar fitur bersifat **non-linear**, sehingga model berbasis ensemble lebih sesuai

Insight ini menjadi dasar pemilihan model Machine Learning berbasis *tree* dan *boosting*.

---

## Metodologi

Proyek ini menggunakan pendekatan **Supervised Learning – Classification** dengan perbandingan beberapa algoritma berikut:

| Model | Deskripsi |
|------|----------|
| Decision Tree | Model dasar berbasis aturan |
| Random Forest | Ensemble untuk mengurangi overfitting |
| K-Nearest Neighbors (KNN) | Klasifikasi berbasis jarak |
| Support Vector Machine (SVM) | Pemisahan kelas dengan hyperplane |
| XGBoost | Gradient Boosting dengan regularisasi tinggi |

### Evaluasi Model
- Metrics: **Accuracy, F1-Score, ROC-AUC**
- Proses:
  - Baseline model
  - Cross Validation
  - Hyperparameter Tuning (GridSearchCV)

**XGBoost** dipilih sebagai model terbaik dengan peningkatan F1-Score dari **0.5969 menjadi 0.6071** setelah tuning, menunjukkan keseimbangan precision dan recall yang lebih baik.

---

## Deployment

Model terbaik telah dideploy dalam bentuk **web application menggunakan Streamlit**.

🔗 **Akses Deployment:**  
https://deploymentmilestone2bayuputradanahacktiv8.streamlit.app

Aplikasi ini memungkinkan pengguna untuk:
- Melihat hasil EDA
- Melakukan prediksi hujan berdasarkan data cuaca baru

---

## Struktur Repository

Rain-Prediction-in-Australia
|
├── README.md
├── P1M2_Bayu_Putradana.ipynb
├── P1M2_Bayu_Putradana.inf.ipynb
├── xgboost_best_model.pkl
├── preprocessor.pkl
├── list_cat_cols.txt
├── list_num_cols.txt
├── P1M2_Bayu_Putradana_conceptual.txt
├── eda.py
├── prediction.py
├── streamlit_app.py
└── requirements.txt


---

## Tech Stack

| Kategori | Tools / Library |
|--------|----------------|
| Bahasa Pemrograman | Python |
| Data Processing | pandas, numpy |
| Visualisasi | matplotlib, seaborn |
| Machine Learning | scikit-learn, xgboost |
| Model Saving | pickle |
| Deployment | Streamlit |

---

## Kesimpulan

Proyek ini menunjukkan bahwa pendekatan **Machine Learning berbasis ensemble**, khususnya **XGBoost**, sangat efektif untuk menangani data cuaca yang kompleks dan non-linear. Model yang dihasilkan mampu memberikan prediksi hujan yang cukup akurat dan siap digunakan dalam konteks nyata melalui web deployment.

---

## Author

**Bayu Putradana**  
Data Analyst | Machine Learning Enthusiast  

---

## Referensi
- Rain in Australia Dataset – Kaggle  
- Dokumentasi XGBoost: https://xgboost.readthedocs.io/  
- Scikit-learn Documentation: https://scikit-learn.org/stable/  
- Pandas Documentation: https://pandas.pydata.org/docs/  

