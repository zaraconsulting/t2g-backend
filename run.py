from app import create_app
from app import db
from app.repo.users.User import User

app = create_app()

@app.shell_context_processor
def make_context():
    return dict(db=db, User=User)