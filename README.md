
# ❤️ Heart Disease Prediction Using Machine Learning

A machine learning web application that predicts the heart disease class based on selected patient health information. The application uses a trained Support Vector Classifier (SVC) model and a user-friendly Streamlit interface.

## 🚀 Live Demo

**Try the application here:**

👉 [Heart Disease Prediction — Live Demo](https://heart-disease-prediction-dgadjppzrw9wedfgjv8omf.streamlit.app/)

## 📌 Project Overview

This project demonstrates how machine learning can be used to analyze patient health features and generate a prediction. Users can enter patient information through a simple web interface and view the model's output in understandable language.

This project was developed for educational purposes as part of a machine learning assignment.

## ✨ Features

- User-friendly Streamlit web interface
- Patient information input form
- Data preprocessing and model training in Jupyter Notebook
- Support Vector Classifier (SVC) model
- Automated prediction from user inputs
- Clear, easy-to-understand prediction results
- Online deployment using Streamlit Community Cloud

## 🩺 Input Features

The application uses the following features:

| Feature | Description |
|---|---|
| Age | Patient's age in years |
| Chest Pain Type (`cp`) | Chest pain category |
| Cholesterol (`chol`) | Cholesterol measurement |
| Maximum Heart Rate (`thalach`) | Maximum recorded heart rate |

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Git and GitHub

## 📂 Project Structure

```text
heart-disease-prediction/
│
├── app.py
├── Task2_Heart_Disease_Prediction.ipynb
├── heart.csv
├── heart_disease_svc_model.pkl
├── heart_disease_le_cp.pkl
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/heart-disease-prediction.git
```

### 2. Open the project directory

```bash
cd heart-disease-prediction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

## 🧠 Machine Learning Workflow

1. Load the heart disease dataset.
2. Inspect and preprocess the data.
3. Perform exploratory data analysis (EDA).
4. Prepare the features and target variable.
5. Train the Support Vector Classifier (SVC).
6. Evaluate the model's performance.
7. Save the trained model and label encoder.
8. Build the Streamlit interface.
9. Deploy the application online.

## ⚠️ Disclaimer

This application is intended for educational and demonstration purposes only. Its predictions are not a medical diagnosis and should not be used to make treatment decisions. Consult a qualified healthcare professional for medical advice.

## 👨‍💻 Author

Developed as a machine learning project demonstrating data analysis, model training, prediction, and web application deployment.

---

⭐ If you find this project useful, consider giving the repository a star.
