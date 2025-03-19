## `ML-SQLInjection-Detection`  
Check the notebooks [here](https://github.com/snehapriya-bs/ML-SQLInjection-Detection) for detailed code and explanation.

This repository modularizes the code for **SQL Injection Detection** and integrates it with **CI/CD** using **Docker** and **GitHub Actions**.

---

## 🚀 **Local Setup**  

### **1. Clone the repository**  
```bash
git clone https://github.com/snehapriya-bs/MLOps-SQLInjection-Detection.git
```

### **2. Create and Activate Virtual Environment**  
```bash
python -m venv sqlinjection
sqlinjection\Scripts\activate
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Add Training Data**  
Place **SqlInjection.csv** in the root directory.  

### **5. Train the Model**  
Delete existing models if they exist:  
```bash
Remove-Item -Path "model.pkl", "vectorizer.pkl" -ErrorAction SilentlyContinue
python train.py
```

### **6. Start FastAPI Server**  
```bash
python main.py
```

### **7. Test the Model**  
```bash
curl -X POST "http://localhost:8000/predict/" -F "file=@test_data.csv"
```

---

## 🛠️ **CI/CD Setup**  
- **Docker**: Dockerfile provided for containerization.  
- **GitHub Actions**: Automates Docker Build.
- **GCP Cloud Run**: Used for Inference
  
## ✅ **Setup Steps for Cloud Run**  

### **1. Create a Service Account in GCP**  
1. Go to **IAM & Admin → Service Accounts** in GCP.  
2. Create a new Service Account with the following roles:  
   - **Cloud Run Admin**  
   - **Artifact Registry Writer**  
3. Generate a key for the Service Account (in JSON format).  

---

### **2. Add GitHub Secrets**  
- **GCP_SA_KEY** → Upload the Service Account key (JSON) as a GitHub secret.  
- **GCP_PROJECT_ID** → Add your GCP project ID as a GitHub secret.  

---

## 🚀 **How It Works**  
✔️ Pulls existing Docker image from **Docker Hub**  
✔️ Tags and pushes it to **Google Artifact Registry**  
✔️ Deploys the image to **Cloud Run**  
✔️ Tests the `/predict/` endpoint using `curl`  

---

## 🌟 **Deployment Status**  
The deployment status can be monitored under **Actions → Cloud Run Deployment** in GitHub.  

---

## 📂 **Structure**  
```
├── app
│   ├── model.py
│   ├── prediction.py
│   ├── routes.py
├── main.py
├── requirements.txt
├── SqlInjection.csv
├── test_data.csv
├── train.py
└── Dockerfile
```

---

## 🚨 **Disclaimer**  
This is a **prototype** model designed to detect SQL Injection. While it performs well on available data, performance can be improved with:  
- **Larger datasets** – More diverse examples of SQL injection queries.  
- **Feature engineering** – Improve vectorization and embeddings.  
- **Hyperparameter tuning** – Optimize classifiers and stacking settings.  
- **Data augmentation** – Generate more variations of known SQL injection patterns.  

---

## 💡 **Optimization Techniques**  
✅ **TF-IDF Adjustments** – Experiment with `ngram_range`, `max_features`, and `stop_words`.  
✅ **Class Balancing** – Try oversampling and undersampling techniques like SMOTE or ADASYN.  
✅ **Model Calibration** – Use `CalibratedClassifierCV` to improve probability estimates.  
✅ **Dropout and Regularization** – Add regularization to reduce overfitting.  
✅ **Cross-Validation** – Use `KFold` or `StratifiedKFold` to improve training consistency.  

---

## 🤝 **Contributing**  
Feel free to open a PR or raise an issue! 😊  

---
