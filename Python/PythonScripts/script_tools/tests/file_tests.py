from components.test_base import TestBase
from functions.file_tools import get_file_path as get_path
from functions.file_tools import print_files_at_location as print_path


class TestGeometricProgression(TestBase):

    def test_basic_functionality(self):
        expected_result = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800]
        self.assertEqual(calc_geo_progress(100, 12, 2), expected_result)

    def test_zero_initial_value(self):
        expected_result = [0, 0, 0, 0, 0]
        self.assertEqual(calc_geo_progress(0, 5, 2), expected_result)

    def test_zero_ratio(self):
        expected_result = [100, 0, 0, 0, 0]
        self.assertEqual(calc_geo_progress(100, 5, 0), expected_result)


if __name__ == '__main__':
    unittest.main()
