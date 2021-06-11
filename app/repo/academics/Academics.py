from app import db


class Academics(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    act = db.Column(db.Integer)
    gpa = db.Column(db.Float)
    sat = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<ACT: {self.act}, GPA: {self.gpa}, SAT: {self.sat}>'

    def from_dict(self, data):
        for field in ['act', 'gpa', 'sat']:
            setattr(self, field, data[field])

    def to_dict(self):
        return {
            'id': self.id,
            'act': self.act,
            'gpa': self.gpa,
            'sat': self.sat
        }
