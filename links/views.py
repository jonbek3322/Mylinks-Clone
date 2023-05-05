from django.shortcuts import render, redirect, get_object_or_404
from .models import Link
from .forms import LinkForm

# Create your views here.


def link_list_view(request):
    links = Link.objects.all()
    return render(request, 'link_list.html', {'links': links})


def create_link(request):
    
    form = LinkForm
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/havolalar/')
    return render(request, 'create_link.html', {'form': form})


def update_link(request, id):

    link = get_object_or_404(Link, id=id)
    form = LinkForm(instance=link)
    if request.method == 'POST':
        form = LinkForm(instance=link, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/havolalar/')
    return render(request, 'create_link.html', {'form': form})