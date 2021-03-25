from unittest import TestCase
import json

from app import app
from api.utils.error import error_message


class TestValidateInput(TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_validate_input_invalid_json(self):
        resp = self.client.post('/api/v1/sanitized/input/',
                                data=json.dumps(dict(payload='Foo')),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_validate_input_empty_payload(self):
        with app.app_context():
            resp = self.client.post('/api/v1/sanitized/input/',
                                    data=json.dumps(dict(payload='')),
                                    content_type='application/json')
            self.assertEqual(resp.status_code, 400)
            self.assertEqual(str(resp.get_data(), 'utf-8'), error_message()[0])

    def test_validate_input_missing_payload(self):
        with app.app_context():
            resp = self.client.post('/api/v1/sanitized/input/',
                                    data=json.dumps(dict(paload='')),
                                    content_type='application/json')
            self.assertEqual(resp.status_code, 400)
            self.assertEqual(str(resp.get_data(), 'utf-8'),
                             error_message("MISSING_PAYLOAD")[0])

    def test_validate_input_invalid_input(self):
        with app.app_context():
            resp = self.client.post('/api/v1/sanitized/input/',
                                    data=json.dumps(dict(payload=99)),
                                    content_type='application/json')
            self.assertEqual(resp.status_code, 400)
            self.assertEqual(str(resp.get_data(), 'utf-8'), error_message()[0])

    def test_validate_input_sanitized_input(self):
        with app.app_context():
            resp = self.client.post('/api/v1/sanitized/input/',
                                    data=json.dumps(dict(payload="Bar__\n")),
                                    content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(str(resp.get_data(), 'utf-8'),
                             '{"result":"sanitized"}\n')

    def test_validate_input_unsanitized_input(self):
        with app.app_context():
            resp = self.client.post('/api/v1/sanitized/input/',
                                    data=json.dumps(dict(payload="Foo@")),
                                    content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(str(resp.get_data(), 'utf-8'),
                             '{"result":"unsanitized"}\n')
