
file_path="values.txt"

def edit_file_line(file_path, line_number, new_text):
    """
    args:
    file_path (str): file name.
    line_number (int): The line in the file according to the current difficulty.
    new_text (str): new score.
    """
    # Read the lines of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Perform the edit in memory
    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_text + '\n'

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print("Invalid line number.")




edit_file_line(file_path,2,str(3))


def load_value(file_path,line_number):
    """
    args:
    file_path (str): file name.
    line_number (int): The line in the file according to the current difficulty.
    """
   # Open a file for reading
    with open(file_path, 'r') as file:
    # Read all lines into a list
        lines = file.readlines()[line_number-1].strip()
    return lines

