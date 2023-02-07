def outer():
    print("Hello from Outer Function")
    def inner():
        print("Hello from inner Function")
    return inner
d=outer()
d()