import yaml


class YamlWriter:
    def write(self, data):
        return yaml.dump(data, None)
