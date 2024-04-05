import json

from acf_utils.fields.getRepeteaterFields import getRepeaterFields

from acf_utils.fields.newField import newField

def addField(file_path, group_index, is_repeater=False):
    if is_repeater:
        repeater_fields = getRepeaterFields(file_path)
        for i in repeater_fields:
            print(f"{i['index']}) {i['label']}")
        repeater_field_index = input("Enter your choice: ")
        field_name = input("Enter field name: ")
        field_slug = field_name.replace(" ", "_").lower()
        if field_name != "":
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
                data[0]['fields'][group_index]['sub_fields'][int(repeater_field_index)]['sub_fields'].append(field)
                newData = json.dumps(data, indent=4)
            with open(file_path, 'w') as file:
                file.write(newData)
    else:
        field_name = input("Enter field name: ")
        field_slug = field_name.replace(" ", "_").lower()
        if field_name != "":
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
                data[0]['fields'][group_index]['sub_fields'].append(field)
                newData = json.dumps(data, indent=4)
            with open(file_path, 'w') as file:
                file.write(newData)
