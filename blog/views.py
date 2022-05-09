

from django.views.generic import ListView
from blog.models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'base.html'
    context_object_name = 'blog'