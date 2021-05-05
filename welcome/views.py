from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'admin',
        'title': 'Test Post',
        'content': 'The world is full of ACKs',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'Routing in django is performed by urls.py, which pulls views and template htmls',
        'date_posted':'April 20, 2021'

    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'Template inheritance with basecase implemented',
        'date_posted':'April 20, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'Boots are strapped with bootstrap (slow UI upgrade)',
        'date_posted':'April 21, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    },
    {
        'author': 'Joshua Dark',
        'title': 'Development post',
        'content': 'The beginning of an ambitious workflow is beginning to work with flow',
        'date_posted':'April 19, 2021'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'welcome/home.html',context)


def about(request):
    return render(request, 'welcome/about.html')

# Create your views here.
