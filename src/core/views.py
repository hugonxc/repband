from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from core.models import Music, Repertory

from core.forms import SignUpForm, LoginForm, NewMusicForm, CreateRepertoryForm

def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()

    return render(request, 'index.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def profile(request):
    print("oi")
    user = User.objects.get(username=request.user)
    repertories = Repertory.objects.filter(owner=user)

    return render(request, 'account/profile.html', {'repertories': repertories})




## Music section
@login_required
def add_new_music(request):
    if request.method == "POST":
        form = NewMusicForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data.get('name')
            artist = form.cleaned_data.get('artist')
            yt_link = form.cleaned_data.get('yt_link')
            
            Music.objects.create(name=name, 
                                artist=artist,
                                yt_link=yt_link)
            return redirect('profile')
    else:
        form = NewMusicForm()

    return render(request, 'repertory/add_new_music.html', {'form': form})


@login_required
def create_repertory(request):
    if request.method == "POST":
        form = CreateRepertoryForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data.get('name')
            note = form.cleaned_data.get('note')
            user = User.objects.get(username=request.user)

            Repertory.objects.create(owner=user,
                                   name=name, 
                                   note=note)
            return redirect('profile')
    else:
        form = CreateRepertoryForm()

    return render(request, 'repertory/create_repertory.html', {'form': form})



@login_required
def manage_repertory(request, pk):
    print("PKa", pk)
    repertory = Repertory.objects.get(pk=pk)
    musics = repertory.repertory_musics
    
    if musics is not None:
        print("Ma", musics)
    else:
        print("M", musics)

    # if request.method == "POST":
    #     form = CreateRepertoryForm(request.POST)
        
    #     if form.is_valid():
    #         name = form.cleaned_data.get('name')
    #         note = form.cleaned_data.get('note')
    #         user = User.objects.get(username=request.user)

    #         Repertory.objects.create(owner=user,
    #                                name=name, 
    #                                note=note)
    #         return redirect('profile')
    # else:
    #     form = CreateRepertoryForm()

    return render(request, 'repertory/manage_repertory.html', {'repertory': repertory})




@login_required
def add_music_to_repertory(request):
    pass



@login_required
def list_repertory(request):
    pass