from django.test import TestCase
import datetime
from datehelpers import isPublicHoliday

# Create your tests here.
class DatehelpersTests(TestCase):

    def test_is_public_holiday(self):
        """
        isPublicHoliday(date) returns true for public holiays and false for not public holidays
        """
        public_holidays= public_holidays = [(1, 1), (21, 3), (14, 4), (17, 4), (27, 4), (1, 5), (16, 6), (9, 8), (24, 9), (16, 12), (25, 12),
                       (26, 12)]
        youth_day = datetime.date(2017,6,16)
        self.assertIs(isPublicHoliday(youth_day), True)