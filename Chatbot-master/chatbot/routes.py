from flask import render_template, request
from chatbot import app  # Assuming 'app' is your Flask application instance
from chatbot.forms import chatbotform  # Import your forms if needed
from chatbot.__init__ import model, words, classes, intents  # Import your initialized variables

import nltk
import numpy as np
from datetime import datetime
import pytz
import requests
import random
import billboard
import time
import COVID19Py

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Function definitions for prediction and response as you have implemented
def clean_up(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def create_bow(sentence, words):
    sentence_words = clean_up(sentence)
    bag = list(np.zeros(len(words)))

    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence, model):
    p = create_bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    threshold = 0.8
    results = [[i, r] for i, r in enumerate(res) if r > threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{'intent': classes[result[0]], 'prob': str(result[1])} for result in results]
    return return_list

def get_response(return_list, intents_json, text):
    if len(return_list) == 0:
        tag = 'noanswer'
    else:
        tag = return_list[0]['intent']

    if tag == 'datetime':
        tz = pytz.timezone('Asia/Kolkata')
        dt = datetime.now(tz)
        return dt.strftime("%A %d %B %Y %H:%M:%S"), 'datetime'

    if tag == 'weather':
        api_key = '987f44e8c16780be8c85e25a409ed07b'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = text.split(':')[1].strip()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url).json()
        pres_temp = round(response['main']['temp'] - 273, 2)
        feels_temp = round(response['main']['feels_like'] - 273, 2)
        cond = response['weather'][0]['main']
        return f"Present temp.: {pres_temp}°C. Feels like: {feels_temp}°C. {cond}", 'weather'

    if tag == 'news':
        main_url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=bc88c2e1ddd440d1be2cb0788d027ae2"
        open_news_page = requests.get(main_url).json()
        article = open_news_page["articles"]
        x = ''
        for i, ar in enumerate(article[:10]):
            x += f"{i + 1}. {ar['title']} - {ar['url']}\n"
        return x, 'news'

    if tag == 'song':
        chart = billboard.ChartData('hot-100')
        x = 'The top 10 songs at the moment are:\n'
        for i, song in enumerate(chart[:10]):
            x += f"{i + 1}. {song.title} - {song.artist}\n"
        return x, 'songs'

    if tag == 'timer':
        x = text.split(':')[1].strip()
        time.sleep(float(x) * 60)
        return 'Timer ringing...', 'timer'

    if tag == 'covid19':
        covid19 = COVID19Py.COVID19(data_source='jhu')
        country = text.split(':')[1].strip()
        if country.lower() == 'world':
            latest_world = covid19.getLatest()
            return f"Confirmed Cases: {latest_world['confirmed']} Deaths: {latest_world['deaths']}", 'covid19'
        else:
            latest = covid19.getLocations()
            latest_conf = np.sum([loc['latest']['confirmed'] for loc in latest if loc['country'].lower() == country.lower()])
            latest_deaths = np.sum([loc['latest']['deaths'] for loc in latest if loc['country'].lower() == country.lower()])
            return f"Confirmed Cases: {latest_conf} Deaths: {latest_deaths}", 'covid19'

    # Default response if no specific tag matched
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if tag == i['tag']:
            result = random.choice(i['responses'])
            break
    else:
        result = "Sorry, I didn't quite get that."

    return result, tag

def response(text):
    return_list = predict_class(text, model)
    response_text, _ = get_response(return_list, intents, text)
    return response_text

# Route for the main page
@app.route('/')
def main():
    return render_template('main.html')

# Route for the chat interface
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        form = chatbotform(request.form)
        if form.validate():
            user_input = form.user_input.data
            response_text = response(user_input)
            return render_template('index.html', response=response_text, form=form)
    return render_template('index.html', form=chatbotform())

# Route for AJAX requests from frontend
@app.route("/get")
def chatbot():
    userText = request.args.get('msg')
    resp = response(userText)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
