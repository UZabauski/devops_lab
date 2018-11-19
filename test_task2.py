from unittest import TestCase
import task2


class TestTask2(TestCase):
    def test_year(self):
        self.assertTrue(task2.year(2012))
        self.assertFalse(task2.year(2011))
