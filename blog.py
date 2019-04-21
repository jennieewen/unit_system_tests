from tests.post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return '{} by {} ({} posts)'.format(self.title, self.author, len(self.posts))

    def create_post(self, title, content, short_description):
        self.posts.append(Post(title, content, short_description))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],
        }