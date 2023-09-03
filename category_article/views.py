from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Rating_Comment,Category
from .forms import Rating_CommentForm
from django.db.models import Avg

def category_page (request,category_id):
    category = Category.objects.get(id =category_id)
    articles = Article.objects.filter(category=category).order_by('-ratings')
    return render(request,'article/category_page.html',{'articles':articles,'category':category})





def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    related_articles = Article.objects.filter(category=article.category).exclude(id=article_id)[:2]
    

    average_result = Rating_Comment.objects.filter(article=article).aggregate(Avg('rating'))
    # print(average_result)
    average_rating = average_result['rating__avg']

    if average_rating is not None:
        article.ratings = round(average_rating, 1)
    else:
        article.ratings = 0.0

    rating_form = None
    existing_rating_comment = None

    if request.method == 'POST':
        if request.user.is_authenticated:
            existing_rating_comment = Rating_Comment.objects.filter(user=request.user, article=article).first()

            if existing_rating_comment:
                rating_form = Rating_CommentForm(request.POST, instance=existing_rating_comment)
            else:
                rating_form = Rating_CommentForm(request.POST)

            if rating_form.is_valid():
                rating_comment = rating_form.save(commit=False)
                rating_comment.user = request.user
                rating_comment.article = article
                rating_comment.save()

                
                return redirect('article_detail', article_id=article_id)
        else:
           
            rating_form = Rating_CommentForm(request.POST)

            if rating_form.is_valid():
                rating_comment = rating_form.save(commit=False)
                rating_comment.article = article
                rating_comment.save()

              
                return redirect('article_detail', article_id=article_id)
    else:
        if request.user.is_authenticated:
         
            existing_rating_comment = Rating_Comment.objects.filter(user=request.user, article=article).first()

        if existing_rating_comment:
            initial_data = {
                'rating': existing_rating_comment.rating,
                'comment': existing_rating_comment.comment,
            }
            rating_form = Rating_CommentForm(initial=initial_data)
        else:
            rating_form = Rating_CommentForm()

    context = {
        'article': article,
        'related_articles': related_articles,
        'rating_form': rating_form,
    }
    return render(request, 'article/article_detail.html', context)





