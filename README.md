<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>IMDB Sentiment Analysis - README</title>
</head>
<body>

<!-- Project Information -->
<section>
    <h1>IMDB Sentiment Analysis</h1>
    <p>This project classifies IMDB movie reviews as either positive or negative using machine learning models, such as Logistic Regression, Naive Bayes, and Support Vector Classifier (SVC). It involves data preprocessing, exploratory data analysis, and model evaluation.</p>

    <h2>Project Information</h2>
    <p><strong>Name:</strong> Abhishek Chauhan</p>
    <p><strong>Company:</strong> Codtech IT Solutions</p>
    <p><strong>ID:</strong> CT6WDS1850</p>
    <p><strong>Domain:</strong> Machine Learning</p>
    <p><strong>Duration:</strong> September 5, 2024 - October 20, 2024</p>
</section>

<h2>Overview</h2>
<p>This project aims to classify movie reviews from an IMDB dataset as either positive or negative. The classification is achieved through various machine learning models, such as Logistic Regression, Naive Bayes, and SVC, with text preprocessing techniques to enhance prediction accuracy.</p>

<h2>Dataset</h2>
<ul>
    <li><strong>Source:</strong> IMDB Dataset containing labeled reviews</li>
    <li><strong>Objective:</strong> Predict the sentiment (positive or negative) based on review content</li>
</ul>

<h2>Project Structure</h2>
<ul>
    <li><strong>Data Preprocessing:</strong> Text cleaning, tokenization, stemming, and stopword removal</li>
    <li><strong>Exploratory Data Analysis (EDA):</strong> Distribution analysis and word cloud generation for sentiment insights</li>
    <li><strong>Modeling:</strong> Applying and evaluating classifiers, parameter tuning for optimal results</li>
</ul>

<h2>Installation</h2>
<pre><code>
# Clone the repository
git clone https://github.com/your-repository/IMDB-Sentiment-Analysis

# Navigate into the project directory
cd IMDB-Sentiment-Analysis

# Install the required libraries
pip install -r requirements.txt
</code></pre>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>Libraries:
        <ul>
            <li>pandas</li>
            <li>matplotlib</li>
            <li>seaborn</li>
            <li>plotly</li>
            <li>nltk</li>
            <li>wordcloud</li>
            <li>sklearn</li>
        </ul>
    </li>
</ul>

<h2>Usage</h2>

<h3>1. Load the Dataset</h3>
<pre><code>
import pandas as pd

# Load the IMDB dataset
df = pd.read_csv('IMDB Dataset.csv')
</code></pre>

<h3>2. Preprocess the Data</h3>
<pre><code>
# Import libraries for data cleaning
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

# Define a function for text cleaning
def data_processing(text):
    # Cleaning logic here...
    return text
</code></pre>

<h3>3. Train Classifier Models</h3>
<pre><code>
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

# Train, predict, and evaluate models
logreg = LogisticRegression()
logreg.fit(x_train, y_train)
</code></pre>

<h3>4. Evaluate Model Performance</h3>
<pre><code>
from sklearn.metrics import accuracy_score

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Test accuracy: {:.2f}%".format(accuracy * 100))
</code></pre>

<h2>Results</h2>
<ul>
    <li><strong>Logistic Regression:</strong> xx% accuracy</li>
    <li><strong>Naive Bayes:</strong> xx% accuracy</li>
    <li><strong>Support Vector Classifier (SVC):</strong> xx% accuracy</li>
</ul>

</body>
</html>
