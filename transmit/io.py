import yaml


class YamlFormatter:
    def format(self, data):
        if data is None:
            raise YamlError('data cannot be None')

        return yaml.dump(data, None)


class YamlError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


class FileWriter():
    def write(self, data):
        with open('output.yml', 'w') as text_file:
            print(data, file=text_file)


class InputTranslator:
    def translate(self, data):
        return None
