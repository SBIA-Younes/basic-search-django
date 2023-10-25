from django.urls import path

from .views import HommePagerView, SearchResultsView, BlogDetailView

urlpatterns = [
    path("", HommePagerView.as_view(),name='homme'),
    path('search/',SearchResultsView.as_view(),name='search_results'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
