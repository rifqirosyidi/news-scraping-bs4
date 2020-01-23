from django.shortcuts import render, redirect, get_object_or_404
from .forms import NotesModelForm
from .models import Note


# Create your views here.
def create_notes(request):
    if request.method == 'POST':
        form = NotesModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/notes/')
    else:
        form = NotesModelForm()
    context = {
        'form': form,
        'naming': 'Create'
    }
    return render(request, 'notes/notes_form.html', context)


def list_notes(request):
    all_notes = Note.objects.all()
    context = {
        'all_notes': all_notes
    }
    return render(request, 'notes/notes_list.html', context)


def delete_notes(request, id):
    note_to_delete = get_object_or_404(Note, pk=id)
    if request.user == note_to_delete.user:
        note_to_delete.delete()

    return redirect('/notes/')