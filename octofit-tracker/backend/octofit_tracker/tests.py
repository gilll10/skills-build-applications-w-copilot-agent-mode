from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='cardio')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=10, week=1)

    def test_user(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.team, self.team)

    def test_activity(self):
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.type, 'Running')

    def test_workout(self):
        self.assertEqual(self.workout.suggested_for, 'cardio')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.team, self.team)
        self.assertEqual(self.leaderboard.points, 10)
