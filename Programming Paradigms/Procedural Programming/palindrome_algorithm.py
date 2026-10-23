 #Algorithm for a Palindrome

word='racecar'


# lastindex=len(word)-1
# print(word[lastindex])

# if  word[0]==word[lastindex]:
#     print('palindrome')
# else:
#     print('not palindrome')

def isPalindrome (str):
    startIndex = 0
    endIndex = len(str) - 1
    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True


print(isPalindrome ('racecars'))

