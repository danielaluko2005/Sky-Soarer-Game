
file_name="values.txt"

def save_value(input_value,file_name):
    with open(file_name,"w") as f:
        f.write(str(input_value))

def load_value(file_name):
    with open(file_name,"r") as f:
        read=f.read()
    return read

myObject=load_value(file_name)
for obj in myObject:
    print(obj)

user_input=input("item:- ")

save_value(str(user_input),file_name)

