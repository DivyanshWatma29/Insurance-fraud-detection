# Insurance Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) 
![Flask](https://img.shields.io/badge/Framework-Flask-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)

## 📝 Project Overview
Insurance fraud is a significant challenge for the insurance industry, leading to substantial financial losses. This project implements an end-to-end Machine Learning solution to detect fraudulent insurance claims. By analyzing historical claim data and policy parameters, the system predicts whether a new claim is legitimate or potentially fraudulent.

## 🚀 Project Workflow
The project is structured into seven distinct Epics:
- **Epic 1: Problem Understanding:** Defining business requirements and impact.
- **Epic 2: Data Preparation:** Handling missing values, cleaning, and outlier treatment (IQR capping).
- **Epic 3: Exploratory Data Analysis:** Visualizing correlations and data distributions.
- **Epic 4: Model Building:** Training multiple classifiers (KNN, Decision Tree, Random Forest, Logistic Regression, Naïve Bayes, SVM).
- **Epic 5: Performance Evaluation:** Comparing models using accuracy, confusion matrices, and cross-validation.
- **Epic 6: Model Deployment:** Saving the best-performing model (SVM) and integrating it with a Flask web framework.
- **Epic 7: Documentation:** Comprehensive project reporting.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Missingno
- **Web Framework:** Flask (HTML/CSS for Frontend)
- **Model Serialization:** Joblib

## 📊 Model Performance
After extensive testing and cross-validation, the models achieved the following mean accuracies:

| Model | Mean Accuracy |
| :--- | :--- |
| **SVM (Best Model)** | **80.93%** |
| Logistic Regression | 80.40% |
| Random Forest | 77.47% |
| KNN | 72.53% |
| Decision Tree | 70.67% |
| Naïve Bayes | 53.20% |

## 💻 Installation & Usage

### Prerequisites
- Python 3.x
- Pip (Python Package Index)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/insurance-fraud-detection.git
   cd insurance-fraud-detection
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn flask joblib
   ```
3. Run the application:
   ```bash
   python app.py

