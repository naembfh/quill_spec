from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from category_article.models import Category, Article
from .forms import CategoryForm, ArticleForm
from django.contrib.auth.models import User
from user.models import User_profile


# Create your views here.
@login_required
def create_article(request):
    print(request.user.user_profile.user_type)
    if request.user.user_profile.user_type == 'editor':
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = ArticleForm()
        return render(request, 'editor/create_article.html', {'form': form})
    else:
        return redirect('home')
@login_required   
def editor_dashboard(request):
    if request.user.user_profile.user_type == 'editor':
        articles = Article.objects.all() 
        return render(request, 'editor/editor_dashboard.html', {'articles': articles})
    else:
        return redirect('home')
    
@login_required
def edit_article(request, article_id):
    if request.user.user_profile.user_type == 'editor':
        article = get_object_or_404(Article, pk=article_id)
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = ArticleForm(instance=article)
        return render(request, 'editor/edit_article.html', {'form': form, 'article': article})
    else:
        return redirect('home')

@login_required
def delete_article(request, article_id):
    if request.user.user_profile.user_type == 'editor':
        article = get_object_or_404(Article, pk=article_id)
        if request.method == 'POST':
            article.delete()
            return redirect('editor_dashboard')
        return render(request, 'editor/delete_article.html', {'article': article})
    else:
        return redirect('editor_dashboard')

@login_required
def create_editor(request):
   
    if request.user.user_profile.user_type == 'editor':
    
        users = User.objects.all()
        return render(request, 'editor/create_editor.html', {'users': users})
    else:
        return redirect('editor_dashboard')
    
    


@login_required
def make_editor(request, user_id):
    if request.method == 'POST':
        user_to_make_editor = User.objects.get(pk=user_id)
        user_profile_to_make_editor = User_profile.objects.get(user=user_to_make_editor)
        
       
        if (request.user.user_profile.user_type == 'editor' and
                user_profile_to_make_editor.user_type != 'editor'):
            user_profile_to_make_editor.user_type = 'editor'
            user_profile_to_make_editor.save()
            return redirect('create_editor') 

    return redirect('create_editor') 
