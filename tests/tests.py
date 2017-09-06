from flask import Flask
from flask_testing import TestCase
from app import app


class TestEndpoints(TestCase):
    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        return app

    def test_non_valid_endpoint(self):
        response = self.client.get("/helloworld")
        self.assertEquals(response.json, dict(natural=None, unix=None))

    def test_natural_timestamp(self):
        response = self.client.get("/December%2015,%202015")
        self.assertEquals(response.json, dict(natural="December 15, 2015", unix=1450137600))

    def test_unix_timestamp(self):
        response = self.client.get("/1450137600")
        self.assertEquals(response.json, dict(natural="December 15, 2015", unix=1450137600))
