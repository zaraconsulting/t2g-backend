from app import db


class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    #  chats not included for now
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    role = db.Column(db.Integer)
    team = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Recruiter: {self.email}>'

    def from_dict(self, data):
        for field in ['first_name', 'last_name', 'email', 'role', 'team']:
            setattr(self, field, data[field])

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

