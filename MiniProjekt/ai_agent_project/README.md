---

# **AI Agent: Interactive Data Query System**

This project allows users to upload **CSV files** or provide **public Google Sheets URLs** and ask **natural language queries**. Powered by a **Language Learning Model (LLM)**, the application generates context-aware responses based on the uploaded data.

## **✨ Key Features**
- **Multi-format Input**: Accepts both CSV files and public Google Sheets links for data input.
- **Dynamic Query Response**: Processes natural language queries and provides tailored responses based on the uploaded data.
- **User-Friendly Dashboard**:
  - Upload files or link Google Sheets effortlessly.
  - Preview uploaded data within the interface.
  - Ask questions dynamically.
  - Download query responses as CSV files.
- **Seamless Integration**:
  - Leverages Google Sheets API for fetching sheet data.
  - Uses Groq's advanced LLM for generating intelligent responses.

---

## **📂 Project Structure**

```
ai_agent_project/
├── app.py                     # Main application script
├── frontend/
│   └── ui.py                  # User interface code
├── backend/
│   ├── api_connections.py     # API integrations for Groq and Google Sheets
│   ├── data_processing.py     # Handles data query processing
│   └── llm_integration.py     # Interacts with LLM for responses
├── requirements.txt           # Required Python packages
├── .env                       # API keys (not included in the repo)
└── README.md                  # Project documentation
```

---

## **🚀 Setup and Usage**

### **1️⃣ Prerequisites**
Ensure the following are installed:
- Python (>= 3.10)
- Required libraries listed in `requirements.txt`.

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/SureshKumar3140/ai_agent_project.git
cd ai_agent_project
```

### **3️⃣ Install Dependencies**
Install all required Python libraries:
```bash
pip install -r requirements.txt
```

### **4️⃣ Environment Setup**
Create a `.env` file in the project directory to store your API keys:
```env
GROQ_API_KEY=<your_groq_api_key>
SERP_API_KEY=<your_serp_api_key>
```

### **5️⃣ Run the Application**
Start the Streamlit app:
```bash
streamlit run app.py
```

Open the app in your browser at `http://localhost:8501`.

---

## **🧰 Required Libraries**

The following libraries are required for the project:
- **Streamlit**: For building the web interface.
- **Pandas**: For data manipulation and processing.
- **Gspread**: For Google Sheets API connection.
- **OAuth2Client**: For authenticating Google Sheets access.
- **Requests**: For handling API calls.
- **Dotenv**: For securely managing environment variables.

Install them via the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### **Additional Notes**
If any library is missing, you can install it manually. Example:
```bash
pip install streamlit pandas gspread oauth2client requests python-dotenv
```

---

## **📹 Loom Video Walkthrough**

[🎥 Watch the walkthrough video here](https://drive.google.com/file/d/114lSyMZaBZ2YNvDvY47V3CsxIR7EjEX1/view?usp=sharing)

---

## **💡 How to Use**
1. **Choose Input Source**: Select "CSV" to upload a file or "Google Sheets" to provide a URL.
2. **Preview Data**: View the first few rows of your data after uploading or linking.
3. **Ask Queries**: Enter natural language questions related to the data.
4. **View Results**: Get context-aware answers based on your uploaded data.
5. **Download Results**: Export query responses as a CSV file.

---

## **🛠️ Future Enhancements**
- Support for private Google Sheets using credentials.
- Advanced query understanding with support for multi-language inputs.
- Enhanced visualization and data insights.

---

## **📜 License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
