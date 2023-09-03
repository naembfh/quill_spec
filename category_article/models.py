from django.db import models
from django.contrib.auth.models import User
from django.forms import forms
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
CATEGORY_CHOICES = [
    ('Latest', 'Latest'),
    ('Politics', 'Politics'),
    ('Crime', 'Crime'),
    ('Opinion', 'Opinion'),
    ('Business', 'Business'),
    ('Sports', 'Sports'),
    ('Entertainment', 'Entertainment'),
    ('Jobs', 'Jobs'),
    ('Tech', 'Tech'),
]

class Category(models.Model):
    name = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='photos/categories')
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publishing_time = models.DateTimeField(auto_now_add=True)
    ratings = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='photos/articles')

    def __str__(self):
        return self.headline
    
class Rating_Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # rating = models.DecimalField(max_digits=2, decimal_places=1)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),  
            MaxValueValidator(4),
        ]
    )
    comment = models.TextField(blank=True, null=True)
    
   