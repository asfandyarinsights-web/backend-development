def divideBY(x , y):
    return x/y

try:
    ans=(divideBY(40,0))
except Exception as e:
    print("Something went wrong", e)
    print(e.__class__) #class of error