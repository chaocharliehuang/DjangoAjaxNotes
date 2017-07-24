from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import Note

def index(request):
    context = {'notes': []}
    notes = Note.objects.all()
    for note in notes:
        context['notes'].append({
            'id': note.id,
            'title': note.title,
            'description': note.description
        })
    return render(request, 'notes/index.html', context)

def add(request):
    if request.method == 'POST':
        Note.objects.create(title=request.POST['title'])
        return redirect(reverse('notes:index'))
    else:
        return redirect(reverse('notes:index'))

def delete(request, id):
    Note.objects.get(id=id).delete()
    return redirect(reverse('notes:index'))

def save(request, id):
    note = Note.objects.get(id=id)
    note.description = request.POST['description']
    note.save()
    return render(request, 'notes/notes.html', {'notes': Note.objects.all()})