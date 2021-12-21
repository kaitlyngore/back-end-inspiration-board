from app import db
from flask import current_app

class Card(db.Model):
     # rename to just id on both models - from Ansel
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'), primary_key=True, nullable=False)