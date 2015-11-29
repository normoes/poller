if __package__ is None:
    import sys
    from os import path
    #print path.dirname( path.dirname( path.abspath(__file__) ) )
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    #from greet import *
    #import greet.people
    #import greet.hello
    from greet import *
    from goodbye import bye
else:
    from greet import *
    from goodbye import bye

from unittest import TestCase

class TestHello(TestCase):
    assert (len(people.names) > 0), "There are no people in the list"
    
    assert (hello.Greeter() is not None, "could not create Greeter")
    
