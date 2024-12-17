---
# **Financial News and Stock Price Integration Project**
## **Exploratory Data Analysis (EDA) - Task 1**
---

### **Project Overview**

This project focuses on analyzing the relationship between financial news sentiment and stock price movements. The ultimate objective is to derive actionable insights by combining **Natural Language Processing (NLP)** and **Financial Analytics**.

**Task 1** primarily involves performing **Exploratory Data Analysis (EDA)** to understand trends, sentiment distributions, and key patterns in the financial news dataset.

---

### **Folder Structure**

```
├── notebooks/
│   ├── task1_eda.ipynb       # Notebook for EDA and sentiment analysis
│   └── README.md             # Current file
├── data/
│   ├── financial_news.csv    # Original dataset
│   └── eda_results.csv       # Processed data with analysis outputs
├── scripts/
│   └── utils.py              # Reusable functions for data analysis
├── tests/
│   ├── test_utils.py         # Unit tests for scripts
├── .github/
│   └── workflows/unittests.yml # CI/CD for testing
├── requirements.txt          # Python dependencies
└── README.md                 # Project Overview & Task Documentation
```

---

### **Objectives of Task 1**

1. **Descriptive Statistics**

   - Analyze headline lengths, top publishers, and article frequency trends.

2. **Text Analysis**

   - Perform sentiment analysis to classify headlines as positive, neutral, or negative.
   - Extract keywords using TF-IDF to identify recurring themes.

3. **Time Series Analysis**

   - Analyze trends in article publication frequency over time.
   - Identify spikes around financial events or mid-week patterns.

4. **Publisher Analysis**
   - Investigate article contributions by top publishers and domain sources.

---

### **Results Summary**

- **Headline Length:** Average length is **73 characters**, with most headlines between 50-100 characters.
- **Top Publishers:**
  - _Paul Quintaro_: 228,373 articles
  - _Lisa Levin_: 186,979 articles
- **Sentiment Distribution:**
  - Positive: **41%**
  - Neutral: **50%**
  - Negative: **9%**
- **Keywords Extracted:** 'announces' 'benzinga' 'buy' 'downgrades' 'earnings' 'eps' 'est' 'market' 'mid' 'price' 'pt' 'raises' 'reports' 'sales' 'shares' 'stocks' 'trading' 'update' 'vs' 'week'
- **Publication Trends:** Spikes observed mid-week, particularly on **Wednesdays** and **Thursdays**, and during major financial events.

---

### **Technologies Used**

- **Programming Language:** Python
- **Libraries:**
  - Pandas, NumPy – Data processing
  - Matplotlib, Seaborn – Data visualization
  - NLTK – Sentiment analysis
  - Scikit-learn – Keyword extraction

---

### **Setup Instructions**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/tesfaymebre/Financial-News-and-Stock-Price-Integration
   cd Financial-News-and-Stock-Price-Integration
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---
