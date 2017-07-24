from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Note

def index(request):
    return render(request, 'notes/index.html', {'notes': Note.objects.order_by("-created_at")})

def add(request):
    if request.method == 'POST':
        Note.objects.create(title=request.POST['title'])
        return render(request, 'notes/notes.html', {'notes': Note.objects.order_by("-created_at")})
    else:
        return redirect(reverse('notes:index'))

def delete(request, id):
    if request.method == 'POST':
        Note.objects.get(id=id).delete()
        return render(request, 'notes/notes.html', {'notes': Note.objects.order_by("-created_at")})
    else:
        return redirect(reverse('notes:index'))

def save(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.description = request.POST['description']
        note.save()
        return render(request, 'notes/notes.html', {'notes': Note.objects.order_by("-created_at")})
    else:
        return redirect(reverse('notes:index'))