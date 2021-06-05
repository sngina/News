class News:
    # news class to define the news objects.
    def __init__(self,id,author,title,description,publishedAt,content):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content