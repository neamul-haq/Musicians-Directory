from django.shortcuts import render, redirect
from . import forms
from . import models
from album.models import Album
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form': musician_form})


def edit_musician(request, id):
    album = Album.objects.get(pk=id)
    musician = album.musician
    musician_form = forms.MusicianForm(instance=musician)
    # print(musician.title)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician) 
        if musician_form.is_valid(): 
            musician_form.save()
            return redirect('homepage') 
    
    return render(request, 'add_musician.html', {'form' : musician_form})

def delete_musician(request, id):
    album = Album.objects.get(pk=id)
    musician = album.musician
    musician.delete()
    return redirect('homepage')


