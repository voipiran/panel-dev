import shutil
import tempfile
import unittest
from qpanel.upgrader import (__first_line as firstline,
    get_current_version, check_require_upgrade, get_stable_version)
import qpanel


class UpgradeTestClass(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_first_line(self):
        content = 'a\n\b\t\b'
        self.assertEqual(firstline(content), 'a')
        self.assertNotEqual(firstline(content), 'ab')

    def test_version(self):
        self.assertEqual(get_current_version(), qpanel.__version__)
        self.assertNotEqual(get_current_version(), '0.11.0')

    def test_check_require_upgrade(self):
        stable = '0.10'
        current = '0.9'
        dev = '1.11.0'

        self.assertEqual(check_require_upgrade(dev, stable), False)
        self.assertEqual(check_require_upgrade(current, stable), True)


    def test_request_estable_version(self):
        """
            Test for request to stable version name
            Maybe this can be a mockup but I used to check requests and get compatability
        """
        current_stable_version = get_stable_version()
        self.assertIsNotNone(current_stable_version)

# runs the unit tests
if __name__ == '__main__':
    unittest.main()
