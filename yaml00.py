# -*- coding: utf-8 -*-
import yaml
import io

data = {'participant': 1,
        'warmup': True,
        'pretest': ['t', 'f', 'dk', 'dk', 't', 't', 't', 'f', 'dk', 'dk', 't'],
        'system example': [
        	{'library': {'t1': ['t', 'f', 'f'], 
        				 't3': ['t', 'f', 'f'],
        				 't4': ['t', 'f', 'f'],
        				 't2': ['t', 'f', 'f']},
        	 'spell' : {'t2' : ['t', 't', 'dk']}}
        	 ],
        }


# Write YAML file
with io.open('data.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True, sort_keys=False)

# Read YAML file
with open("data.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)

print(data == data_loaded)
print(data['pretest'])
