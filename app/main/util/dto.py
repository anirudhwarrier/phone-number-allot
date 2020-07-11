from flask_restplus import Namespace, fields

class PhoneDto:
    api = Namespace('phone', description='phone number related operations')
    phone = api.model('phone', {
        'number': fields.String(required=True, description='phone number'),
        'client_id': fields.String(description='client Identifier')
    })