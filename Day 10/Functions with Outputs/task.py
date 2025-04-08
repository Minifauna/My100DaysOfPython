# pause 1 - create a function called format_name() that takes two inputs: f_name and 'l_name'
# def format_name(f_name, l_name):
#     return (f_name + " " + l_name).title()
# print(format_name("adam", "chomey"))

def format_name(f_name, l_name):
    f_f_name = f_name.title()
    l_l_name = l_name.title()
    return f"{f_f_name} {l_l_name}"
formatted_string = format_name("adam", "chomey")
print(formatted_string)

output = len("Moose") # iterates through, counts objects in container, "returns" int
print(output)

def function1(text):
    return text + text

def function2(text):
    return text.title()

output = function2(function1("word")) #function2 input is the output of function1
print(output)
