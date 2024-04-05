#!/usr/bin/python3
import json
import os

from termcolor import colored
from acf_utils.group.chooseGroup import chooseGroup
from acf_utils.group.editGroup import editGroup
from acf_utils.group.getGroups import getGroups
from acf_utils.group.groupMenu import groupMenu
from acf_utils.group.showAll import showAll
from acf_utils.group.addGroup import addGroup
from acf_utils.section.newSection import newSection
from acf_utils.wp.wpExport import wpExport
from acf_utils.wp.wpImport import wpImport
from acf_utils.group.showGroups import showGroups

if not os.path.exists("front-page.php"):
    exit(colored("Please run this script from the root of your theme folder!", "red"))

def getFullPath():
    os.chdir("acf")
    json_file = os.popen("fzf").read()
    # print(json_file)
    # file_path=f"acf/page-home.json"
    file_path = f"acf/{json_file}"
    file_path = file_path.replace("\n", "")
    # print(file_path)
    os.chdir("..")
    return file_path


file_path = getFullPath()
# showAll(file_path)
# group_id = chooseGroup(file_path)
# groups = getGroups(file_path)
# print(f"group id: {group_id}")
# showAll(file_path, group_id)

def mainMenu(file_path):
    print('----------------------------- Menu -----------------------------')
    print(colored("1) Show All:", "yellow"))
    print(colored("2) Add Group:", "green"))
    print(colored("3) Edit Group:", "green"))
    print(colored("4) Delete Group:", "green"))
    print(colored("5) Choose Group:", "green"))
    # print(colored("4) Delete Group:", "green"))
    # print(colored("4.1) Copy Group:", "green"))
    # print(colored("5) Add Field:", "blue"))
    # print(colored("5.1) Add Repeater Field:", "blue"))
    # print(colored("6) Edit Field:", "blue"))
    # print(colored("7) Delete Field:", "blue"))
    # print(colored("8) Import:", "yellow"))
    # print(colored("9) Export:", "yellow"))
    print(colored("10) Exit:", "red"))
    action = input("Enter your choice: ")
    print('----------------------------- Menu -----------------------------')
    if action == "1":
        showAll(file_path)  # show groups with fields
        mainMenu(file_path)
    elif action == "2":
        addGroup(file_path)  # add group
        # groupHandler(file_path)  # edit group
        mainMenu(file_path)
    elif action == "3":
        editGroup(file_path)  # add group
        mainMenu(file_path)
    elif action == "4":
        group_id = chooseGroup(file_path)
        editGroup(file_path, group_id)  # add group
        mainMenu(file_path)
    elif action == "5":
        group_id = chooseGroup(file_path)
        editGroup(file_path, group_id)  # add group
        mainMenu(file_path)

        group_id = chooseGroup(file_path)
        showAll(file_path, group_id)
        groupMenu(file_path, group_id)
    # elif action == "4":
    #     groupHandler(file_path, True)  # delete Group
    #     mainMenu(file_path)
    # elif action == "4.1":
    #     copyGroup(file_path)
    #     exit()
    # elif action == "5":
    #     addField(file_path)  # add field
    #     mainMenu(file_path)
    # elif action == "5.1":
    #     addField(file_path, is_repeater=True)  # add field
    #     mainMenu(file_path)
    # elif action == "6": # edit field
    #     editField(file_path)
    #     mainMenu(file_path)
    # elif action == "7":#delete field
    #     editField(file_path, True) 
    #     mainMenu(file_path)
    # elif action == "8":
    #     wpImport()
    #     mainMenu(file_path)
    # elif action == "9":
    #     wpExport()
    #     mainMenu(file_path)
    # elif action == "10":
    #     exit()
    else:
        exit()
mainMenu(file_path)



# print(json.dumps(groups[group_index], indent=4))
# editField(file_path)
# addField(file_path) # add field

# print(colored("Welcome to ACF CLI", "green"))
# print(colored("1) Create new section", "yellow"))
# print(colored("2) Select section", "yellow"))
# print(colored("3) Import", "blue"))
# print(colored("4) Export", "blue"))
# print(colored("5) Exit", "red"))
# choice = input("Make your choice:")
# if choice == "1":
#     newSection()
# elif choice == "3":
#     wpImport()
# elif choice == "4":
#     wpExport()
# elif choice == "5":
#     exit()
# else:
#     file_path = getFullPath()
#
#     def mainMenu(file_path):
#         print('----------------------------- Menu -----------------------------')
#         print(colored("1) Show groups with fields:", "yellow"))
#         print(colored("2) Show All:", "green"))
#         # print(colored("3) Edit Group:", "green"))
#         # print(colored("4) Delete Group:", "green"))
#         # print(colored("4.1) Copy Group:", "green"))
#         # print(colored("5) Add Field:", "blue"))
#         # print(colored("5.1) Add Repeater Field:", "blue"))
#         # print(colored("6) Edit Field:", "blue"))
#         # print(colored("7) Delete Field:", "blue"))
#         # print(colored("8) Import:", "yellow"))
#         # print(colored("9) Export:", "yellow"))
#         print(colored("10) Exit:", "red"))
#         action = input("Enter your choice: ")
#         print('----------------------------- Menu -----------------------------')
#         if action == "1":
#             showGroups(file_path, True)  # show groups with fields
#             mainMenu(file_path)
#         elif action == "2":
#             showAll(file_path)  # add group
#             mainMenu(file_path)
#         # elif action == "3":
#         #     groupHandler(file_path)  # edit group
#         #     mainMenu(file_path)
#         # elif action == "4":
#         #     groupHandler(file_path, True)  # delete Group
#         #     mainMenu(file_path)
#         # elif action == "4.1":
#         #     copyGroup(file_path)
#         #     exit()
#         # elif action == "5":
#         #     addField(file_path)  # add field
#         #     mainMenu(file_path)
#         # elif action == "5.1":
#         #     addField(file_path, is_repeater=True)  # add field
#         #     mainMenu(file_path)
#         # elif action == "6": # edit field
#         #     editField(file_path)
#         #     mainMenu(file_path)
#         # elif action == "7":#delete field
#         #     editField(file_path, True) 
#         #     mainMenu(file_path)
#         # elif action == "8":
#         #     wpImport()
#         #     mainMenu(file_path)
#         # elif action == "9":
#         #     wpExport()
#         #     mainMenu(file_path)
#         # elif action == "10":
#         #     exit()
#         else:
#             exit()
#
#     mainMenu(file_path)
