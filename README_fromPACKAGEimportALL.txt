assume package is called greet.

if you ant to do something like:
        $from greet import *

add all the contained modules into into __init__.py of greet:
        __all__ = ["hello", "people"]
        
        
example:
        test cases
