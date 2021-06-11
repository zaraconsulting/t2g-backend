from flask import current_app as app

from app.blueprints.api.auth import bp as auth
app.register_blueprint(auth)

from app.blueprints.api.coach import bp as coaches
app.register_blueprint(coaches)

from app.blueprints.api.academics import bp as academics
app.register_blueprint(academics)

from app.blueprints.api.available_videos import bp as available_videos
app.register_blueprint(available_videos)

from app.blueprints.api.players import bp as players
app.register_blueprint(players)

from app.blueprints.api.positions import bp as positons
app.register_blueprint(positons)

from app.blueprints.api.recruiters import bp as recruiters
app.register_blueprint(recruiters)

from app.blueprints.api.sports import bp as sports
app.register_blueprint(sports)

from app.blueprints.api.stats import stats as bp
app.register_blueprint(bp)

from app.blueprints.api.postings import bp as postings
app.register_blueprint(postings)
