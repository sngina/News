from app import app
import urllib.request, json
from .models import news


News = news.News
# Getting the api key

api_key = app.config['NEWS_API_KEY']

#getting the news base url
base_url = app.config["NEWS_BASE_URL"]

# getting the category 
category_url = app.config["CATEGORY_URL"]


def get_news(source):
    # function that gets the json response to our url.
    get_news_url = category_url.format(source, api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url)as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
    print(news_results)
    return news_results
def process_results(news_list):
    # function that processes the news result and transform them to a list of objects
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')

    
        news_object = News(id,name, description,url,category,language)
        news_results.append(news_object)
        print(name)

    return news_results

def get_new(id):
    get_new_url = base_url.format(api_key)

    with urllib.request.urlopen(get_new_url) as url:
        news_details_data =url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        
        return news_object
def process_article(news_article):
    process_article_list = []

    for news_details_response in news_article:
        author = news_details_response.get('author')
        url = news_details_response.get('url')
        title = news_details_response.get('original_title')
        description = news_details_response.get('description')
        publishedAt = news_details_response.get('publishedAt')
        content = news_details_response.get('content')
        urlToImage = news_details_response.get('urlToImage')

        news_object = News(author,url,title,description,publishedAt,content,urlToImage,)

