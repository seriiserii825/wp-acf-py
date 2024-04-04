import json
from termcolor import colored
from acf_utils.fields.getFields import getFields
from acf_utils.group.getGroupByGroupId import getGroupByGroupId
from acf_utils.group.getGroupPathById import getGroupPathById
from acf_utils.group.getGroups import getGroups
from acf_utils.section.sectionHasGroup import sectionHasGroup
from acf_utils.tabs.getTabs import getTabs


def editGroup(file_path, group_id):
    tabs = getTabs(file_path)
    group_path = getGroupPathById(file_path, group_id)
    group = getGroupByGroupId(file_path, group_id)
    group_label = group['label']
    print(f"Group: {group_label}")
    # print(f"Group: {group}")
    # group_label =  exec(f"{group_path}['label']")
    # print(f"Group label: {group_label}")
    # for i in tabs:
    #     if i['label'] == group_id:
    #         group = i
    #         break
    # print(f"tabs: {tabs}")
    # # new_group_name = input("Enter group name: ")
    # new_group_slug = new_group_name.replace(" ", "_").lower()
    # tabs = getTabs(file_path)
    # key = 'label'
    # val = group['label']
    # tab = next((d for d in tabs if d.get(key) == val), None)
    # group_path = getGroupPathById(file_path, group_id)
    # print(f"Group path: {group_path}")
    # if new_group_name != "":
    #     with open(file_path, 'r') as file:
    #         data = json.load(file)
    #         exec(f"{group_path}['label'] = new_group_name")
    #         exec(f"{group_path}['name'] = new_group_slug")
    #         # exec(f"{group_path}[''][0]['label'] = new_group_name")
    #         # data[0]['fields'][group_index]['label'] = new_group_name
    #         # data[0]['fields'][group_index]['name'] = new_group_slug
    #         # data[0]['fields'][tab_index]['label'] = new_group_name
    #         # data[0]['fields'][tab_index]['label'] = new_group_name
    #         newData = json.dumps(data, indent=4)
    #
    #     with open(file_path, 'w') as file:
    #         file.write(newData)
