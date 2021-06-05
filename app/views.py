from flask import render_template
from app import app

@app.route('/')
def index():
  # a function that return the index page and its data.....

    message = 'Hello News'
    return render_template('index.html')

@app.route('/news/<news_id>')
def news(news_id):
    # function that returns the news details page and its data

    return render_template('news.html', id = news_id)
@app.route('/news/<int:news_id>')
def  news(news_id):
    #function that returns the movie details page and its data
    return render_template('news.html', id = news_id)