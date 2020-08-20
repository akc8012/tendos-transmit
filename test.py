import unittest
from transmit.YamlWriter import YamlWriter


class TestYamlWriter(unittest.TestCase):
    def test_yaml_write_none(self):
        """
        YamlWriter can output nothing when given nothing
        """
        data = {}
        result = YamlWriter().write(data)

        self.assertEqual(result, '{}\n')

    def test_yaml_write_single(self):
        """
        YamlWriter can output single key-value pair
        """
        data = {'hello': 'friends'}
        result = YamlWriter().write(data)

        self.assertEqual(result, 'hello: friends\n')

    def test_yaml_write_multiple(self):
        """
        YamlWriter can output multiple key-value pairs
        """
        data = {
            'goodbye': 'world',
            'stonk_value': 1200
        }
        result = YamlWriter().write(data)

        self.assertEqual(result, 'goodbye: world\nstonk_value: 1200\n')
