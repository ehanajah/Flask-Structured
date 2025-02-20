from app.extensions import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id
