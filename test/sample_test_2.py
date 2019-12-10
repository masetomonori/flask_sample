from flask_testing import TestCase

import sys
sys.path.append('../')
from src.api import app

class MyTest2(TestCase):

  def create_app(self):
    return app

  def test_1(self):
    response = self.client.get("todos/todo1")
    #print(response.json)
    self.assert_status(response, 200)
    self.assertEqual(response.json, dict(task='build an API'))

  def test_2(self):
    response = self.client.get("todos/todo2")
    #print(response.json)
    self.assert_status(response, 200)
    self.assertEqual(response.json, dict(task='?????'))



