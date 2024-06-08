def load_file_content(file_name):
    # Attempt to open and read the specified file
    try:
        with open(f"./cfg/{file_name}.cfg", "r") as file:
            lines = file.readlines()  # Read all lines from the file
            if not lines:
                print("File is empty")  # Check if the file is empty
                return None
            # Remove comments and strip whitespace from lines
            lines = [line[:line.index("#")].strip() + "\n" if "#" in line else line for line in lines]
            while "\n" in lines:
                lines.remove("\n")  # Remove empty lines
            lines = "".join(lines)  # Join lines into a single string
            return lines
    except FileNotFoundError:
        print(f"File '{file_name}' not found")  # Handle file not found error
        return None

def get_section_list(content):
    tokens = content.split("\n")  # Split content into lines
    array = []
    for token in tokens:
        if token.strip().startswith("[") and token.strip().endswith("]"):
            array.append(token.strip().strip("[]"))  # Add section names to the array
        elif "[" in token or "]" in token:
            print(f"Invalid section syntax '{token}'")  # Handle invalid section syntax
            return []
    return array

def get_section_content(content, name):
    array = []
    if name in content:
        lines = [elem.strip() for elem in content.split("\n")]  # Split content into lines
        index = lines.index(f"[{name}]") + 1  # Find the starting index of the section
        while lines[index].strip().lower() != "end":
            if "[" in lines[index] or "]" in lines[index]:
                print(f"End of section '{name}' not found")  # Handle end of section not found
                return []
            array.append(lines[index])  # Add lines to the section array
            index += 1
    return array
