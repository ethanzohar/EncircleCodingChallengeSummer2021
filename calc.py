import sys
import re

# Regex to split a given string into an S-Expression format
sExprRegex = re.compile("(^add)|(^multiply)|(\s\d(\)|\s))|(\((?<=\().*\))|\s")

def calc(expr):
    # If the first character of the expression is a '('
    # then there is a function call that must be handled
    if (expr[0] == '('):
        # Strip out junk from regex parse and clean up values
        # Only left with ['FUNCTION', 'EXPR1', 'EXPR2']
        exprParams = [e.strip() for e in sExprRegex.split(expr[1:-1]) if (e and not e.isspace())]

        # Recursively parse the parameters of the function call as individual expressions
        if (exprParams[0] == 'multiply'):
            return calc(exprParams[1]) * calc(exprParams[2])
        elif (exprParams[0] == 'add'):
            return calc(exprParams[1]) + calc(exprParams[2])
        else:
            raise Exception("Unknown function")
    
    # If there is no function call, it means the expression is just a number
    return int(expr)

if __name__ == '__main__':
    if (not len(sys.argv) == 2):
        raise Exception("Only one argument is allowed to be passed")

    print(calc(sys.argv[1]))