FILEPATH = "To_Dos.txt"

def get_to_dos():
    with open(FILEPATH, 'r') as file:
        return file.readlines()

def clean_user_input(prompt):
    """takes user input and makes it standard format for boolean checks"""
    clean_input = input(prompt).capitalize().strip()
    return clean_input

def show_to_do_list(new_or_current, to_do_list_param):
    """reads file for current to dos.  Takes string input to show the user if we're
    viewing the current list or the new list after modification"""
    if new_or_current == 'new':
        print("Changes saved")
    print(f"Here is your {new_or_current} list:")
    for index, item in enumerate(to_do_list_param):
        # can also be done as to_do_list = [item.strip('\n') for item in to_do_list]
        item = item.strip("\n")
        print(f"{index+1}: {item}")

def save_to_do_list(new_list):
    """saves list to file after modifications like save, edit or complete"""
    with (open(FILEPATH, 'w') as file):
        file.writelines(new_list)
    show_to_do_list('new', new_list)