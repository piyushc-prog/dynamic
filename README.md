📌 Project Overview

This project is a simple pipeline to train word embedding models using text data extracted from any webpage URL.

🚀 Objective

The goal of this project is to:

Take a URL as input
Fetch and extract textual data from the webpage
Train word embedding models:
CBOW (Continuous Bag of Words)
Skip-Gram
Allow users to save the trained model
Enable querying of the trained model




⚙️ How It Works
Enter URL
Provide a webpage URL from which text data will be extracted.
Choose Model
Select which model you want to train:
CBOW
Skip-Gram
Train Model
The system processes the text and trains the selected model.
Save Model
After training, you will be prompted to save the model.
Query Model
You can query the trained model to:
Find similar words
Explore word relationships




Features
Fetch data from any URL
Train CBOW and Skip-Gram models
Save trained models
Query models interactively



Requirements

Make sure you have the following installed:

Python 3.8 or higher
pip (Python package manager)
📦 Required Python Libraries

Install dependencies using:

pip install -r requirements.txt

Or install manually:

pip install requests beautifulsoup4 nltk gensim

Libraries used:

requests – for fetching webpage data
beautifulsoup4 – for parsing HTML
nltk – for text preprocessing
gensim – for training CBOW and Skip-Gram models
🧪 Setting Up Virtual Environment

It is recommended to use a virtual environment to manage dependencies.


🔹 Step 1: Create Virtual Environment
python -m venv venv
🔹 Step 2: Activate Virtual Environment
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
🔹 Step 3: Install Dependencies
pip install -r requirements.txt
▶️ Usage

Run the main script:

python main.py

Then follow the prompts:

Enter URL
Select model (CBOW / Skip-Gram)
Train and save model
Query the model


📁 Project Structure 
.
├── main.py
├── utils.py
├── model/
├── data/
├── requirements.txt
└── README.md



Future Improvements
Add GUI or web interface
Support more NLP models
Improve preprocessing pipeline
Add evaluation metrics
