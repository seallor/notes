from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from django.shortcuts import redirect


def index(request):
    notes = Note.objects.order_by('-unique_words')
    if request.method == "POST":

        form = NoteForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.publish()
            return redirect('index')

    else:
        form = NoteForm()

    return render(request, 'note/index.html', {'notes': notes, 'form': form})


# Create your views here.
