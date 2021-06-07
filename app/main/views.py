from flask import render_template ,request, redirect, url_for
from  . import main
from ..request import get_news , get_new



@main.route('/')
def index():
  # function that returns the index page and its data

  #getting trending news
  trending_news = get_news('entertainment')
  now_showing_news = get_news('business')
  general = get_news ('general')
  sports = get_news('sports')
  health = get_news('health')
  technology = get_news('technology')

  title = 'Home -Welcome to the News Website Online'
  return render_template('index.html', title = title, trending = trending_news, now_showing = now_showing_news , general = general , sports = sports, health = health,  technology = technology)



@main.route('/new/<id>')
def new(id):
  # function that returns the news details page.

  new = get_new(id)
  return render_template('news.html', new = new)
