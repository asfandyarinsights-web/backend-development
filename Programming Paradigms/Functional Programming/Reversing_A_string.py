# 1 - Slice Function Reversing a String
# str[start : stop : step]
# indices Slice Syntax

address="HomeTown Is Pakistan"

reverseString=address[::-1]

print(reverseString)


# Recursion

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]


str = "reversal"
reverse=string_reverse(str)
print(reverse)