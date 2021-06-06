from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():
  # function that returns the index page and its data

  #getting trending news
  trending_news = get_news('popular')
  now_showing_news = get_news('now_showing_news')
  print(trending_news)
  title = 'Home -Welcome to the News Website Online'
  return render_template('index.html', title = title, trending = trending_news, now_showing = now_showing_news)


@app.route('/news/<int:news_id>')
def news(news_id):
    # function that returns the news details page and its data

    return render_template('news.html', id = news_id)
