# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# Functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What's it like in {location}")
greet_with("Moose", "Alaska")
greet_with(name="Moose", location="Alaska")
# positional versus keyword arguments for the parameters
