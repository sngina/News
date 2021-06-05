import unittest
from models import news
News = news.News
class NewsTest(unittest.TestCase):
    #test the behaviour of the news class
    def setUp(self):
        #method that will run before every test
        self.new_news = News(1234, 'Where did covid come from','"https://cointelegraph.com/news/no-musk-don-t-blame-bitcoin-for-dirty-energy-the-problem-lies-deeper')
        def test_instances(self):
            self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()
        