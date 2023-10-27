from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list_or_create),
    path('articles/<int:article_pk>/', views.article_detail_or_delete_or_update),
]
