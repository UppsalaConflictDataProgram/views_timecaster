
import json
from datetime import date
from app import Query,Response,date_to_mid,mid_to_date
import unittest

class TestTimecaster(unittest.TestCase):
    def test_conversion(self):
        for n in range(12):
            mid = n+1
            d = mid_to_date(mid)
            m = date_to_mid(d)
            self.assertEqual(mid,m)
            self.assertEqual(d,date(year=1980,month=mid,day=1))

