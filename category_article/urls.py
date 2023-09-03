from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/', views.category_page, name='category_page'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]
