from flask import request
from flask_restplus import Resource

from ..util.dto import PhoneDto
from ..service.phone_service import save_new_phone, get_all_phones, get_a_phone

api = PhoneDto.api
_phone = PhoneDto.phone


@api.route('/')
class PhoneList(Resource):
    @api.doc('list_of_registered_phones')
    @api.marshal_list_with(_phone)
    # @api.marshal_list_with(_phone, envelope='data')
    def get(self):
        """List all registered phone numbers"""
        return get_all_phones()

    # @api.expect(_phone, validate=True)
    @api.response(201, 'Phone number successfully allotted.')
    @api.doc('allot a new phone number')
    def post(self):
        """Allot random phone number"""
        return save_new_phone({})

@api.route('/<phone_num>')
@api.param('phone_num', 'Fancy Phone number')
class Phone(Resource):
    @api.doc('request fancy number')
    def post(self, phone_num):
        """Allot fancy phone number"""
        return save_new_phone({'number':phone_num})