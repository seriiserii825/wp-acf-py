import json
from termcolor import colored
from acf_utils.fields.getFields import getFields
from acf_utils.group.getGroupByGroupId import getGroupByGroupId
from acf_utils.group.getGroupPathById import getGroupPathById
from acf_utils.group.getGroups import getGroups
from acf_utils.section.sectionHasGroup import sectionHasGroup
from acf_utils.tabs.getTabs import getTabs


def editGroup(file_path):
    fields = getFields(file_path)
    tabs = getTabs(file_path)
    groups = getGroups(file_path)
    print(colored("Select group to edit:", "green"))
    for i in groups:
        print(f"{i['index']}) {i['label']}")
    group_index = input("Enter your choice: ")
    if group_index.isdigit():
        group_index = int(group_index)
        group = fields[0][int(group_index)]
        # print(tabs)
        key = 'label'
        val = group['label']
        tab = next((d for d in tabs if d.get(key) == val), None)
        tab_index = tab['index']
        old_group_name = group['label']
        new_group_name = input("Enter group name(Leave blank for old title): ")
        if new_group_name == "":
            new_group_name = old_group_name
        new_group_slug = new_group_name.replace(" ", "_").lower()
        print(colored("Group layout(Leave blank for block): ", "green"))
        print(colored("1) block", "blue"))
        print(colored("2) table", "yellow"))
        print(colored("3) row", "red"))
        new_group_layout = input(colored("Enter group layout:", "green"))
        if new_group_layout == "1":
            new_group_layout = "block"
        elif new_group_layout == "2":
            new_group_layout = "table"
        elif new_group_layout == "3":
            new_group_layout = "row"
        else:
            new_group_layout = "block"
        print(f"Group layout: {new_group_layout}")
        with open(file_path, 'r') as file:
            # read
            data = json.load(file)
            data[0]['fields'][group_index]['label'] = new_group_name
            data[0]['fields'][group_index]['name'] = new_group_slug
            data[0]['fields'][group_index]['layout'] = new_group_layout
            data[0]['fields'][tab_index]['label'] = new_group_name
            newData = json.dumps(data, indent=4)

        with open(file_path, 'w') as file:
            # write
            file.write(newData)
