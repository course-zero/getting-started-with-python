print( "basicmath/__init__.py: __name__ => ", __name__ )
print( "basicmath/__init__.py: __package__ => ", __package__ )

from . import utils as utility # exports utility name
from .utils import * # exports everything from utils

def info():
    return 'Yes, init can also contain functions.'