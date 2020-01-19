from app import db

class Living_room(db.Model):
    __tablename__  = 'living_room'
    room_number = db.Column('room_number', db.Integer, primary_key = True)
    floor = db.Column('floor', db.Integer)
    room_class = db.Column('room_class', db.String(220))

    def __init__(self, room_number, floor, room_class):
        self.room_number = room_number
        self.floor = floor
        self.room_class = room_class

    def __repr__(self):
        return '<id {}>'.format(self.room_number)

    def serialize(self):
        return {
            'room_number': self.room_number,
            'floor': self.floor,
            'room_class': self.room_class
        }