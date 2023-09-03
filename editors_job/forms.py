
from django import forms
from category_article.models import Category, Article

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'body', 'category', 'image']
