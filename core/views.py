from django.shortcuts import render
from core.models import Comment
from core.spam_model import predict_spam

# Create your views here.



def comments(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments
    }
    return render(request, 'comments.html', context)


def check_spam(request):
    comments = Comment.objects.all()
    predictions = predict_spam(comments.values_list('text', flat=True))
    context = {
        'comments': zip(comments, predictions)
    }
    return render(request, 'partials/comments-spam.html', context)

