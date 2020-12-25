from server import db, session, base


class Users(base):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    pwd = db.Column(db.String(100), nullable=False)
    path = db.Column(db.String(100), nullable=False, unique=True)
