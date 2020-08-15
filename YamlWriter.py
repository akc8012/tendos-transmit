import yaml


class YamlWriter:
    def __init__(self):
        data = dict(
            hello='world',
            itreally=dict(
                do='be',
                like='that',
            )
        )

        with open('output.yml', 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)
