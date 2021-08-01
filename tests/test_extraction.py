import unittest

from extraction import Playlist


class TestExtraction(unittest.TestCase):
    def setUp(self):
        self.object = Playlist('05kISTbCkMooGzBj5h28tp?si=ea26d808213c4a6a')  # my own main playlist

    def test_get_raw(self):
        """initialization test"""
        self.assertIsInstance(self.object.playlist, list)
        self.assertIsInstance(self.object.playlist[0], dict)

    @unittest.skip
    def test_shuffle(self):
        pass

    @unittest.skip
    def test_get_human_readable(self):
        pass

    @unittest.skip
    def test_get_images_list(self):
        pass


if __name__ == '__main__':
    unittest.main()
