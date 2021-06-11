from app import db

class Available_Videos(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    thumbnail_url = db.Column(db.String)
    video_url = db.Column(db.String)
    video_size = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Video: {self.video_url}>'

    def from_dict(self, data):
        for field in ['thumbnail_url', 'video_url', 'video_size']:
            setattr(self, field, data[field])

    def to_dict(self):
        return {
            'id': self.id,
            'thumbnail_url': self.thumbnail_url,
            'video_url': self.video_url,
            'video_size': self.video_size
        }
