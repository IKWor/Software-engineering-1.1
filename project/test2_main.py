import unittest
from main import voicer

class TestMain(unittest.TestCase):
    def test_voicer(self):
        text = "Привет, мир!"
        audio = voicer(text)
        self.assertIsInstance(audio, torch.Tensor)
        self.assertEqual(audio.shape[0], 1)
        self.assertEqual(audio.shape[1], 48000)

if __name__ == '__main__':
    unittest.main()
