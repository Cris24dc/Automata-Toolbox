def load_file_content(file_name):
    try:
        with open(f"./cfg/{file_name}.cfg", "r") as file:
            lines = file.readlines()
            if not lines:
                print("File is empty")
                return None
            lines = [line[:line.index("#")].strip() + "\n" if "#" in line else line for line in lines]
            while "\n" in lines:
                lines.remove("\n")
            lines = "".join(lines)
            return lines
    except FileNotFoundError:
        print(f"File '{file_name}' not found")
        return None


def get_section_list(content):
    tokens = content.split("\n")
    array = []
    for token in tokens:
        if token.strip().startswith("[") and token.strip().endswith("]"):
            array.append(token.strip().strip("[]"))
        elif "[" in token or "]" in token:
            print(f"Invalid section syntax '{token}'")
            return []
    return array


def get_section_content(content, name):
    array = []
    if name in content:
        lines = [elem.strip() for elem in content.split("\n")]
        index = lines.index(f"[{name}]") + 1
        while lines[index].strip().lower() != "end":
            if "[" in lines[index] or "]" in lines[index]:
                print(f"End of section '{name}' not found")
                return []
            array.append(lines[index])
            index += 1
    return array
