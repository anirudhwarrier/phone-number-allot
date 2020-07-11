import unittest

from app.main import db
import json
from app.test.base import BaseTestCase


def request_new_phone(self):
    return self.client.post(
        '/phone/',
    )

def request_fancy_phone(self):
    return self.client.post(
        '/phone/1234567898',
    )

def request_invalid_phone(self):
    return self.client.post(
        '/phone/123',
    )


def get_phones(self):
    return self.client.get(
        '/phone/',
    )


class TestPhone(BaseTestCase):
    def test_request_new_phone(self):
        """ Test for new number allotment """
        with self.client:
            response = request_new_phone(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['number'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_request_fancy_phone(self):
        """ Test for fancy number allotment """
        with self.client:
            response = request_fancy_phone(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            print(data['number'])
            self.assertTrue(data['number'] == '1234567898')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_request_invalid_fancy_phone(self):
        """ Test for invalid fancy number allotment """
        with self.client:
            response = request_invalid_phone(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Invalid Number. Please try different number')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 410)

    def test_request_duplicate_fancy_phone(self):
        """ Test for duplicate number check """
        with self.client:
            request_fancy_phone(self)
            response = request_fancy_phone(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Number already in use. Please try different number')
            
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_get_phone(self):
        """ Test for number retreival """
        with self.client:
            request_fancy_phone(self)
            request_new_phone(self)
            response = get_phones(self)
            data = json.loads(response.data.decode())
            self.assertTrue(len(data)== 2)
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
