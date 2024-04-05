from django.shortcuts import render
from core.models import Comment

# Create your views here.



def comments(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments
    }
    return render(request, 'comments.html', context)


def check_spam(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments
    }
    return render(request, 'partials/comments-spam.html', context)

