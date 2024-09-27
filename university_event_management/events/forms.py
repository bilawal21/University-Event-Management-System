from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UniversityUser, Player, Notice, Event, Match

class UniversityUserCreationForm(UserCreationForm):
    class Meta:
        model = UniversityUser
        fields = ('university_name', 'location', 'email', 'password1', 'password2')

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'game', 'student_class', 'photo']

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description', 'event_date', 'deadline']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'venue']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team1', 'team2', 'date', 'team1_score', 'team2_score']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'team1_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'team2_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }