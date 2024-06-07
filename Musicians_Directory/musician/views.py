from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
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

@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


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

@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(DeleteView):
    model = models.Musician
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'
    
    
def delete_musician(request, id):
    album = Album.objects.get(pk=id)
    musician = album.musician
    musician.delete()
    return redirect('homepage')


