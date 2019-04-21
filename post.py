class Post:
    def __init__(self, title, content, short_description):
        self.title = title
        self.content = content
        self.short_description = short_description

    def __repr__(self):
        return ' blah'



    # converting post to JSON
    def json(self):
        return {
            'title': self.title,
            'content': self.content,
            'short_description': self.short_description,
         }

