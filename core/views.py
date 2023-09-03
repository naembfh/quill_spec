from django.shortcuts import render
from category_article.models import Category,Article
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    categories = Category.objects.order_by('name') 
    # print(categories)
    top_two_article_each_category = []
    for category in categories:
        article = Article.objects.filter(category=category)
        # print(article)
        top_article = article.order_by('-ratings')[:2]
        top_two_article_each_category.append({'category':category,'articles':top_article})
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_categories = paginator.get_page(page_number)
    context = {'page_categories': page_categories,'top_two_article_each_category': top_two_article_each_category,}
    return render(request, 'core/home.html', context)