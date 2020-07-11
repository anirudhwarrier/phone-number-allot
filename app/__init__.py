from flask_restplus import Api
from flask import Blueprint

from .main.controller.phone_controller import api as phone_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='PHONE-NUMBER-ALLOTMENT-SYSTEM',
          version='1.0',
          description='Assign phone number to clients based on availability.'
          )

api.add_namespace(phone_ns, path='/phone')