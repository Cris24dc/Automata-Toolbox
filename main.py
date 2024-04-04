import interface

def main():
    while True:
        interface.main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            interface.generate_template()
        elif choice == "2":
            interface.emulate_dfa()
        elif choice == "3":
            interface.configure_file()
        elif choice == '4':
            interface.list_config_files()
        elif choice == '5':
            interface.delete_config_file()
        elif choice.lower() == "q":
            interface.clear_screen()
            break
        else:
            interface.clear_screen()
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
