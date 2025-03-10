from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category

class CategoryCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_create_category(self):
        response = self.client.post(reverse('category_add'), {'name': 'New Category'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='New Category').exists())
        category = Category.objects.get(name='New Category')
        self.assertEqual(category.created_by, self.user)