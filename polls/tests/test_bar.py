from django.test import TestCase


class BArTestCase(TestCase):
    def test_bar_1(self):
        self.assertEqual("bar", "bar")

    def test_bar_2(self):
        self.assertEqual("bar" * 2, "barbar")
