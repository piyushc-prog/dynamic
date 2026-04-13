# 📌 Project Overview 

This project is a simple and efficient pipeline for training word embedding models using textual data extracted directly from any webpage URL.

---

# 🚀 Objective

The main goals of this project are to:

* Accept a webpage URL as input
* Fetch and extract textual content from the webpage
* Train word embedding models:

  * **CBOW (Continuous Bag of Words)**
  * **Skip-Gram**
* Allow users to save trained models
* Enable interactive querying of trained models

---

# ⚙️ How It Works

### 1. Enter URL

Provide a webpage URL from which the system will extract text data.

### 2. Choose Model

Select the model you want to train:

* CBOW
* Skip-Gram

### 3. Train Model

The system processes the extracted text and trains the selected word embedding model.

### 4. Save Model

After training, you will be prompted to save the model for future use.

### 5. Query Model

Interact with the trained model to:

* Find similar words
* Explore semantic relationships

---

# ✨ Features

* Extract text from any webpage URL
* Train CBOW and Skip-Gram models
* Save trained models locally
* Interactive querying of word embeddings

---

# 🧰 Requirements

Ensure you have the following installed:

* Python 3.8 or higher
* pip (Python package manager)

---

# 📦 Installation

### Install dependencies using requirements file:

```bash
pip install -r requirements.txt
```

### Or install manually:

```bash
pip install requests beautifulsoup4 nltk gensim
```

---

# 📚 Libraries Used

* **requests** – Fetch webpage content
* **beautifulsoup4** – Parse HTML and extract text
* **nltk** – Text preprocessing
* **gensim** – Train CBOW and Skip-Gram models

---

# 🧪 Virtual Environment Setup (Recommended)

### Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **macOS/Linux:**

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Run the main script:

```bash
python main.py
```

Then follow the prompts:

1. Enter a webpage URL
2. Select model (CBOW / Skip-Gram)
3. Train and save the model
4. Query the trained model

---

# 📁 Project Structure

```
.
├── main.py          # Entry point of the application
├── utils.py         # Helper functions for preprocessing and utilities
├── model/           # Saved models directory
├── data/            # Extracted or processed data
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

