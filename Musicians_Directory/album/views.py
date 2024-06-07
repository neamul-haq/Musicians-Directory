from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import forms
from . import models
from django.views.generic import CreateView,UpdateView,DeleteView
# Create your views here.

def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form': album_form})


def edit_album(request, id):
    album = models.Album.objects.get(pk=id) 
    album_form = forms.AlbumForm(instance=album)
    # print(post.title)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album) 
        if album_form.is_valid(): 
            album_form.save()
            return redirect('homepage') 
    
    return render(request, 'add_album.html', {'form' : album_form})


@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        return super().form_valid(form)
    
    
@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    

@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'