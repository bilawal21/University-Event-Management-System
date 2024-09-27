from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UniversityUserCreationForm, PlayerForm, NoticeForm, EventForm, MatchForm
from .models import Player, Notice, Event, Team, Match

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UniversityUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UniversityUserCreationForm()
    return render(request, 'events/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'events/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'events/dashboard.html')

@login_required
def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save(commit=False)
            player.university = request.user
            player.save()
            form.save_m2m()
            return redirect('dashboard')
    else:
        form = PlayerForm()
    return render(request, 'events/add_player.html', {'form': form})

@login_required
def list_players(request):
    players = Player.objects.filter(university=request.user)
    return render(request, 'events/list_players.html', {'players': players})

def logout_view(request):
    logout(request)
    return redirect('login')

def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'events/notice_list.html', {'notices': notices})

def create_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.approved = False  
            notice.save()
            return redirect('notice_list')
    else:
        form = NoticeForm()
    return render(request, 'events/create_notice.html', {'form': form})

def approve_notices(request):
    unapproved_notices = Notice.objects.filter(approved=False)
    return render(request, 'events/approve_notices.html', {'notices': unapproved_notices})

def approve_notice(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    notice.approved = True
    notice.save()
    return redirect('approve_notices')

def notice_list(request):
    notices = Notice.objects.filter(approved=True)  
    return render(request, 'events/notice_list.html', {'notices': notices})

def admin_required(user):
    return user.is_superuser  

@user_passes_test(admin_required)
def approve_notices(request):
    unapproved_notices = Notice.objects.filter(approved=False)
    return render(request, 'events/approve_notices.html', {'notices': unapproved_notices})

def event_schedule(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'events/event_schedule.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_schedule')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

def standings(request):
    teams = Team.objects.all().order_by('-wins', '-draws', 'losses')
    return render(request, 'events/standings.html', {'teams': teams})

def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('standings')
    else:
        form = MatchForm()
    return render(request, 'events/create_match.html', {'form': form})