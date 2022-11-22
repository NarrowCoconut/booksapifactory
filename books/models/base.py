from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.Text, index=True, unique=True)
    rating = db.Column(db.Numeric(), index=True, unique=False)
    image = db.Column(db.String(120), index=True, unique=True)
    url = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
         return '<Post: %r>' % (self.title)