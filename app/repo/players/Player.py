from app import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    first_login = db.Column(db.Integer)
    email = db.Column(db.String, unique=True)
    role = db.Column(db.Integer)
    team = db.Column(db.String)
    # stream_data = db.Column(db.String)
    # player_questions = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Player: {self.email}>'

    def from_dict(self, data):
        for field in ['first_name', 'last_name', 'email', 'role', 'team']:
            setattr(self, field, data[field])

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'first_login': self.first_login,
            'email': self.email,
            'role': self.role,
            'team': self.team
        }
