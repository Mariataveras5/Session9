def greet():
    """
    Simple function printing hello
    :return: None
    """
    print("Hello")
    return 0

def greet_improved(name):
    """
    More complex greet that takes a name as param
    :param name: the name of the person to greet 
    :return: None
    """
    print("Hello", name)

greet_improved("John")
greet_improved("Jane")

def custom_op(x = 0,y = 0):
    """
    Custom op: 10x+ y
    :param x: the first number
    :param y: the second number
    :return: number, 10x+y
    """
    result = 10*x + y
    return result

print(custom_op(5,8))
x = custom_op(5,9) #arguments by position
print(f"the result of custom_op is: {x}")
x = custom_op(y=9, x=5) #agruments by name
print(f"the result of custom_op is: {x}")
print(custom_op(5)) #using default values for y
print(custom_op()) #default values for both
print(custom_op(y=9)) #default value for x

def bond_intro(name):
    print("the name is:", name)

def bond_name (first = "James", last = "Bond"):
    return f"{last}, {first} {last}"

print(bond_name("Bogdan", "Ratiu"))
bond_intro(bond_name("Bogdan", "Ratiu"))
bond_intro(bond_name())
