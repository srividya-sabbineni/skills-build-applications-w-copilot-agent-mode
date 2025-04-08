from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe", password="password123")
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", password="password123")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha")
        team2 = Team.objects.create(name="Team Beta")

        # Add users to teams
        team1.members.add(user1)
        team2.members.add(user2)

        # Create test activities
        Activity.objects.create(user=user1, type="Running", duration=30, date="2025-04-07")
        Activity.objects.create(user=user2, type="Cycling", duration=45, date="2025-04-07")

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=150)

        # Create test workouts
        Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
        Workout.objects.create(name="Sit-ups", description="Do 30 sit-ups")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
