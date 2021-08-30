import unittest

from extraction import Playlist


class TestExtraction(unittest.TestCase):
    def setUp(self):
        self.object = Playlist('05kISTbCkMooGzBj5h28tp?si=ea26d808213c4a6a')  # my own main playlist

    def test_get_playlist(self):
        """initialization test"""
        self.assertIsInstance(self.object.playlist, list)
        self.assertIsInstance(self.object.playlist[0], dict)

    def test_shuffle(self):
        temp = self.object.playlist.copy()
        self.object.shuffle()
        self.assertNotEqual(self.object.playlist, temp)

        self.object.playlist = None
        self.assertRaises(TypeError, self.object.shuffle)  # call the method

    def test_get_images_list(self):
        self.assertRaises(ValueError, lambda: self.object.get_images_list(img_size=63))  # if an option is required
        self.assertIsInstance(self.object.get_images_list(img_size=64), list)
        self.assertIsInstance(self.object.get_images_list(img_size=64)[0], str)

    @unittest.skip
    def test_get_human_readable(self):
        pass


if __name__ == '__main__':
    unittest.main()
