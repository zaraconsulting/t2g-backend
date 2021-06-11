from app import db


class Coach(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    players = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Coach: {self.email}>'

    def from_dict(self, data):
        for field in ['first_name', 'last_name', 'email', 'role_id']:
            setattr(self, field, data[field])

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'role': self.role_id,
            'players': []
        }


#revisit this section
# class User(db.Model):
#     coaches = db.Column(db.String)
#     recruiters = db.Column(db.String)
#     players = db.Column(db.String)

#     def save(self):
#         db.session.add(self)
#         db.session.commit()

#     def __repr__(self):
#         return f'<User: {self.category}>'

#     def from_dict(self, data):
#         for field in ['category', 'position']:
#             setattr(self, field, data[field])

#     def to_dict(self):
#         return {
#             'category': self.category,
#             'position': self.position

#         }
