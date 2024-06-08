import os
import subprocess
import templates
import dfa
import nfa
import cfg
import pda

def clear_screen():
    # Clear the console screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()  # Clear the screen
    # Print the main menu options
    print("Main Menu:\n")
    print("1. Generate a Template")
    print("2. Edit Config File")
    print("3. List Config Files")
    print("4. Delete Config File")
    print("5. Emulate a DFA")
    print("6. Emulate a NFA")
    print("7. Emulate a CFG")
    print("8. Emulate a PDA")
    print("q. Exit\n")

def generate_template():
    clear_screen()  # Clear the screen
    print("Generate a Template:\n")
    print("1. DFA Template")
    print("2. NFA Template")
    print("3. CFG Template")
    print("4. PDA Template")
    choice = input("Enter your choice: ")  # Get user's choice
    # Generate the corresponding template based on user's choice
    if choice == "1":
        templates.dfa_template_generator()
        input("Press Enter to return to the main menu.")
    elif choice == "2":
        templates.nfa_template_generator()
        input("Press Enter to return to the main menu.")
    elif choice == "3":
        templates.cfg_template_generator()
        input("Press Enter to return to the main menu.")
    elif choice == "4":
        templates.pda_template_generator()
        input("Press Enter to return to the main menu.")
    else:
        print("Invalid option. Please try again.")

def emulate_dfa():
    clear_screen()  # Clear the screen
    print("Emulate a DFA")
    dfa.dfa_emulator()  # Call DFA emulator
    input("Press Enter to return to the main menu.")

def emulate_nfa():
    clear_screen()  # Clear the screen
    print("Emulate a NFA")
    nfa.nfa_emulator()  # Call NFA emulator
    input("Press Enter to return to the main menu.")

def emulate_cfg():
    clear_screen()  # Clear the screen
    print("Emulate a CFG")
    cfg.cfg_generator()  # Call CFG generator
    input("Press Enter to return to the main menu.")

def emulate_pda():
    clear_screen()  # Clear the screen
    print("Emulate a PDA")
    pda.pda_emulator()  # Call PDA emulator
    input("Press Enter to return to the main menu.")

def configure_file():
    clear_screen()  # Clear the screen
    file_name = input("Enter the name of the file to open: ")  # Get file name from user
    if os.path.exists(f"./cfg/{file_name}.cfg"):  # Check if file exists
        subprocess.run(["nano", f"./cfg/{file_name}.cfg"])  # Open file in nano editor
    else:
        print(f"The file '{file_name}' does not exist.")
    input("Press Enter to return to the main menu.")

def list_config_files():
    clear_screen()  # Clear the screen
    print("List Config Files\n")
    cfg_files = os.listdir("./cfg/")  # List all files in the 'cfg' directory
    for file in cfg_files:
        print(file)  # Print each file name
    input("\nPress Enter to return to the main menu.")

def delete_config_file():
    clear_screen()  # Clear the screen
    file_name = input("Enter the name of the file to delete: ")  # Get file name from user
    file_path = f"./cfg/{file_name}.cfg"
    if os.path.exists(file_path):  # Check if file exists
        os.remove(file_path)  # Delete the file
        print(f"The file '{file_name}' has been deleted.")
    else:
        print(f"The file '{file_name}' does not exist.")
    input("Press Enter to return to the main menu.")
