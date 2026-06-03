# 📚 AI Research Assistant

An AI-powered research paper analysis tool built using Python, Streamlit, Google Gemini, PyPDF, and ReportLab.

The application allows users to upload research papers in PDF format, generate structured insights, ask questions about the paper, and download professional analysis reports.

## 🌐 Live Demo

🔗 https://ai-research-assistant-yug.streamlit.app/

---

## 🚀 Features

### 📄 Research Paper Analysis

* Upload PDF research papers
* Extract and process paper content
* Generate AI-powered analysis using Google Gemini

### 📝 Structured Insights

* Summary Generation
* Key Contributions Extraction
* Limitations Identification
* Future Work Suggestions

### 💬 Interactive Paper Chat

* Ask questions about the uploaded paper
* Receive contextual answers based on paper content
* Maintain conversation history during the session

### 📥 Report Export

* Download analysis results as a PDF report
* Save research insights for future reference

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* PyPDF
* ReportLab
* Python Dotenv

---

## 📂 Project Structure

```text
AI-Research-Assistant/
│
├── app.py
├── app_backup_v1.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── venv/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yugbagrodia/AI-Research-Assistant.git
cd AI-Research-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a .env File

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### 6. Run the Application

```bash
streamlit run app.py
```

---

## 🎯 How It Works

1. Upload a research paper in PDF format.
2. The application extracts text from the PDF.
3. Google Gemini analyzes the content.
4. The system generates:

   * Summary
   * Key Contributions
   * Limitations
   * Future Work
5. Users can ask additional questions about the paper.
6. Analysis results can be downloaded as a PDF report.

---

## 📈 Future Improvements

* Full-paper analysis using chunking
* Multi-paper comparison
* Citation extraction
* Research paper recommendation system
* Advanced Retrieval-Augmented Generation (RAG)
* Online deployment and public access

---

## 👨‍💻 Author

Developed by Yug Bagrodia as part of AI/ML learning and research exploration.
