import yaml

y = yaml.load(open("foobar.yaml"))
yaml.dump(y, open("foobar.yaml", "w"))
