"""
    VARIABLES:
    variableName = value
"""
integer = 123
decimal = 12.3
string = "string"
boolean = True

# assignment
variableName = 12
# assignment with expression
variableName = otherVariableName operator someValue

"""
    OPERATORS:
        Addition: +
        Subtraction: -
        Multiplication: *
        Division: /
        Modulus (Remainder): %
        Power(Exponentiation): **

        Interger Division: //

    Operator Precedence:
        Parenthesis: (), {}, []
        Power: a**b or a^b
        Multiplication: Division(/), Multiplication (*), Remainder (%)
        Addition: Addition(+), Subtraction (-)
        Left to Right: a - c + d

    Comparision Operators:
        Less than: <
        Less than or equal: <=
        Greater than: >
        Greater than or equal: >=
        Equal: ==
        Not equal: !=
        
"""
type(variableName) # gives type of variable (int, str, float, bool, object, etc)
"""
    CONVERTING TYPE (suitable conversion):
    str(variableName): converts to string
    int(variableName): converts to integer
    float(variableName): converts to float/decimal
"""


"""
    CONDITIONAL STATEMENTS
    if condition:
        # code goes here
        pass
    else:
        # code goes here
        pass

    More conditions
    if condition1:
        # code goes here
        pass
    elif condition2:
        # code goes here
        pass
    ...
    ...
    ...
    elif conditionN:
        # code goes here
        pass
    else:
        # code goes here
        pass


    TRY - EXCEPT

    try:
        # put dangerous / critical code which will probably cause exception
        pass
    except:
        # if exception encountered..
        pass


    FUNCTIONS:
        Built-in functions:
            (int(), float(), str(), print(), etc.)

    def functionName():
        # function code goes here
        pass

    def functionName(argument[s]):
        # function code goes here
        pass

    def functionName(arguments[s]):
        # function code goes here

        return someValue


    LOOPS:
        # indefinite loop
        while condition[s]:
            # loop code goes here
            if condition:
                continue # skip following line go to next iteration
            if condition:
                break: # stop loop
        
        # definite loop
        for item in itemsList:
            # process item





    STRINGS:
    

        
"""













