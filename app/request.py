from app import app
import urllib.request, json
from .models import news

News = news.News
# Getting the api key

api_key = app.config['NEWS_API_KEY']

#getting the news base url
base_url = app.config["NEWS_BASE_URL"]


def get_news(category):
    # function that gets the json response to our url.
    get_news_url = base_url.format(api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url)as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results
def process_results(news_list):
    # function that processes the news result and transform them to a list of objects
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        author= news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

    
        news_object = News(id,author,title, description,publishedAt,content)
        news_results.append(news_object)
    return news_results
def get_new(id):
    get_new_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_url) as url:
        news_details_data =url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('original_title')
            description = news_details_response.get('description')
            publishedAt = news_details_response.get('publishedAt')
            content = news_details_response.get('content')

            news_object = News(id,title,description,publishedAt,content)
        return news_object