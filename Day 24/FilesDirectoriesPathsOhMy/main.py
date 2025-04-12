with open('../../../../Documents/100PythonSuppDoc/my_file.txt') as file: # with will close the file once done with indented instructions
    contents = file.read()
    print(contents)

