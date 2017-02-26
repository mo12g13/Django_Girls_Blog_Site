from django.shortcuts import render, render_to_response
from . models import Post
from django.utils import timezone
from django.template.response import TemplateResponse

# Create your views here.
# This is the view that display the data in the  html form

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

