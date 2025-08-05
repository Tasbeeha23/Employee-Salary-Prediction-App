# 💼 Salary Estimation Web App

A simple, interactive web application built using **Streamlit** and **Machine Learning** to predict expected salaries based on user input. This project showcases how to deploy a trained ML model in a user-friendly web interface for real-world usage.

---

## 🚀 Features

- 📊 Predicts salary based on experience, company level, etc.
- 🧠 Uses a trained **Linear Regression** model
- 🔄 Preprocessing handled with **StandardScaler**
- 💾 Model and scaler loaded via `joblib`
- 🌐 Built and deployed using **Streamlit**

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/salary-estimation-app.git
   cd salary-estimation-app
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows
Install the dependencies

bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the App
To run the Streamlit app locally:

bash
Copy
Edit
streamlit run app.py
This will launch the app in your default browser at http://localhost:8501.

🧠 Model Info
Model: Linear Regression

Scaler: StandardScaler

Persistence: Both saved using joblib

File Names:

model.pkl

scaler.pkl

📁 Project Structure
Copy
Edit
.
├── app.py
├── scaler.pkl
├── model.pkl
├── requirements.txt
└── README.md

✨ Screenshots 
<img width="1066" height="559" alt="app2" src="https://github.com/user-attachments/assets/4c7394ef-b4ff-433e-a259-79e1bec0a33e" />


🤝 Contributing
Pull requests are welcome! Feel free to fork the repo and improve the UI, model, or logic.

📝 License
This project is open-source and available under the MIT License.
