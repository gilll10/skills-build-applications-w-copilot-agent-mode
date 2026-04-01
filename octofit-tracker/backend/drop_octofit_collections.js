// Run this script in mongosh to drop all OctoFit collections and start fresh
use octofit_db
db.users.drop()
db.teams.drop()
db.activities.drop()
db.leaderboards.drop()
db.workouts.drop()
