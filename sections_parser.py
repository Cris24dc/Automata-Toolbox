def load_file_content(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("File is empty")
            lines = [line[:line.index("#")].strip() + "\n" if "#" in line else line for line in lines]
            while("\n" in lines):
                lines.remove("\n")
            lines = "".join(lines)
            return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_name}' not found")


def get_section_list(content):
    tokens = content.split("\n")
    array = []
    for token in tokens:
        if token.strip().startswith("[") and token.strip().endswith("]"):
            array.append(token.strip().strip("[]"))
        elif "[" in token or "]" in token:
            raise ValueError(f"Invalid section syntax '{token}'")
    return array


def get_section_content(content, name):
    array = []
    if name in content:
        lines = [elem.strip() for elem in content.split("\n")]
        index = lines.index(f"[{name}]") + 1
        while lines[index].strip().lower() != "end":
            if ("[" in lines[index]) or ("]" in lines[index]):
                raise ValueError(f"end of section '{name}' not found")
            array.append(lines[index])
            index += 1
    return array
