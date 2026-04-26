def say_hello():
    print("Hello, World!")

def say_hello_times(times):
    for i in range(times):
        say_hello()

say_hello_times(5)