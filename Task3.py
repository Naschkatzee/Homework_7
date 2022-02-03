import json
import yaml


data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {'age': 3,
        'name': 'Alice'
        }
    ],
    'married': True,
    'city': None   
    }

with open ('dump', 'w') as f:
    json.dump (data, f)
    print (data)

with open ('dump', 'r') as f:
    data = json.load (f)
    print (data)



data = '{"Name" : "Romy", "Gender" : "Female"}'

data = json.loads (data)
print(data)

data = json.dumps (data)
print (data)



