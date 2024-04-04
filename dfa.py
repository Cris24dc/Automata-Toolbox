import sections_parser
import os


def dfa_check():

    file_name = input("Please enter a valid filename: ")

    content = sections_parser.load_file_content(file_name)

    if content == None:
        return None
    
    sections = sections_parser.get_section_list(content)

    required_sections = ["Sigma", "States", "Start", "Final", "Delta"]
    if sorted(sections) != sorted(required_sections):
        print("Invalid sections")
        return

    section_contents = {}
    for section in sections:
        section_contents[section] = sections_parser.get_section_content(content, section)
        if not section_contents[section]:
            print(f"Section '{section}' is empty")
            return
    
    sigma = section_contents["Sigma"]
    states = section_contents["States"]
    start = section_contents["Start"]
    final = section_contents["Final"]
    delta = section_contents["Delta"]

    for section_name, section_content in section_contents.items():
        if section_name in ["Sigma", "States", "Start", "Final"]:
            for line in section_content:
                if len(line.split()) != 1:
                    print(f"Line '{line}' in section '{section_name}' has more than one character")
                    return
        elif section_name == "Delta":
            for line in section_content:
                if len(line.split()) > 3:
                    print(f"Line '{line}' in section 'Delta' has more than three characters")
                    return
                if len(line.split()) < 3:
                    print(f"Line '{line}' in section 'Delta' has less than three characters")
                    return
                state_from, char, state_to = line.split()
                if state_from not in states:
                    print(f"State '{state_from}' not found in 'States' section")
                    return
                if char not in sigma:
                    print(f"Character '{char}' not found in 'Sigma' section")
                    return
                if state_to not in states:
                    print(f"State '{state_to}' not found in 'States' section")
                    return

    print(f"DFA from \"{file_name}\" is valid")

    return sigma, states, start, final, delta


def dfa_emulator():

    result = dfa_check()
    if result is None:
        return

    sigma, states, start, final, delta = result

    string = input("Please enter a string: ")

    current_state = start[0]
    for char in string:
        if char not in sigma:
            print("Invalid string")
            return
        
        for transition in delta:
            if transition.split()[0] == current_state and transition.split()[1] == char:
                current_state = transition.split()[2]
                break

    if current_state in final:
        print("String accepted")
    else:
        print("String rejected")
