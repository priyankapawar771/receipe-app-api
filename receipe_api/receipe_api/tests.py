'''Sample Tests'''

from django.test import SimpleTestCase
from . import calc

class CalcTest(SimpleTestCase):
    def test_add_number(self):
        res = calc.add(2,2)
        self.assertEqual(res,4)
