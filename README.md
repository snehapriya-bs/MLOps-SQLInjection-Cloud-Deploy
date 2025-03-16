### `ML-SQLInjection-Detection`  
Check the notebooks [here](https://github.com/snehapriya-bs/ML-SQLInjection-Detection) for detailed code and explanation.

This repository modularizes the code for SQL Injection Detection and integrates it with **CI/CD** using **Docker** and **GitHub Actions**.

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
del model.pkl vectorizer.pkl
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
- **GitHub Actions**: Automates builds and tests.  

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

## 💡 **Contributing**  
Feel free to open a PR or raise an issue! 😊  
```

This version includes **SqlInjection.csv** in both the instructions and the file structure. 👍
