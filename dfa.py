import sections_parser

def dfa_check():
    file_name = input("Please enter a valid filename: ")  # Get file name from user

    content = sections_parser.load_file_content(file_name)  # Load file content

    if content == None:
        return None
    
    sections = sections_parser.get_section_list(content)  # Get list of sections

    required_sections = ["Sigma", "States", "Start", "Final", "Delta"]
    if sorted(sections) != sorted(required_sections):
        print("Invalid sections")  # Check for required sections
        return

    section_contents = {}
    for section in sections:
        section_contents[section] = sections_parser.get_section_content(content, section)
        if not section_contents[section]:
            print(f"Section '{section}' is empty")  # Check for empty sections
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

    print(f"DFA from \"{file_name}\" is valid")  # Confirm DFA validity

    return sigma, states, start, final, delta

def dfa_emulator():
    result = dfa_check()  # Perform DFA check
    if result is None:
        return

    sigma, states, start, final, delta = result

    string = input("Please enter a string: ")  # Get input string from user

    current_state = start[0]
    for char in string:
        if char not in sigma:
            print("The string contains characters not present in the alphabet")
            return
        
        for transition in delta:
            if transition.split()[0] == current_state and transition.split()[1] == char:
                current_state = transition.split()[2]
                break

    if current_state in final:
        print("String accepted")  # String is accepted if in final state
    else:
        print("String rejected")  # String is rejected if not in final state
