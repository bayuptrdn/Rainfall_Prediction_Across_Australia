# Rain Prediction in Australia (Milestone 2)

## Repository Outline
1. **README.md** – Penjelasan umum project dan dokumentasi hasil analisis.  
2. **P1M2_Bayu_Putradana.ipynb** – Notebook utama berisi tahapan data preprocessing, eksplorasi data (EDA), feature engineering, model training, cross validation, dan hyperparameter tuning.  
3. **P1M2_Bayu_Putradana.inf.ipynb** – Notebook untuk melakukan prediksi data cuaca menggunakan model terbaik (XG Boost).  
4. **xgboost_best_model.pkl** – File hasil penyimpanan model XGBoost terbaik setelah tuning.  
5. **preprocessor.pkk** - File hasil penyimpanan data yang sudah dilakukan preprocessing di Feature Engineering.
6. **list_cat_cols.txt** - List data bertipe kategorikal.
7. **list_num_cols.txt** - List data bertipe numerik.
8. **P1M2_Bayu_Putradana_conceptual.txt** - Jawaban pertanyaan konseptual di Milestone 2
9. **eda.py** - Berisi kode python untuk menampilkan Exploratory Data Analysis di Model Deployment menggunakan Streamlit.
10. **prediction.py** - Berisi kode python untuk menampilkan Model Prediksi Cuaca di Model Deployment menggunakan Streamlit.
11. **streamlit_app.py** - Berisi kode python untuk menggabungkan **eda.py** dan **prediction.py** ke dalam 1 navigasi.
12. **requirements.txt** - Berisi library yang dibutuhkan untuk dapat mengakses model deployment dengan baik.


---

## Problem Background
Prediksi hujan merupakan permasalahan penting dalam meteorologi karena berdampak besar terhadap **aktivitas pertanian, transportasi, hingga mitigasi bencana**.  
Proyek ini bertujuan untuk **memprediksi kemungkinan hujan keesokan harinya (`RainTomorrow`)** di Australia berdasarkan kondisi cuaca hari ini menggunakan pendekatan **Machine Learning (Classification)**.

Melalui sistem ini, diharapkan hasil prediksi dapat membantu **lembaga cuaca dan masyarakat umum** dalam pengambilan keputusan berbasis data, seperti perencanaan aktivitas harian, distribusi pertanian, atau peringatan dini cuaca ekstrem.

---

## Project Output
- Model Machine Learning berbasis **XGBoost** dengan performa terbaik untuk memprediksi `RainTomorrow (Yes/No)`.  
- Notebook inference untuk prediksi otomatis data baru. 
- Model deployment yang dapat diakses di : https://deploymentmilestone2bayuputradanahacktiv8.streamlit.app
- Visualisasi tren cuaca, distribusi fitur, korelasi, serta evaluasi model.  
- File model tersimpan dalam format `.pkl` yang siap digunakan untuk deployment.

---

## Data
- **Sumber:** [Rain in Australia – Kaggle](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)  
- **Deskripsi Singkat:**
  - Jumlah baris: ±145.460  
  - Jumlah kolom: 23  
  - Target: `RainTomorrow` (Yes/No)  
  - Fitur mencakup suhu maksimum & minimum, tekanan udara, kelembapan, curah hujan, kecepatan & arah angin, serta kondisi visual lainnya.  
  - **Missing values** ditangani dengan *median/mode imputation*.  
  - **Outlier** dikendalikan menggunakan *winsorization*.  
  - Dataset di-*resample* sebesar **10%** untuk efisiensi pemrosesan tanpa kehilangan representasi pola utama.

---

## Exploratory Data Analysis (EDA) Summary
Beberapa temuan penting dari hasil EDA antara lain:

- **Distribusi Target:** Data cukup seimbang, namun sedikit lebih banyak hari tanpa hujan (*No RainTomorrow*).  
- **Tren Waktu:** Suhu sore (`Temp3pm`) menunjukkan pola musiman yang konsisten tiap tahun, sedangkan curah hujan lebih fluktuatif dan tidak memiliki pola tetap.  
- **Kelembapan:** Hari-hari dengan hujan memiliki nilai kelembapan lebih tinggi, terutama pada sore hari.  
- **Tekanan Udara:** Tekanan rendah pada pagi dan sore hari memiliki hubungan kuat dengan kemungkinan hujan esok harinya.  
- **Korelasi Fitur:** Fitur kelembapan, tekanan, dan curah hujan memiliki pengaruh paling besar terhadap `RainTomorrow`.

Kesimpulan utama EDA menunjukkan bahwa **hubungan antarvariabel cuaca sangat kompleks dan non-linear**, sehingga model berbasis *tree* seperti XGBoost atau ensemble learning lebih tepat digunakan.

---

## Method
Proyek ini menggunakan pendekatan **Supervised Learning – Classification** dengan membandingkan beberapa algoritma berikut:

| Model | Deskripsi Singkat | Performa Utama |
|-------|--------------------|----------------|
| **Decision Tree** | Model dasar berbasis pemisahan aturan (rule-based). | Baseline awal. |
| **Random Forest** | Ensemble dari banyak decision tree untuk mengurangi overfitting. | Peningkatan stabilitas. |
| **K-Nearest Neighbors (KNN)** | Mengklasifikasikan data berdasarkan kedekatan fitur antar sampel. | Sensitif terhadap skala dan noise. |
| **Support Vector Machine (SVM)** | Memaksimalkan margin antar kelas menggunakan hyperplane. | Cukup baik namun lambat pada dataset besar. |
| **XGBoost** | Gradient boosting dengan regularisasi tinggi untuk performa optimal. | Model terbaik. |

Hasil evaluasi menggunakan metrik **Accuracy**, **F1-Score**, dan **ROC-AUC** menunjukkan bahwa model **XGBoost** memberikan hasil terbaik.  
Setelah dilakukan **Cross Validation** dan **Hyperparameter Tuning (GridSearchCV)**, model menunjukkan peningkatan F1-Score dari **0.5969 menjadi 0.6071**, menandakan keseimbangan antara *precision* dan *recall* semakin baik.  

Model akhir XGBoost kemudian disimpan untuk tahap inference dan siap digunakan untuk prediksi data baru.

---

## Stacks
| Kategori | Tools/Library |
|-----------|----------------|
| Bahasa Pemrograman | Python |
| Lingkungan Kerja | Google Colab |
| Library Data | pandas, numpy, matplotlib, seaborn |
| Machine Learning | scikit-learn, xgboost |
| Model Saving | pickle |
| Deployment | Notebook inference via Google Drive |

---

## Reference
- Dataset: [Rain in Australia – Kaggle](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)  
- Dokumentasi XGBoost: https://xgboost.readthedocs.io/  
- Scikit-learn Documentation: https://scikit-learn.org/stable/  
- Pandas Documentation: https://pandas.pydata.org/docs/  
- Artikel referensi: [freeCodeCamp – How to Write a Good README](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)

