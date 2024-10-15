<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project README - Sentiment Analysis with Linear Regression</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f5f5f5;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 20px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            display: inline-block;
            background: #eee;
            padding: 5px;
            border-radius: 5px;
            color: #333;
            font-size: 0.9em;
        }
        pre {
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sentiment Analysis with Linear Regression</h1>

        <h2>Project Information</h2>
        <ul>
            <li><strong>Name:</strong> Abhishek Chauhan</li>
            <li><strong>Company:</strong> Codtech IT Solutions</li>
            <li><strong>ID:</strong> CT6WDS1850</li>
            <li><strong>Domain:</strong> Machine Learning</li>
            <li><strong>Duration:</strong> September 5, 2024 to October 20, 2024</li>
        </ul>

        <h2>Project Overview</h2>
        <p>This project applies sentiment analysis on IMDB movie reviews using machine learning models, such as Linear Regression, Logistic Regression, and Support Vector Classifier (SVC). By processing and analyzing text data, it identifies and predicts whether reviews are positive or negative.</p>

        <h2>Requirements</h2>
        <pre>
pip install pandas matplotlib seaborn plotly nltk wordcloud scikit-learn
        </pre>

        <h2>Data Processing</h2>
        <p>The data is preprocessed to remove special characters, HTML tags, and stop words. The cleaned text is then tokenized and stemmed to reduce dimensionality.</p>

        <h2>Usage</h2>
        <p>Follow these steps to run the project:</p>
        <ol>
            <li>Clone the repository.</li>
            <li>Install the required packages.</li>
            <li>Run the main Python script to load and process data.</li>
            <li>Review the generated visualizations for sentiment analysis results.</li>
        </ol>

        <h2>Example Code</h2>
        <h3>1. Loading and Displaying Data</h3>
        <pre>
df = pd.read_csv('IMDB Dataset.csv')
df.head()
        </pre>

        <h3>2. Plotting Sentiment Distribution</h3>
        <pre>
sns.countplot(x='sentiment', data=df)
plt.title("Sentiment Distribution")
plt.show()
        </pre>

        <h3>3. Training Model</h3>
        <pre>
logreg = LogisticRegression()
logreg.fit(x_train, y_train)
logreg_pred = logreg.predict(x_test)
        </pre>

        <h2>Results</h2>
        <p>Accuracy and model performance details for each machine learning model are provided within the project scripts.</p>
        
        <h2>Contact</h2>
        <p>For more information, reach out to <strong>Abhishek Chauhan</strong> at Codtech IT Solutions.</p>
    </div>
</body>
</html>
