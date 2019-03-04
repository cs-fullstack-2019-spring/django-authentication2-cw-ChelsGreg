from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

# Create your views here.

# to require login
@login_required
def index(request):
    # to display logged in users' entries
    blogPost = Blog.objects.filter(blog_user=request.user)
    context = {
        'blogPost': blogPost
    }

    # to direct to index page
    return render(request, 'blogApp/index.html', context)

