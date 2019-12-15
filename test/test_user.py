import unittest
from flask_testing import TestCase

class TestNotRenderTemplate(TestCase):

    render_templates = False

    def test_assert_not_process_the_template(self):
        response = self.client.get("/Users/")

if __name__ == '__main__':
    unittest.main()
    