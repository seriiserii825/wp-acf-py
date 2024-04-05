from termcolor import colored
from acf_utils.fields.addField import addField
from acf_utils.fields.deleteField import deleteField
from acf_utils.fields.editField import editField

from acf_utils.group.showAll import showAll
from acf_utils.wp.wpExport import wpExport
from acf_utils.wp.wpImport import wpImport


def repeaterFieldsMenu(file_path, group_index, field_index):
    print('----------------------------- Group Menu -----------------------------')
    print(colored("1) Show All:", "yellow"))
    print(colored("2) Add Field:", "blue"))
    print(colored("3) Edit Field:", "blue"))
    print(colored("4) Delete Field:", "blue"))
    print(colored("5) Import:", "red"))
    print(colored("6) Export:", "red"))
    print(colored("7) Exit", "red"))
    showAll(file_path, group_index)
    action = input("Enter your choice: ")
    if action == "1":
        showAll(file_path, group_index)
        repeaterFieldsMenu(file_path, group_index, field_index)
    if action == "2":
        addField(file_path, group_index, field_index)
        repeaterFieldsMenu(file_path, group_index, field_index)
    if action == "4":
        editField(file_path, group_index)
        repeaterFieldsMenu(file_path, group_index, field_index)
    if action == "5":
        deleteField(file_path, group_index)
        repeaterFieldsMenu(file_path, group_index, field_index)
    elif action == "6":
        wpImport()
        exit()
    elif action == "7":
        wpExport()
        exit()
    elif action == "8":
        exit()
    else:
        repeaterFieldsMenu(file_path, group_index, field_index)
