from django.urls import path
from . import views

urlpatterns = [
path('create_article/', views.create_article, name='create_article'),
path('dashboard/', views.editor_dashboard, name='editor_dashboard'),
path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
path('create_editor/', views.create_editor, name='create_editor'),
path('make_editor/<int:user_id>/', views.make_editor, name='make_editor'),
]