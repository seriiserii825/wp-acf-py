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
from acf_utils.group.deleteGroup import deleteGroup
from acf_utils.group.copyGroup import copyGroup
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
    print(colored("2) Choose Group:", "green"))
    print(colored("3) Add Group:", "green"))
    print(colored("4) Edit Group:", "green"))
    print(colored("5) Delete Group:", "green"))
    print(colored("6) Copy Group:", "green"))
    print(colored("7) Import:", "yellow"))
    print(colored("8) Export:", "yellow"))
    print(colored("9) Exit:", "red"))
    action = input("Enter your choice: ")
    print('----------------------------- Menu -----------------------------')
    if action == "1":
        showAll(file_path)
        mainMenu(file_path)
    elif action == "2":
        group_index = chooseGroup(file_path)
        showAll(file_path, group_index)
        back = groupMenu(file_path, group_index)
        if back == False:
            mainMenu(file_path)
    elif action == "3":
        addGroup(file_path)
        mainMenu(file_path)
    elif action == "4":
        editGroup(file_path)
        mainMenu(file_path)
    elif action == "5":
        deleteGroup(file_path)
        mainMenu(file_path)
    elif action == "6":
        copyGroup(file_path)
        exit()
    elif action == "7":
        wpImport()
        mainMenu(file_path)
    elif action == "8":
        wpExport()
        mainMenu(file_path)
    elif action == "9":
        exit()
    else:
        exit()
mainMenu(file_path)
