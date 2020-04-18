
# https://docs.python.org/3/library/inspect.html#inspect.getmro
from inspect import getmro


# in other programming language, we are ChildClass extends ParentClass
# in python, we write ChildClass(ParentClass): which means the same thing
# python supports inheriting multiple classes, ChildClass(ParentOneClass, ParentTwoClass):

# in python every class, custom or user-defined, inherits `object` class
# but in python 3, we do not have to use `MyClass(object):`, python interprets `MyClass:` as the same

# we can view the inheritance tree by inspecting method resolution order or MRO (discussed later)
# A boolean value is an instance of `bool` class which inherits `int` class which inherits `object` class
# we can use `__class__` property of an object to see its constructor class
boolVal = True

# in case of multiple inheritance, `__bases__` return all inherited classes while `__base__` returns first inherit class
print( 'boolVal.__class__.__bases__ => ', boolVal.__class__.__bases__ )
# we can use `getmro` function from `insepct` package to see MRO
print( 'getmro(boolVal.__class__) => ', getmro(boolVal.__class__) )

# When a child class inherits parent class, child class has access to all properties and methods of parent class.

# When we try to access an attribute on an instance of child class, it first searches for instance attribute, then class attribute on it, then class attribute on parent class, then class attributes on the classes they inherit

# single inheritance
class AGrandParentOne:
    classAttrA = 'AGrandParentOneClassAttrA'
    classAttrB = 'AGrandParentOneClassAttrB'
    classAttrC = 'AGrandParentOneClassAttrC'

class AParentOne(AGrandParentOne):
    classAttrA = 'AParentOneClassAttrA'
    classAttrB = 'AParentOneClassAttrB'

class AChildOne(AParentOne):
    classAttrA = 'AChildOneClassAttrA'

AInstChildOne = AChildOne()

# multiple inheritance
class BParentOne:
    classAttrA = 'BParentOneClassAttrA'
    classAttrB = 'BParentOneClassAttrB'
    classAttrC = 'BParentOneClassAttrC'

class BParentTwo:
    classAttrA = 'BParentTwoClassAttrA'
    classAttrB = 'BParentTwoClassAttrB'

class BChildOne(BParentTwo, BParentOne):
    classAttrA = 'BChildOneClassAttrA'

BInstChildOne = BChildOne()


# according to method resolution order (funny: it also applies for attributes and not only methods), attributes and methods are first resolved on the base class (child class), if missing, they are looked up on inherited classes in order of their appearance.
# MRO: https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/
# ARO: https://codefellows.github.io/sea-python-401d4/lectures/inheritance_v_composition.html

# method resolution order of single and multiple inheritance
# Question: Why only on `object` in MRO? Anser: C3 linearization
print("AChildOne.mro() => ", AChildOne.mro())
print( "AInstChildOne classAttrA => {}, classAttrB => {}, classAttrC => {}".format( AInstChildOne.classAttrA, AInstChildOne.classAttrB, AInstChildOne.classAttrC) )

print("BChildOne.mro() => ", BChildOne.mro())
print( "BInstChildOne classAttrA => {}, classAttrB => {}, classAttrC => {}".format( BInstChildOne.classAttrA, BInstChildOne.classAttrB, BInstChildOne.classAttrC) )

# there will be cases when inherited classes will have a common inherit class. To create a MRO tree, python uses C3 linearization (https://en.wikipedia.org/wiki/C3_linearization).
# Rules:
# 1. Method on sibling inherit classes will be resolved from left to right
# 2. If sibling classes inherit a common class eventually, then the common class will come last in MRO
# 3. object will always be a common class

'''
E
| \
|  D
|  |
B  C
\  /
 A

# MR(a) : A -> B -> C -> D -> E -> E
'''

# Using MRO, python also looks up for methods
class CParentOne:
    def __init__(self):
        self.owner = 'CParentOne'
    def world(self):
        return 'CParentOne.world'
class CChildOne(CParentOne):
    def hello(self):
        return 'CChildOne.hello'

CInstChildOne = CChildOne()
print( "CInstChildOne.owner: {}, CInstChildOne.hello(): {}, CInstChildOne.world(): {}".format( CInstChildOne.owner, CInstChildOne.hello(), CInstChildOne.world() ) )

