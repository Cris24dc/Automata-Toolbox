import interface

def main():
    # Loop to continuously show the main menu and process user choices
    while True:
        interface.main_menu()  # Display the main menu
        choice = input("Enter your choice: ")  # Get user's choice
        if choice == "1":
            interface.generate_template()  # Generate a template based on user's choice
        elif choice == "2":
            interface.configure_file()  # Configure a file
        elif choice == '3':
            interface.list_config_files()  # List all config files
        elif choice == '4':
            interface.delete_config_file()  # Delete a config file
        elif choice == '5':
            interface.emulate_dfa()  # Emulate a DFA
        elif choice == '6':
            interface.emulate_nfa()  # Emulate a NFA
        elif choice == '7':
            interface.emulate_cfg()  # Emulate a CFG
        elif choice == '8':
            interface.emulate_pda()  # Emulate a PDA
        elif choice.lower() == "q":
            interface.clear_screen()  # Clear the screen
            break  # Exit the loop
        else:
            interface.clear_screen()  # Clear the screen for any invalid input

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
