from app import db

class Posting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    school = db.Column(db.String)
    title = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Posting: {self.url}>'

    def from_dict(self, data):
        for field in ['url', 'description', 'school', 'title']:
            setattr(self, field, data[field])

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'description': self.description,
            'school': self.school,
            'title': self.title
        }