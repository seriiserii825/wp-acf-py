import json
from termcolor import colored
from acf_utils.group.getGroupPathById import getGroupPathById
from acf_utils.group.newGroup import newGroup
from acf_utils.section.sectionHasGroup import sectionHasGroup
from acf_utils.tabs.newTab import newTab


def addGroup(file_path, group_id = None):
    new_group_name = input("Enter group name: ")
    if new_group_name != "":
        group_slug = new_group_name.lower().replace(" ", "_")
        if sectionHasGroup(file_path, group_slug):
            print(colored("Group already exists!!!", "red"))
            return
        with open(file_path, 'r') as file:
            # read
            data = json.load(file)
            if group_id:
                group_path = getGroupPathById(file_path, group_id)
                real_data = eval(group_path)
                print(f"real_data: {real_data}")
                new_tab = newTab(new_group_name)
                group_path.append(new_tab)
                new_group = newGroup(new_group_name)
                group_path.append(new_group)
                newData = json.dumps(data, indent=4)
                print(json.dumps(group_path, indent=4))
            else:
                new_tab = newTab(new_group_name)
                data[0]['fields'].append(new_tab)
                new_group = newGroup(new_group_name)
                data[0]['fields'].append(new_group)
                newData = json.dumps(data, indent=4)
                print(json.dumps(data[0]['fields'], indent=4))
            print(newData)

        # with open(file_path, 'w') as file:
        #     # write
        #     file.write(newData)
        #
