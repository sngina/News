class News:
    # news class to define the news objects.
    def __init__(self,id,name,description,url,category,language):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
class Article:
    def __init__(self,author,url,title,description,publishedAt,content,UrlToImage):
        self.author = author
        self.url = url
        self.title = title
        self.description = description
        self.publisedAt = publishedAt
        self.content = content
        self.UrlToImage = UrlToImage 

        