import yaml


class YamlFormatter:
    def format(self, data):
        if data is None:
            raise YamlError('data cannot be None')

        return yaml.dump(data, None)


class YamlError(RuntimeError):
    def __init__(self, arg):
        self.args = arg
