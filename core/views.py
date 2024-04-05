from django.shortcuts import render
from core.models import Comment

# Create your views here.



def comments(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments
    }
    return render(request, 'comments.html', context=)

