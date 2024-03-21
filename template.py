def template_generator():
    file_name = input("Enter the name of the config file: ")
    content = """# The Section names are case-sensitive
# The content of each section should be between the section name and the word 'end'
# The Sigma, States, Start and Final sections should have one element per line
# The Start section should have only one element
# The Delta section should have 3 elements separated by a space
# The Delta section should have the format: state_from char state_to

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

    with open(file_name, 'w') as file:
        file.write(content)
