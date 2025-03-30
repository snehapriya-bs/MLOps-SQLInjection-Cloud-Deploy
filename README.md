# **MLOps SQL Injection Detector deployed on GCP Cloud Run**
A scalable and serverless deployment for real-time SQL injection detection.

## 🚀 **Project Overview**
This project is an **MLOps pipeline** for **SQL Injection Detection** using **Machine Learning**. The model is trained to detect malicious SQL queries and is deployed on **Google Cloud Run** for real-time predictions.Cloud Run ensures automatic scaling, high availability, and secure API access with minimal operational overhead.

## 📁 **Repository Structure**
```
MLOps-SQLInjection-Detection/
│── data/                     # Dataset and sample SQL queries
│── sql_injection/            # ML model and feature extraction
│── sql_injection_api/        # FastAPI application for inference
│── deployment/               # Contains Requirement file for deployment
│── tests/                    # Unit Tests and Test data
│── Dockerfile                # Docker setup for Cloud Run
│── setup.py                  # Installation script for Build
│── pyproject.toml            # Project dependencies
│── Read.md                   # Project documentation
│── .github/workflows/        # CI/CD GitHub Actions workflows
```

---

## ⚙️ **Setup Instructions**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/snehapriya-bs/MLOps-SQLInjection-Detection.git
cd MLOps-SQLInjection-Detection
```

### **2️⃣ Set Up Virtual Environment & Install Dependencies**
```sh
python -m venv sqlinjection
source sqlinjection/bin/activate  # On macOS/Linux
# sqlinjection\Scripts\activate  # On Windows
pip install -r deployment/requirements.txt 
```

### **3️⃣ Train & Test the Model**
```sh
python sql_injection/train.py
python sql_injection/predict.py
pytest tests/test_predict.py
```

### **4️⃣ Build the Package**
```sh
pip install build
python -m build
mv dist/*.whl .
```

### **5️⃣ Run the Application Locally**
```sh
pip install -r sql_injection_api/requirements.txt
python sql_injection_api/app/main.py 
```
- Access the API docs at: [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)

### **6️⃣ Test with Sample SQL Query**
```sh
curl -X POST "http://localhost:8080/api/v1/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@data/test_sql_file.sql"

```

---

## 🛠️ **CI/CD with GitHub Actions**
This repository includes multiple **GitHub Actions workflows** to automate the **Docker build, testing, deployment, and triggering the Cloud Run endpoint**.

### 📌 **GitHub Actions Workflows**
1️⃣ **Docker Image Creation (`docker-build.yml`)**  
   - Runs on **pushes to `main`**.
   - Builds and pushes the Docker image to **Google Container Registry (GCR)**.

2️⃣ **Docker Testing (`docker-test.yml`)**  
   - Runs on **every pull request**.
   - Builds the Docker image and **runs tests inside the container**.

3️⃣ **Deploy to Cloud Run (`deploy.yml`)**  
   - Runs when **code is merged into `main`**.
   - Deploys the latest Docker image to **Google Cloud Run**.

4️⃣ **Trigger Cloud Run Endpoint (`trigger-cloud-run.yml`)**  
   - Runs on **pull requests**.
   - Calls the deployed Cloud Run endpoint to **validate deployment integrity**.

---

## 📜 **License**
None
---

### 🚀 **Contributors**
💡 Feel free to contribute! Open a PR or issue if you have suggestions.  

🤖 Created and Maintained by **@snehapriya-bs** and the community! 🎉  

---

Let me know if you need any modifications! 🚀🔥
