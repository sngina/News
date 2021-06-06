from instance.config import NEWS_API_KEY


class Config:
    '''
    General configuration parent class
    '''
    CATEGORY_URL =  'https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=ad60a84a90b44683897fb1d384e67f04'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True