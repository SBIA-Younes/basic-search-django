from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from .models import BlogPost
from django.db.models import Q

class HommePagerView(ListView):
    model = BlogPost
    template_name = "home.html"
    context_object_name = "blogs"
    paginate_by = 10
  
  
class SearchResultsView(ListView):
    model = BlogPost
    template_name = "serach_results.html"
    context_object_name = "blogs"
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('q')
        if query :
            return BlogPost.objects.filter(title__icontains=query)
        return BlogPost.objects.all()


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


