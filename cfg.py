import sections_parser
import random

def cfg_check():

    file_name = input("Enter the name of the config file: ")

    content = sections_parser.load_file_content(file_name)

    if content == None:
        return None
    
    sections = sections_parser.get_section_list(content)

    required_sections = ["Variables", "Terminals", "Rules"]
    if sorted(sections) != sorted(required_sections):
        print("Invalid sections")
        return

    section_contents = {}
    for section in sections:
        section_contents[section] = sections_parser.get_section_content(content, section)
        if not section_contents[section]:
            print(f"Section '{section}' is empty")
            return
    
    variables = section_contents["Variables"]
    terminals = section_contents["Terminals"]
    rules = section_contents["Rules"]

    for section_name, section_content in section_contents.items():
        if section_name in ["Variables", "Terminals"]:
            for line in section_content:
                if len(line.split()) != 1:
                    print(f"Line '{line}' in section '{section_name}' has more than one element")
                    return
        elif section_name == "Rules":
            for line in section_content:
                if len(line.split()) < 3:
                    print(f"Line '{line}' in section 'Rules' has less than three elements")
                    return
                if "->" not in line:
                    print(f"Line '{line}' in section 'Rules' does not have '->'")
                    return
                variable, rule = line.split("->")
                variable = variable.strip()
                if variable not in variables:
                    print(f"Variable '{variable}' not found in 'Variables' section")
                    return
                for element in rule.split():
                    if element not in variables and element not in terminals:
                        print(f"Element '{element}' not found in 'Variables' or 'Terminals' section")
                        return

    print(f"CFG from \"{file_name}\" is valid")

    return variables, terminals, rules

# context free grammar emulator
# it s generating and printing random strings until there are just terminals in the string, based on the rules, choosing the rules randomly
def cfg_emulator():
    
    result = cfg_check()
    if result is None:
        return
    
    variables, terminals, rules = result

    string = random.choice(variables)
    
    while True:
        new_string = ""
        for element in string.split():
            if element in terminals:
                new_string += element + " "
            else:
                found = False
                for rule in rules:
                    if rule.split("->")[0].strip() == element:
                        new_string += rule.split("->")[1].strip() + " "
                        found = True
                        break
                if not found:
                    new_string += element + " "
        if new_string == string:
            break
        string = new_string.strip()
        print(string)


    

    

        