# We can also call parent method from the child method
class DParentOne:
    def sayHello(self):
        return 'Hello ' + self.name

class DChildOne(DParentOne):
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return DParentOne.sayHello(self)

DInstChildOne = DChildOne("John")
print("DInstChildOne.sayHello() => ", DInstChildOne.sayHello())

# to avoid using name of the inherit class, we can use `super` function which returns a proxy (temporary) object of the parent class binded with `self`. Hence passing self is not necessary
# super: https://realpython.com/python-super/
# When a attribute and method is accessed on `super()`, it follows the MRO tree
class EGrandParentOne:
    def sayHello(self):
        return 'Grand Hello ' + self.name

class EParentOne(EGrandParentOne):
    pass

class EChildOne(EParentOne):
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return super().sayHello()

EInstChildOne = EChildOne("John")
print("EInstChildOne.sayHello() => ", EInstChildOne.sayHello())

# When an inherited class modifies `self`, we must call __init__ function of it
class FParentOne:
    def __init__(self):
        self.fullName = self.firstName + ' ' + self.lastName
    def sayHello(self):
        return 'Hello ' + self.fullName

class FChildOne(FParentOne):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

        super().__init__()

FInstChildOne = FChildOne("John", "Doe")
print("FInstChildOne.sayHello() => ", FInstChildOne.sayHello())

# In case of multiple inheritance, super() only resolves the class according to MRO
class GParentOne:
    def __init__(self):
        self.parentOne = 'ParentOne'

class GParentTwo:
    def __init__(self):
        self.parentTwo = 'ParentTwo'

class GChildOne(GParentOne, GParentTwo):
    def __init__(self):
        self.childOne = 'ChildOne'
        super().__init__()

GChildInstOne = GChildOne()
print('GChildInstOne.__dict__ => ', GChildInstOne.__dict__)

# to call all the parent constructors, we need to manually call __init__ methods on all inherit classes
# GParentOne.__init__(self), GParentTwo.__init__(self)

# Or, we can observe MRO and call super to propogate method call
class HParentOne:
    def __init__(self):
        self.parentOne = 'ParentOne'
        super().__init__() # calls HParentTwo.__init__()

class HParentTwo:
    def __init__(self):
        self.parentTwo = 'ParentTwo'
        super().__init__() # calls object.__init__()

class HChildOne(HParentOne, HParentTwo):
    def __init__(self):
        self.childOne = 'ChildOne'
        super().__init__()

HChildInstOne = HChildOne()
print('HChildOne.mro() => ', HChildOne.mro())
print('HChildInstOne.__dict__ => ', HChildInstOne.__dict__)

# In case of multiple inheritance, when constructor needs arguments, passing them carefully can be done using keyword arguments
# https://realpython.com/python-super/


# In case of third party plugins, we do not have control over the class to call super
# Hence, we need to create an adapater
class IParentOne:
    def __init__(self):
        self.parentOne = 'ParentOne'

class IParentTwo:
    def __init__(self):
        self.parentTwo = 'ParentTwo'

class IParentThree:
    def __init__(self):
        self.parentThree = 'ParentThree'

# to call super in MRO chain
class AdapaterIParentOne(IParentOne):
    def __init__(self):
        super().__init__() # calls IParentOne.__init__()
        IParentTwo.__init__(self) # manuall call IParentTwo.__init__()
        IParentThree.__init__(self) # manuall call IParentThree.__init__()

class IChildOne(AdapaterIParentOne, IParentTwo, IParentThree):
    def __init__(self):
        self.childOne = 'ChildOne'
        super().__init__() # AdapaterIParentOne.__init__()

IChildInstOne = IChildOne()
print('IChildOne.mro() => ', IChildOne.mro())
print('IChildInstOne.__dict__ => ', IChildInstOne.__dict__)

# Common functions and methods used in OOP
# 1. Is class A subclass of B
# 2. Is object a instance of class A
# 3. __repr__ and __str__ for string representation of an object (https://www.geeksforgeeks.org/str-vs-repr-in-python/)
# 4. Operator overloading (https://www.programiz.com/python-programming/operator-overloading)