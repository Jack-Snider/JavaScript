



def hello(a : int):

    if not isinstance(a, int):
        raise TypeError("the parameter should be Integer")

    return a

hello('s')