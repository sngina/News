from flask import render_template ,request, redirect, url_for
from  . import main
from ..request import get_news , get_new



@main.route('/')
def index():
  # function that returns the index page and its data

  #getting trending news
  trending_news = get_news('entertainment')
  now_showing_news = get_news('business')
  print(trending_news[0].name)
  title = 'Home -Welcome to the News Website Online'
  return render_template('index.html', title = title, trending = trending_news, now_showing = now_showing_news)



@main.route('/new/<id>')
def new(id):
  # function that returns the news details page.

  new = get_new(id)
  return render_template('news.html', new = new)
