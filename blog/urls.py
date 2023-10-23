from django.urls import path

from .views import HommePagerView, SearchResultsView

urlpatterns = [
    path('search/',SearchResultsView.as_view(),name='search_results'),
    path("", HommePagerView.as_view(),name='homme'),
]
