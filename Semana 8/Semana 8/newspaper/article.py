class Article:
    def __init__(self, title, sum_up,body,images,create_date,writer):
        self.title = title
        self.sum_up = sum_up
        self.body = body
        self.images = images
        self.create_date = create_date
        self.publish_date = None
        self.writer = writer