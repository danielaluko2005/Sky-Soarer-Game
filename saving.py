
file_name="values.txt"

def save_value(input_value,file_name):
    with open(file_name,"w") as f:
        f.write(str(input_value))

def load_value(file_name):
   # Open a file for reading
    with open(file_name, 'r') as file:
    # Read all lines into a list
        lines = file.readlines()
    return int(lines[0])


