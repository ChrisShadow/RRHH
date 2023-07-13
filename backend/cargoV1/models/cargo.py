#region Doc

#Inheritance: Adoption of properties from the parent class into the child class.
#Polymorphism: Creation of many forms from one form.
#Abstraction: Displaying the necessary data and hiding unnecessary data.
#Encapsulation: Securing the info of the class.

"classes on Python: https://docs.python.org/3/tutorial/classes.html"
"https://youtu.be/LwFnF9XoEfM"
"https://realpython.com/lessons/managing-class-attributes/"
"https://www.geeksforgeeks.org/python-classes-and-objects/"
"https://realpython.com/python-namespaces-scope/#:~:text=the%20next%20level.-,Namespaces%20in%20Python,values%20are%20the%20objects%20themselves."
"https://www.askpython.com/python/oops/class-instance-attributes#:~:text=You%20can%20access%20the%20attributes,would%20use%20the%20expression%20myClass."
"Modules and Packages: https://youtu.be/f26nAmfJggw"
"Public and private classes: https://youtu.be/xY__sjI5yVU"
"Public and Private members: https://youtu.be/js9EITv4HqM"

"There are not private and protected, just public and non-public(uses __ for att and meth) class members"
"Passign members from one class to another one: https://youtu.be/iDc_VrawjqY"
"Basic Decorations: @classmethod, @staticmethod"
"Classes inside another classes: Inner Classes"
"Functions inside another functions: nested methods"

#In Python we have class type attributes and instance type attributes. 
# That is, those not defined in the constructor(__init__) and those that are defined in it.
#The same ocurrs with methods: class level ones and instance level ones. Key word are self for the 
#instance level and cls for class level
#Another kind of method is the static one. Only has access to the parameters that we pass into it individually and then
#can be used with either the class itself or the instance object
#endregion

class Cargo():
    
    def __init__(self) -> None:
        pass