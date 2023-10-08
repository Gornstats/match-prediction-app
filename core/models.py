from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Extend standard user model in case of future enhancements
class User(AbstractUser):
    pass

# Soccer teams available for tipping
class Team(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
# The matches played by the teams. Can have null goals if the game is yet to be played
class Fixture(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_fixtures')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_fixtures')
    home_goals = models.IntegerField(blank=True, null=True)
    away_goals = models.IntegerField(blank=True, null=True)
    
# Tip made by a user, with home and away goal predictions
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='predictions')
    home_goals = models.IntegerField(validators=[MinValueValidator(0)])
    away_goals = models.IntegerField(validators=[MinValueValidator(0)])

