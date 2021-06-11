from app import db

class Stat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Stat: {self.value}>'

    def from_dict(self, data):
        for field in ['name', 'value']:
            setattr(self, field, data[field])

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value
        }
