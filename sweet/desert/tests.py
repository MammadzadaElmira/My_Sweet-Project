from django.test import TestCase
from .models import Category
from django.urls import reverse

class CategoryTest(TestCase):
    def test_category_checking(self):
        category = Category.objects.create(title="Desserts")
        self.assertEqual(category.title, "Desserts")



class LoginTest(TestCase):
    def test_log_in_template(self):
        response = self.client.get(reverse("log_in"))
        self.assertTemplateUsed( response,"log_in.html")


class AboutUsTest(TestCase):
    def test_about_us_template(self):
        response = self.client.get(reverse("about_us"))
        self.assertTemplateUsed(response, "about_us.html")
       

