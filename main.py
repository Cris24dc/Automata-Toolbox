import template
import dfa

def main():
    choice = input("Enter 1 to generate a template or 2 to emulate a DFA: ")
    if choice == "1":
        template.template_generator()
    elif choice == "2":
        dfa.dfa_emulator()

if __name__ == "__main__":
    main()
