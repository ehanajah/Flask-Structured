from app.extensions import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    blogs = db.relationship('Blog', backref='author', lazy=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email
