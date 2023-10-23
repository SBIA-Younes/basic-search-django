from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import BlogPost
from django.db.models import Q

class HommePagerView(TemplateView):
  template_name = "home.html"
  
  
  
class SearchResultsView(ListView):
  model = BlogPost
  template_name = "serach_results.html"
  def get_queryset(self) -> QuerySet[Any]:
    query = self.request.GET.get('q')
    keywords = query.split()
    for keyword in keywords:
      object_list = BlogPost.objects.filter(
      Q(title__icontains=keyword) | Q(content__icontains=keyword)
      )
    return object_list
