from termcolor import colored
from acf_utils.fields.addField import addField
from acf_utils.fields.chooseRepeaterField import chooseRepeaterField
from acf_utils.fields.deleteField import deleteField
from acf_utils.fields.editField import editField
from acf_utils.group.repeaterFieldsMenu import repeaterFieldsMenu

from acf_utils.group.showAll import showAll
from acf_utils.wp.wpExport import wpExport
from acf_utils.wp.wpImport import wpImport


def groupMenu(file_path, group_index):
    print('----------------------------- Group Menu -----------------------------')
    print(colored("1) Show All:", "yellow"))
    print(colored("2) Add Field:", "blue"))
    print(colored("3) Choose Repeater Field:", "green"))
    print(colored("4) Edit Field:", "blue"))
    print(colored("5) Delete Field:", "blue"))
    print(colored("6) Import:", "red"))
    print(colored("7) Export:", "red"))
    print(colored("8) Exit", "red"))
    print(colored("9) Back to Main Menu", "green"))
    showAll(file_path, group_index)
    action = input("Enter your choice: ")
    if action == "1":
        showAll(file_path, group_index)
        groupMenu(file_path, group_index)
    if action == "2":
        addField(file_path, group_index)
        groupMenu(file_path, group_index)
    if action == "3":
        field_index = chooseRepeaterField(file_path, group_index)
        if field_index == False:
            groupMenu(file_path, group_index)
        else:
            repeaterFieldsMenu(file_path, group_index, field_index)
    if action == "4":
        editField(file_path, group_index)
        groupMenu(file_path, group_index)
    if action == "5":
        deleteField(file_path, group_index)
        groupMenu(file_path, group_index)
    elif action == "6":
        wpImport()
        exit()
    elif action == "7":
        wpExport()
        exit()
    elif action == "8":
        exit()
    elif action == "9":
        return False
    else:
        groupMenu(file_path, group_index)
