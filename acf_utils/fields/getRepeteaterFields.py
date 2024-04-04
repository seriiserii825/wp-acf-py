import json

def getRepeaterFields(file_path):
    repeater_fields = []
    f = open(file_path,)
    data = json.load(f)
    for i in data:
        for j in i['fields']:
            if j['type'] == "group":
                sub_fields = j['sub_fields']
                for k in sub_fields:
                    if k['type'] == "repeater":
                        repeater_field = {'name': k['name'], 'label': k['label'], 'index': sub_fields.index(k)}
                        repeater_fields.append(repeater_field)
    return repeater_fields

