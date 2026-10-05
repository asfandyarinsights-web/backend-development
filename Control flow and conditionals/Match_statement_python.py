'''
The match statement was introduced in Python 3.10
to handle multiple conditions more cleanly than if-else chains.
'''


'''
Conditional Guards (if):You can append an if condition
directly inside a case pattern to implement more precise rules.

case n if n < 0:
    return "Negative Number"
'''

https_status=501

match https_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 500 | 501:
        print("Server Error")
    case _:
        print("UnKnown")