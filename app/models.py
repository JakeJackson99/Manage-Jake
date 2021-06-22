import datetime

from app import db


"""
TODO
turn date into rough estimate, i.e. "3 days ago"
"""


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note_content = db.Column(db.String(280), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Note: %r>' % self.note_content
