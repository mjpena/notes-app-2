from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from notes.models import Note, Tag
from notes.forms import NoteForm
# Create your views here.

def home_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        auth = authenticate(username = username, password=password)
        if auth is not None:
            login(request, auth)
            return HttpResponseRedirect(reverse('notes:home'))
        else:
            messages.add_message(request, messages.INFO, "Authentication Failed")
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'home.html')
    
def index_view(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html',{'notes':notes})

def add_note(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Note Added!')
			return HttpResponseRedirect(reverse('notes:index'))
	else:
		form = NoteForm()
	return render(request, 'notes/addnote.html', {'form':form})
    
    
