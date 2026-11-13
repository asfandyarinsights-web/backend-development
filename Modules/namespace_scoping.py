def d():
    animal="elephant"
    def e():
        nonlocal animal
        animal="giraffe"
        print("Inside nested function E () : ",animal)

    print("Before Calling Function E()",animal)
    e()
    print("After Calling Function E()",animal)


animal="camel"
d()
print("Global Variable Aninmal: ",animal)
