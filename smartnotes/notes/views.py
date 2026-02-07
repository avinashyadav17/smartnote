from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'notes/home.html')


# CREATE
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('/notes/')
    else:
        form = NoteForm()

    return render(request, 'notes/create_note.html', {'form': form})


@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/list.html', {'notes': notes})


# UPDATE

@login_required
def update_note(request, id):
    note = get_object_or_404(Note, id=id)

    form = NoteForm(request.POST or None, instance=note)

    if form.is_valid():
        form.save()
        return redirect('/notes/')

    return render(request, 'notes/create_note.html', {'form': form})



@login_required
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('/notes/')

def login_user(request):

    if request.method == "POST":

        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is not None:
            login(request, user)   # creates session + cookie
            return redirect('/notes/')

        else:
            return render(request, 'notes/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'notes/login.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')

from django.http import HttpResponse


def set_session(request):
    request.session['username'] = 'avinash'
    return HttpResponse("Session set!")


def get_session(request):
    name = request.session.get('username')
    return HttpResponse(name if name else "No session found")
