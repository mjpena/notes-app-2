from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from notes.models import Note, Tag
from notes.forms import NoteForm
# Create your views here.

def home_view(request):
    return render(request, 'home.html')

    
def index_view(request):
    notes = Note.objects.all().order_by('-pubTime')
    return render(request, 'notes/index.html',{'notes':notes})


def add_note(request):
    id = request.GET.get('id', None)
    if id is None:
        note = None
    else:
        note = get_object_or_404(Note, id=id)
	
	if request.method == 'POST':
		if request.POST.get('control') == 'delete':
			note.delete()
			messages.add_message(request, messages.INFO, 'Note Deleted!')
			return HttpResponseRedirect(reverse('notes:index'))
		
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Note Added!')
			return HttpResponseRedirect(reverse('notes:index'))
	else:
	     form = NoteForm(instance=note)
		
	return render(request, 'notes/addnote.html', {'form':form})
    
