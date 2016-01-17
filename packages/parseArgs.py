import argparse

parser = argparse.ArgumentParser()

## positional argument: a
#nargs='?' one argument which can also be empty
parser.add_argument('path', nargs='?', help='Description for "a" element', default="check_string_for_empty")

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-f','--foo', nargs=2, help='Description for foo argument', required=True)
parser.add_argument('-b','--bar', nargs=3, help='Description for bar argument', required=True)
parser.add_argument('-c','--cho', nargs='?', help='Description for cho argument', const='const value', default="check_string_for_empty", required=False)

args = vars(parser.parse_args())

print args

