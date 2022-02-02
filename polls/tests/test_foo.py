from django.test import TestCase


class FooTestCase(TestCase):
    def test_foo_1(self):
        self.assertEqual("foo", "foo")

    def test_foo_2(self):
        self.assertEqual("foo" * 2, "foofoo")
