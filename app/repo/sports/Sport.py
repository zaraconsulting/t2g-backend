from app import db


class Sport(db.Model):
    id = db.Column(db.String, primary_key=True)
    category = db.Column(db.String)
    position = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Sport: {self.category}>'

    def from_dict(self, data):
        for field in ['category', 'position']:
            setattr(self, field, data[field])

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'position': self.position
        }
