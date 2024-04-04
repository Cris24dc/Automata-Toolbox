import os
import subprocess
import template
import dfa

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("Main Menu:\n")
    print("1. Generate a Template")
    print("2. Emulate a DFA")
    print("3. Edit Config File")
    print("4. List Config Files")
    print("5. Delete Config File")
    print("q. Exit\n")

def generate_template():
    clear_screen()
    print("Generate a Template")
    template.template_generator()
    input("Press Enter to return to the main menu.")

def emulate_dfa():
    clear_screen()
    print("Emulate a DFA")
    dfa.dfa_emulator()
    input("Press Enter to return to the main menu.")

def configure_file():
    clear_screen()
    file_name = input("Enter the name of the file to open: ")
    if os.path.exists(f"./cfg/{file_name}.cfg"):
        subprocess.run(["nano", f"./cfg/{file_name}.cfg"])
    else:
        print(f"The file '{file_name}' does not exist.")
    input("Press Enter to return to the main menu.")

def list_config_files():
    clear_screen()
    print("List Config Files\n")
    cfg_files = os.listdir("./cfg/")
    for file in cfg_files:
        print(file)
    input("\nPress Enter to return to the main menu.")

def delete_config_file():
    clear_screen()
    file_name = input("Enter the name of the file to delete: ")
    file_path = f"./cfg/{file_name}.cfg"
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"The file '{file_name}' has been deleted.")
    else:
        print(f"The file '{file_name}' does not exist.")
    input("Press Enter to return to the main menu.")