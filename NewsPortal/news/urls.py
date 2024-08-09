from django.urls import path
#имортируем созданное нами представление
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete


urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('search/', NewsSearch.as_view(), name='search'),
    path('<int:pk>/', NewsDetail.as_view(), name='post_detail'),
    path('create/', NewsCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('articles/create/', NewsCreate.as_view(), name='post_create'),
    path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='post_edit'),
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
]
