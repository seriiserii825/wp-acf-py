import json

from acf_utils.group.getGroups import getGroups

def chooseGroup(file_path):
    groups = getGroups(file_path)
    print(json.dumps(groups, indent=4))
    print("Choose a group:")
    for i in groups:
        index = groups.index(i)
        print(f"{index}) {i['label']}")
    choice = input("Make your choice:")
    group_id = groups[int(choice)]['key']
    return group_id
