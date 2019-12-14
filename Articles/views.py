from django.shortcuts import render
from .models import Rubric, Article, Comment
from .forms import CommentForm

def HomeView(request):
    return render(request, 'home.html', {'rubric': Rubric.objects.all(), 'articles': Article.objects.all()})

def SortView(request, link):
    rubs = Rubric.objects.get(url = link)
    return render(request, 'home.html', {'rubric': Rubric.objects.all(), 'articles': Article.objects.filter(rubric = rubs.id)})

def ArticleView(request, article_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(commentator = comment_form.cleaned_data['name'], text = comment_form.cleaned_data['text'], article = Article.objects.get(pk = article_id)) 
    else: comment_form = CommentForm()
    cntx = {'rubric': Rubric.objects.all(), 
    'article': Article.objects.get(id = article_id), 
    'comments': Comment.objects.filter(article = article_id),
    'comment_form': comment_form
    }
    return render(request, 'article.html', cntx)