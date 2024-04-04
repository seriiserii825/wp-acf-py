import json

def getGroups(file_path):
    groups = []
    f = open(file_path,)
    data = json.load(f)
    for i in data:
        for j in i['fields']:
            if j['type'] == "group":
                # print(j)
                fields = []
                for k in j['sub_fields']:
                    field = {'name': k['name'], 'label': k['label']}
                    fields.append(field)
                group = {'name': j['name'], 'label': j['label'], 'index': i['fields'].index(j), 'fields': fields}
                groups.append(group)
    # print(groups)
    return groups