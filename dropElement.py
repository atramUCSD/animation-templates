import json

with open('dest_file.json', 'w') as dest_file:
    with open('result.json', 'r') as result:
        for line in result:
            element = json.loads(line.strip())
            if 'examples' in element:
                del element['examples']
            dest_file.write(json.dumps(element))