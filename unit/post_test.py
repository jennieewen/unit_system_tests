from unittest import TestCase
from tests.post import Post


class PostTest(TestCase):

    def test_create_post(self):
        p = Post('Test', 'Test Content', 'Description')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)
        self.assertEqual('Description', p.short_description)

    def test_json(self):
        p = Post('Test', 'Test Content', 'Description')
        expected = {'title': 'Test', 'content': 'Test Content', 'short_description': 'Description'}

        self.assertDictEqual(expected, p.json())

