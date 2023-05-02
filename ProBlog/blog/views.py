from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'AviralGupta',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'March 30, 2023'
    },

    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'March 30, 2023'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
