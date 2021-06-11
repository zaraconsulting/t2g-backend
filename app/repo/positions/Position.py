from app import db

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    team = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Player: {self.email}>'

    def from_dict(self, data):
        for field in ['first_name', 'last_name', 'team']:
            setattr(self, field, data[field])

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'team': self.team
        }
