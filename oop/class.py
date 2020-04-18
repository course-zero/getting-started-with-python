# python supports OOP paradigm
# we use `class` keyword to create a class
# we can use `pass` keyword to define an empty class

class MyClassA:
    """
    Optional docstring explaining MyClassA 
    """
    pass

print( 'MyClassA.__doc__ => ', MyClassA.__doc__ )

# in python class, we have attributes and methods
# attribute stores some data while method references a function

# python class has two kind of attributes, class attributes and instance attribute
# class attributes are shared across all the instances
class MyClassB:
    # class attribute
    classAttributeA = 'classAttrA'

# class attributes will be accessible on class
print( 'MyClassB.classAttributeA => ', MyClassB.classAttributeA )


# python class has three kind of methods, class methods, static methods and instance methods
class MyClassC:

    # class attribute
    classAttributeA = 'classAttrA'

    # class method defintion, we use @classmethod decorator
    # giving first argument is necessary event if we don't use it
    @classmethod
    def classMethodA( cls, name ):
        return cls.classAttributeA + ':' + name
    
    # static method defintion, we use @staticmethod decorator
    @staticmethod
    def staticMethodA( name ):
        return name
        # works: return MyClassC.classAttributeA + ':' + name

# @classmethod decorator passes class as the first argument implicitely
# hence class methods have access to the class they belong to
# these are useful to create factory function
print( 'MyClassC.classMethodA("John") => ', MyClassC.classMethodA("John") )

# @staticmethod decorator defines a statc method and do not pass class reference
# but you can use class variable to access static property, not recommended as class name might change
# these are useful for pure utility purposes
print( 'MyClassC.staticMethodA("John") => ', MyClassC.staticMethodA("John") )

# To create an object, we need to call class like a function
# an object contains attributes and methods defined by the class
# but we can add custom attributes and methods after object is created on that specific instance
instanceC_A = MyClassC()
print( 'instanceC_A => ', instanceC_A )

# all class attributes are accessible on object
# however class attributes are not defined on object, if python can not find instance attribute with the same name, it will find on its constructor class
# TODO: this is possible due to namespace: https://dzone.com/articles/python-class-attributes-vs-instance-attributes
print( 'instanceC_A.classAttributeA => ', instanceC_A.classAttributeA )
print( 'instanceC_A.classAttributeA is MyClassC.classAttributeA => ', instanceC_A.classAttributeA is MyClassC.classAttributeA )

# create instance property if doesn't exist and assign new value
instanceC_A.classAttributeA = 'instanceA'
print( 'After: instanceC_A.classAttributeA => ', instanceC_A.classAttributeA )
print( 'After: instanceC_A.classAttributeA is MyClassC.classAttributeA => ', instanceC_A.classAttributeA is MyClassC.classAttributeA )

# static and class methods are also accessible on object and they can be overriden in the same way attributes can be overridden
print('instanceC_A.classMethodA("Mike") => ', instanceC_A.classMethodA("Mike"))
print('instanceC_A.staticMethodA("Mike") => ', instanceC_A.staticMethodA("Mike"))

instanceC_A.classMethodA = lambda name: "instance " + name
instanceC_A.staticMethodA = lambda name: "instance " + name

print('After: instanceC_A.classMethodA("Mike") => ', instanceC_A.classMethodA("Mike"))
print('After: instanceC_A.staticMethodA("Mike") => ', instanceC_A.staticMethodA("Mike"))

# instance method is method defintion without any decorator
# this method is accessible on an instance of the class
# __init__ method is always called when instance of a class is created, passing all arguments passed by the user
# when any instance method is called, python implicitely passes object as the first argument, conventionally named as self
class MyClassD:

    # also called as constructor method
    # self is passed by python, represents the object which will be created
    def __init__( self, firstName, lastName ):

        # these are instance attributes because they are only accessible on the instance
        # python does not support access modifiers on attributes or methods
        self.firstName = firstName # add firstName attribute to the object and assign value
        self.lastName = lastName # add lastName attribute to the object and assign value

    # instance method
    def getFullName( self ):
        return self.firstName + " " + self.lastName

instanceD_A = MyClassD( 'John', 'Doe' )
print( 'instanceD_A.firstName, instanceD_A.lastName => ', instanceD_A.firstName, instanceD_A.lastName )

# call an instance method
print( "instanceD_A.getFullName() => ", instanceD_A.getFullName() )

