from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Note
from .forms import NoteForm

# Create your views here.

def index(request):
    return render(request, "main_page.html")


def return_simple_html(request): 
    blog_entries = \
        [{"title": "Something",
         "body": "one"},
         {"title": "Anything",
         "body": "two"}]


    return render(request, 'first_sub.html', 
                  context={"blog_entries":blog_entries})

def return_html_page(request):
    return render(request, "second_page.html")
                  

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



def return_note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})

def return_note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note_detail.html', {'note': note})

def return_note_page(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')  
    else:
        form = NoteForm()
    return render(request, 'note.html', {'form': form})

def return_delete_note(request, pk):
    note = get_object_or_404(Note, pk = pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note_confirm_delete.html', {'note': note})





# def return_note_page(request):
#     if request.method == 'POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('note_list')  
#     else:
#         form = NoteForm()
#     return render(request, 'note.html', {'form': form})