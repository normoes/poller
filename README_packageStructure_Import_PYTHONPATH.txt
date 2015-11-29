project structure
    /helloer
        /helloer    
                /greet
                        __init__.py
                        hello.py
                        people.py
                /goodbye
                        __init__.py
                        bye.py
                greetings.py
                /test
                        __init__.py
                        test.py

assuming that bye.py imports people.py from package greet.
        when calling bye.py directly the value in the PYTHONPATH variable is important.
1)
call a module directly using the console:
        assumption: cd /helloer/helloer
        $python -m goodbye.bye (without .py file extension)
        in bye.py:
                $from greet import people (works)
		__package__ is set
2)
call a module from within the package subdirectory:
        assumption: cd /helloer/helloer/goodbye
        python bye.py
        --> add path to sys.path
        --> otherwise package greet would be unknown
        in bye.py:
                $import sys
                $from os import path
                $sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
		__package__ is not set (= None)

3)
__file__ is set when called via the console
--> module cannot be executed from IDE (like IDLE) with these settings
		__package__ is None and __file__ is not set
				
				

        