# we can access class of the object using __class__ attribute
print( "instanceD_A.__class__ is MyClassD => ", instanceD_A.__class__ is MyClassD )

# we can see attributes of an object using __dict__ attributes
print("instanceD_A.__dict__ => ", instanceD_A.__dict__)

# attributes on an object can be deleted any type
del instanceD_A.firstName
# print( "After delete: instanceD_A.firstName => ", instanceD_A.firstName ) #AttributeError: 'MyClassD' object has no attribute 'firstName'


# having a constructor is not necessary, until unless we have some initialzation data
class MyClassE:

    @staticmethod
    def getGreetings():
        return {'morning': 'Good Morning', 'hello': 'Hello World'}

    # we can call another instance method of the object
    # passing self to invoked method is not allowed, as python do that internally
    def getMessage(self):
        return self.getHelloWorld()
    
    # having self is necessary, even though we are not using it
    def getHelloWorld(self):

        # we can call a static method or class method on object
        # as it will look up on the class if instance method is not defined with that name
        greetings = self.getGreetings()
        return greetings['hello']

instanceE_A = MyClassE()
print( "instanceE_A.getMessage() => ", instanceE_A.getMessage() )

# python does not support access modifiers but using _ prefix is a conventional way to tell that the property or method is meant to be private
# we can use __ prefix to change the name of the attribute on final object. This makes little harder to access it on the object but not impossible. We still can reference them from inside using the same attribute name.
class MyClassG:
    def __init__(self):
        self._firstName = 'John'
        self.__lastName = 'Doe'
    
    def getFullName(self):
        return self._firstName + ' ' + self.__lastName
    
instanceG_A = MyClassG()
print('instanceG_A.__dict__', instanceG_A.__dict__)
print('instanceG_A.__getFullName()', instanceG_A.getFullName())



# getters and setters in python
# in the below example, we are safely setting the name
# but since we can not allow user to set name directory as name has to be broken down it parts, user needs to use `setName` and `getName` methods
class MyClassH:
    def __init__(self, name):
        self.setName(name)

    def setName(self, name):
        nameParts = name.split(" ")
        self.firstName = nameParts[0]
        self.lastName = nameParts[-1]
    
    def getName(self):
        return "{} {}".format(self.firstName, self.lastName)

instanceH_A = MyClassH("John M. Doe")
print('instanceH_A.getName()', instanceH_A.getName())

instanceH_A.setName("Jenna Doe")
print('After: instanceH_A.getName()', instanceH_A.getName())

# python provides `property` function which creates a property object that calls `getter` method when a attribute is accessed, `setter` method when attribute is assigned a value and `deleter` method when attribute is deleted
# this property object is class attribute of type <class 'property'>, but when accessed from an instance invokes the methods registered on it depending on type of operation
# unless we are trying to perform, get, set or delete operation, method arguments in property function are optional
class MyClassI:
    def __init__(self, name):
        self.setName(name)
    
    # getter method
    def getName(self):
        print("MyClassI.getName() called", end=" , ")
        return "{} {}".format(self.firstName, self.lastName)

    # setter method
    def setName(self, name):
        print("MyClassI.setName() called", end=" , ")
        nameParts = name.split(" ")
        self.firstName = nameParts[0]
        self.lastName = nameParts[-1]
    
    # deleter method
    def delName(self):
        print("MyClassI.getName() delName", end=" , ")
        del self.firstName
        del self.lastName

    # property attribute
    name = property(getName, setName, delName, "docstring")

instanceI_A = MyClassI("John M. Doe")
print('instanceI_A.name', instanceI_A.name)

instanceI_A.name = "Jenna Doe"
print('After: instanceI_A.name', instanceI_A.name)

del instanceI_A.name

# @property decorator makes it easy to write
# all method name should be same as attribute name
class MyClassJ:
    def __init__(self, name):
        self.name = name
    
    @property # property must be defined on getter
    def name(self):
        return "{} {}".format(self.firstName, self.lastName)

    @name.setter
    def name(self, name):
        nameParts = name.split(" ")
        self.firstName = nameParts[0]
        self.lastName = nameParts[-1]
    
    @name.deleter
    def name(self):
        del self.firstName
        del self.lastName

instanceJ_A = MyClassJ("John M. Doe")
print('instanceJ_A.name', instanceJ_A.name)

instanceJ_A.name = "Jenna F. Doe"
print('After: instanceJ_A.name', instanceJ_A.name)

del instanceJ_A.name
