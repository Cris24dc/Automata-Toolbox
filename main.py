import interface

def main():
    while True:
        interface.main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            interface.generate_template()
        elif choice == "2":
            interface.configure_file()
        elif choice == '3':
            interface.list_config_files()
        elif choice == '4':
            interface.delete_config_file()
        elif choice == '5':
            interface.emulate_dfa()
        elif choice == '6':
            interface.emulate_nfa()
        elif choice == '7':
            interface.emulate_cfg()
        elif choice == '8':
            interface.emulate_pda()
        elif choice.lower() == "q":
            interface.clear_screen()
            break
        else:
            interface.clear_screen()

if __name__ == "__main__":
    main()
