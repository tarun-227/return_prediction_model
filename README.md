Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # 📦 Product Return Prediction API  This project builds a machine learning model to **predict the return percentage of products** using synthetic e-commerce data. It includes data generation, training, model saving, and a real-time API using FastAPI.  ---  ## 🚀 Features  - ✅ Synthetic dataset generation    - ✅ Random Forest Regressor model    - ✅ Real-time predictions via FastAPI    - ✅ Feature importance chart    - ✅ Modular and resume-ready project  ---  ## 📊 Features Used  - **Category** – Product type (Clothing, Electronics, etc.)    - **Price** – Product price    - **Num_Orders** – Total orders received    - **Past_Returns** – Previous return count    - **Return_Percentage** – Target variable for model  ---  ## 📁 Project Structure   `

return-prediction-project/│├── generate\_data.py # Creates synthetic dataset├── product\_data.csv # Dataset with return info├── model\_train.py # Trains and saves the model├── model.pkl # Trained ML model├── encoder.pkl # Category label encoder├── feature\_importance.png # Visual of feature impact├── main.py # FastAPI app for real-time prediction└── README.md # Project documentation

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ---  ## ⚙️ Setup & Run Instructions  ### 1. Clone the repo (or create folder manually)  ```bash  git clone https://github.com/yourusername/return-prediction-project.git  cd return-prediction-project   `

### 2\. Install required libraries

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install pandas numpy scikit-learn matplotlib fastapi uvicorn joblib   `

### 3\. Generate the synthetic data

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python generate_data.py   `

### 4\. Train the machine learning model

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python model_train.py   `

### 5\. Launch the FastAPI server

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m uvicorn main:app --reload   `

🧪 How to Test
--------------

Visit:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://127.0.0.1:8000/docs   `

Use the interactive Swagger UI to test the /predict endpoint.

### 🔸 Sample Input

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "Category": "Clothing",    "Price": 2499,    "Num_Orders": 300,    "Past_Returns": 40  }   `

### 🔹 Sample Output

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "Predicted Return Percentage": 18.72  }   `

📈 Feature Importance Example
-----------------------------

The model’s top influencing features:

🎯 Use Cases
------------

*   Predict return risk for new products
    
*   Help sellers improve product quality
    
*   Integrate into e-commerce dashboards
    

🧠 Future Improvements
----------------------

*   Add real-world data or APIs
    
*   Include more features (e.g. discounts, reviews)
    
*   Use SHAP for model explainability
    
*   Deploy to cloud (Render, Heroku, etc.)
    
*   Build frontend with Streamlit
    

👩‍💻 Author
------------

**Janavi S.D**Aspiring IAS Officer | ML Learner | Self-Improvement EnthusiastProject created for resume portfolio and hands-on ML practice.

📜 License
----------

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML``   ---  Let me know if you'd like a `requirements.txt`, push-to-GitHub guide, or a Streamlit UI next! 💻   ``
