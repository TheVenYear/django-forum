from django.urls import path
from .views import HomeView, SortView, ArticleView
urlpatterns = [
    path('', HomeView, name = 'home_url'),
    path('sort_by:<str:link>/', SortView, name = 'sort_url'),
    path('article:<int:article_id>', ArticleView, name = 'article_view_url')

]