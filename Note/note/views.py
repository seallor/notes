from django.shortcuts import render
from .models import Note


def index(request):
    notes = Note.objects.order_by('unique_words')
    return render(request, 'note/index.html', {'notes': notes})
# Create your views here.
