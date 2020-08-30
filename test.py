import unittest
from transmit.io import YamlFormatter
from transmit.io import YamlError
from transmit.io import FileWriter
from transmit.audio import AudioFile


class TestYamlWriter(unittest.TestCase):
    def test_yaml_write_nothing(self):
        """
        YamlWriter can output nothing when given nothing
        """
        self.assertEqual(YamlFormatter().format({}), '{}\n')
        self.assertEqual(YamlFormatter().format(''), "''\n")
        self.assertRaises(YamlError, YamlFormatter().format, None)

    def test_yaml_write_single(self):
        """
        YamlWriter can output single key-value pair
        """
        data = {'hello': 'friends'}
        result = YamlFormatter().format(data)

        self.assertEqual(result, 'hello: friends\n')

    def test_yaml_write_multiple(self):
        """
        YamlWriter can output multiple key-value pairs
        """
        data = {
            'goodbye': 'world',
            'stonk_value': 1200
        }
        result = YamlFormatter().format(data)

        self.assertEqual(result, 'goodbye: world\nstonk_value: 1200\n')


class TestFileWriter(unittest.TestCase):
    def test_file_write(self):
        """
        FileWriter does not blowup
        """
        data = 'kinda bug and kinda snacks!'
        FileWriter().write(data)

        self.assertTrue(True)


class TestAudioFile(unittest.TestCase):
    def test_audio_duration(self):
        """
        AudioFile can get duration in seconds
        """
        audio = AudioFile('intro100.mp3')
        self.assertEqual(audio.duration, 29.592)
