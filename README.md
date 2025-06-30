\
# 📦 Product Return Prediction API

This project builds a **machine learning model** to **predict the return percentage of products** using synthetic e-commerce data. It includes data generation, model training, feature importance visualization, and a real-time API using FastAPI.

* * *

## 🚀 Key Features

* *   ✅ Generates synthetic product data (price, category, orders, past returns)
*     
* *   ✅ Trains a **Random Forest Regressor** to predict return percentage
*     
* *   ✅ Provides a **real-time prediction API** with FastAPI
*     
* *   ✅ Saves model and label encoders for reuse
*     
* *   ✅ Includes a **feature importance plot** for model transparency
*     

* * *

## 📊 Features Used

* *   **Category** – Product type (Clothing, Electronics, etc.)
*     
* *   **Price** – Product’s selling price
*     
* *   **Num\_Orders** – Total orders received for the product
*     
* *   **Past\_Returns** – Number of returns in previous cycles
*     
* *   **Return\_Percentage** – Target variable (calculated from returns and orders)
*     

* * *

## 📁 Project Structure

```
return-prediction-project/
│
├── generate_data.py         # Creates synthetic product dataset
├── product_data.csv         # Synthetic dataset (1000 records)
├── model_train.py           # Trains the model and saves it
├── model.pkl                # Trained Random Forest model
├── encoder.pkl              # LabelEncoder for Category
├── feature_importance.png   # Bar chart showing feature weights
├── main.py                  # FastAPI server for real-time prediction
└── README.md                # Project documentation
```

* * *

## ⚙️ How to Set Up & Run

### 1\. Install required Python libraries

```bash
pip install pandas numpy scikit-learn matplotlib fastapi uvicorn joblib
```

### 2\. Generate synthetic dataset

```bash
python generate_data.py
```

### 3\. Train the model

```bash
python model_train.py
```

### 4\. Launch the FastAPI server

```bash
python -m uvicorn main:app --reload
```

* * *

## 🧪 API Testing (Swagger UI)

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
You'll find an interactive Swagger interface to test your model.

### 🔹 Sample Input

```json
{
  "Category": "Clothing",
  "Price": 2499,
  "Num_Orders": 300,
  "Past_Returns": 40
}
```

### 🔸 Sample Output

```json
{
  "Predicted Return Percentage": 18.72
}
```

* * *

## 📈 Feature Importance Chart

After training, a plot is saved as `feature_importance.png`, helping you understand which features impact return prediction the most.

* *   🟢 `Num_Orders` and `Past_Returns` typically influence return rate the most.
*     
* *   🟡 `Category` also plays a significant role, especially for Clothing or Beauty products.
*     

* * *

## 🎯 Use Cases

* *   🛒 Predict return rates for new products before launch
*     
* *   📉 Help sellers and platforms minimize return risk
*     
* *   📊 Use return insights in inventory or pricing strategies
*     

* * *

## 🧠 Future Improvements

* *   Add more features (e.g., discounts, ratings, shipping time)
*     
* *   Connect with real e-commerce data APIs
*     
* *   Add model explainability with SHAP
*     
* *   Deploy to the cloud (Render, Heroku, AWS, etc.)
*     
* *   Add a Streamlit-based dashboard
*     

* * *

## 👩‍💻 Author

**Tarun Sekar & Sagar K Pillai**  
🎯 This project was built as a portfolio/resume project to showcase real-world ML & API integration.

* * *

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

* * *

