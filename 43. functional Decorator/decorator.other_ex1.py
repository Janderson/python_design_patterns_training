# source: https://www.artima.com/weblogs/viewpost.jsp?thread=240845#decorator-functions-with-decorator-arguments


def decoratorFunctionWithArguments(*args_dec, **kwargs):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments: --->", args_dec)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap

@decoratorFunctionWithArguments('_parameter1_')
def sayHello(a1, a2, a3, a4):
    print('---> sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("#1 Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")

print("#2 after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("#3 after second sayHello() call")