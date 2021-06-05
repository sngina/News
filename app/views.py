from flask import render_template
from app import app

@app.route('/')
def index():
  # a function that return the index page and its data.....

    message = 'Hello News'
    return render_template('index.html')

@app.route('/news/<int:news_id>')
def news(news_id):
    # function that returns the news details page and its data

    return render_template('news.html', id = news_id)
def index():
    # function that returns the index page and its data
    title = 'Home - Welcome to The News Website Online'
    return render_template('index.html',title = title)
