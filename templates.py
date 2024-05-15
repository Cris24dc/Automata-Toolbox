# deterministic finite automaton template generator
def dfa_template_generator():
    file_name = input("Enter the name of the config file: ")
    file_path = f"./cfg/{file_name}.cfg"
    content = """# The Section names are case-sensitive
# The content of each section should be between the section name and the word 'end'
# The Sigma, States, Start and Final sections should have one element per line
# The Start section should have only one element
# The Delta section should have 3 elements separated by a space
# The Delta section should have the format: state_from char state_to
# The alphabet should contain only single characters
# The alphabet should not contain the "[" and "]" characters

[Sigma]
# Content of Sigma section
end

[States]
# Content of States section
end

[Start]
# Content of Start section
end

[Final]
# Content of Final section
end

[Delta]
# Content of Delta section
end"""

    with open(file_path, 'w') as file:
        file.write(content)

# context free grammar template generator
def cfg_template_generator():
    file_name = input("Enter the name of the config file: ")
    file_path = f"./cfg/{file_name}.cfg"
    content = """# The Section names are case-sensitive
# The content of each section should be between the section name and the word 'end'
# The Variables, Terminals and Rules sections should have one element per line
# The Start variable should be the first element in the Rules section
# The Variables and Terminals should not contain the "[" and "]" characters
# The Rules section should have the format: variable -> rule
# The Rules should contain variables and terminals separated by spaces
# The Variables and Terminals should not contain 

[Variables]
# Content of Variables section
end

[Terminals]
# Content of Terminals section
end

[Rules]
# Content of Rules section
end"""

    with open(file_path, 'w') as file:
        file.write(content)