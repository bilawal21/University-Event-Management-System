from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class UniversityUser(AbstractUser):
    university_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'university_name', 'location']

    def __str__(self):
        return self.university_name

class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Player(models.Model):
    university = models.ForeignKey(UniversityUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    age = models.PositiveBigIntegerField()
    photo = models.ImageField(upload_to='player_photos/')
    student_class = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)  
    
    def __str__(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    games_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_points(self):
        """Calculate points based on wins/draws/losses."""
        return self.wins * 3 + self.draws

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    date = models.DateField()
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    
    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} on {self.date}"
    
    def save(self, *args, **kwargs):
        super(Match, self).save(*args, **kwargs)
        self.update_team_standings()

    def update_team_standings(self):
        if self.team1_score > self.team2_score:
            self.team1.wins += 1
            self.team2.losses += 1
        elif self.team1_score < self.team2_score:
            self.team1.losses += 1
            self.team2.wins += 1
        else:
            self.team1.draws += 1
            self.team2.draws += 1
        
        self.team1.games_played += 1
        self.team2.games_played += 1
        self.team1.save()
        self.team2.save()