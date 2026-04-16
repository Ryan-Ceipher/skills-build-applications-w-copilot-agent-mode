from djongo import models
from bson import ObjectId

# User model
class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)

# Team model
class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

# Activity model
class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

# Leaderboard model
class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

# Workout model
class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.CharField(max_length=50)
