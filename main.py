import sections_parser

def main():
    while True:
        file_name = input("Please enter a valid filename: ")
        try:
            with open(file_name, 'r') as file:
                break
        except FileNotFoundError:
            print("Error: File not found. Please try again.")
    
    content = sections_parser.load_file_content(file_name)
    # print(content)
    print(sections_parser.get_section_list(content))
    # print(sections_parser.get_section_content(content, "Test2"))

if __name__ == "__main__":
    main()