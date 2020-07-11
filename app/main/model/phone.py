
from .. import db
import datetime

class Phone(db.Model):
    """ Phone Model for storing user related details """
    __tablename__ = "phone"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(10), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    client_id = db.Column(db.String(100))


    def __repr__(self):
        return "<Phone '{}'>".format(self.number)
