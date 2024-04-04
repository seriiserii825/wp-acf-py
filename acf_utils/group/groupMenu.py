from termcolor import colored
from acf_utils.group.addGroup import addGroup
from acf_utils.group.editGroup import editGroup

from acf_utils.group.showAll import showAll


def groupMenu(file_path, group_id):
    print('----------------------------- Group Menu -----------------------------')
    print(colored("1) Show All:", "yellow"))
    print(colored("2) Add Group:", "yellow"))
    print(colored("3) Edit Group:", "yellow"))
    print(colored("5) Exit", "red"))
    action = input("Enter your choice: ")
    if action == "1":
        showAll(file_path, group_id)
        groupMenu(file_path, group_id)
    if action == "2":
        addGroup(file_path, group_id)
        groupMenu(file_path, group_id)
    if action == "3":
        editGroup(file_path, group_id)
        groupMenu(file_path, group_id)
    elif action == "5":
        exit()
    else:
        groupMenu(file_path, group_id)
