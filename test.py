import unittest
from transmit.yaml import YamlFormatter
from transmit.yaml import YamlError


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
