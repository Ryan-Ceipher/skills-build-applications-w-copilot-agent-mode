
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):


        # Clear existing data using PyMongo
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]
        db.user.drop()
        db.team.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workout.drop()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Create activities
        Activity.objects.create(user=tony, type='Running', duration=30, date='2024-04-01')
        Activity.objects.create(user=steve, type='Cycling', duration=45, date='2024-04-02')
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date='2024-04-03')
        Activity.objects.create(user=clark, type='Yoga', duration=20, date='2024-04-04')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Full Body Blast', description='A full body workout', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
