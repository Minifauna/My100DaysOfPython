def format_name(f_name, l_name):
    if l_name == "" or f_name == "":
        return "Invalid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("First name?"),input("Last name?")))

