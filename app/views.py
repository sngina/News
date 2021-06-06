from flask import render_template
from app import app
from .request import get_news , get_new


@app.route('/')
def index():
  # function that returns the index page and its data

  #getting trending news
  trending_news = get_news('entertainment')
  now_showing_news = get_news('business')
  print(trending_news[0].name)
  title = 'Home -Welcome to the News Website Online'
  return render_template('index.html', title = title, trending = trending_news, now_showing = now_showing_news)


@app.route('/news/<int:news_id>')
def news(news_id):
    # function that returns the news details page and its data

    return render_template('news.html', id = news_id)

@app.route('/new/<id>')
def new(id):
  # function that returns the news details page.

  new = get_new(id)
  print(new [0])
  title = f'{new.title}'
  return render_template('news.html', title = title, new = new)
