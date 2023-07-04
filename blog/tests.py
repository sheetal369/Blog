from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = User.objects.create(username='testuser')  # Create a user
        cls.post = Post.objects.create(
            title='Gangadhar ko Jeewan katha',
            slug='gangadhar-ko-jeewan-katha',
            body='This book is about the life of the Great Gangadhar',
            author=author
        )

    def test_post_content(self):
        self.assertEqual(self.post.title, 'Gangadhar ko Jeewan katha')
        self.assertEqual(self.post.slug, 'gangadhar-ko-jeewan-katha')
        self.assertEqual(self.post.body, 'This book is about the life of the Great Gangadhar')
        self.assertEqual(str(self.post.author), 'testuser')

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "posts/blogs_list.html")
