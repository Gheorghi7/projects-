def multiply(fn):
    def wrapper(*args, **kwargs):
        return f"you called {fn.__name__}{args}\nIt resulted {args[0] * args[1] * args[2]}"

    return wrapper


@multiply
def a_fun(a, b, c):
    return a * b * c


print(a_fun(1, 2, 3))
