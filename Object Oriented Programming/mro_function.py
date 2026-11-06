class A:   #parent class
    pass

class B(A):  #child of A
    pass

class C(B): #child of B
    pass


print(C.mro())
print(help(C))


'''
[<class '__main__.C'> goes to  <class '__main__.B'> and it goes to
<class '__main__.A'> at the end it goes to <class 'object'>]

'''
