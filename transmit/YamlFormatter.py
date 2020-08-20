import yaml


class YamlFormatter:
    def format(self, data):
        return yaml.dump(data, None)
