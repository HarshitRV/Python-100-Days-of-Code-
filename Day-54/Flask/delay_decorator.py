import time

def delay_decorator(function):
    time.sleep(5)
    def wrapper_function():
        function()
    return wrapper_function

def say_hi():
    print("Hi")

# Noramally we would use the delay as follows
# delay_decorator(say_hi)()

# Instead we can use decorator function like this
@delay_decorator
def say_hello():
    print("Hello")

say_hello()
