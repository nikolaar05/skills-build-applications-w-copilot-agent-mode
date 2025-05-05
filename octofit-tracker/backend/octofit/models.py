from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        db_table = 'activity'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'workouts'
