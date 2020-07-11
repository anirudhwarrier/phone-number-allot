import uuid
import datetime
import random

from app.main import db
from app.main.model.phone import Phone


def save_new_phone(data):
    number = int(data['number']) if ('number' in data) else random.randint(1111111111,9999999999)
    number_range = number in range(1111111111,9999999999) 
    number_exist = Phone.query.filter_by(number=str(number)).first()

    if not number_range:
        response_object = {
            'status': 'fail',
            'message': 'Invalid Number. Please try different number',
        }
        return response_object, 410
    if not number_exist:
        new_phone = Phone(
            client_id=str(uuid.uuid4()),
            number=str(number),
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_phone)
        response_object = {
            'status': 'success',
            'number': str(number)
        }
        return response_object, 201 
    else:
        response_object = {
            'status': 'fail',
            'message': 'Number already in use. Please try different number',
        }
        return response_object, 409

def get_all_phones():
    return Phone.query.all()


def get_a_phone(client_id):
    return Phone.query.filter_by(client_id=client_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

