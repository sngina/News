from urllib.request import url2pathname


class News:
    # news class to define the news objects.
    def __init__(self,id,author,title,description,publishedAt,content,url,urlToImage):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.urlToImage = urlToImage
