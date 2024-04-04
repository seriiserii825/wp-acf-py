import json

from termcolor import colored
from acf_utils.fields.addField import addField

from acf_utils.fields.getFields import getFields
from acf_utils.fields.newField import newField
from acf_utils.group.getGroups import getGroups
from acf_utils.group.showGroups import showGroups


def editField(file_path, delete=False):
    fields = getFields(file_path)
    groups = getGroups(file_path)
    groups.append({'index': colored(0, 'red'),  'name': '','label': colored('Exit', 'red')})
    print(colored("Select group:", "green"))
    for i in groups:
        print(f"{i['index']}) {i['label']}")
    group_index = input("Enter your choice: ")
    if group_index != "0":
        showGroups(file_path, True)  # show groups with fields
        group_index = int(group_index)
        group = fields[0][int(group_index)]
        sub_fields = group['sub_fields']

        for i in sub_fields:
            print(f"{sub_fields.index(i)}) {i['label']}")

        field_index = input("Enter your choice: ")

        if field_index == "":
            return

        if delete == False:
            field_name = input("Enter field name: ")

            if field_name == "":
                field_name = sub_fields[int(field_index)]['label']
                field_slug = field_name.replace(" ", "_").lower()
            else:
                field_slug = field_name.replace(" ", "_").lower()


            field_types = ['text', 'textarea', 'number', 'email', 'url', 'wysiwyg', 'image', 'gallery', 'file', 'repeater', 'message']
            for i in field_types:
                print(f"{field_types.index(i)}) {i}")
            field_type_index = input("Enter your choice: ")
            if field_type_index == "":
                field_type_index = "0"
            field_type = field_types[int(field_type_index)]
            field_width = input("Enter field width: ")
            if field_width == "":
                field_width = "100"
            field = newField(field_name, field_slug, field_type, field_width)
            with open(file_path, 'r') as file:
                # read
                data = json.load(file)
                data[0]['fields'][group_index]['sub_fields'][int(field_index)] = field
                newData = json.dumps(data, indent=4)
            with open(file_path, 'w') as file:
                file.write(newData)
        else:
            with open(file_path, 'r') as file:
                data = json.load(file)
                del data[0]['fields'][group_index]['sub_fields'][int(field_index)]
                newData = json.dumps(data, indent=4)

            with open(file_path, 'w') as file:
                # write
                file.write(newData)
    elif group_index == "0":
        return


    print(colored("Add new field, choose group", "blue"))
    addField(file_path)
