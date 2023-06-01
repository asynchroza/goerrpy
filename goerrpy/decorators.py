import typing

def goerr(unpack: bool = False):
    def goerr_decorator(func: typing.Callable[..., typing.Any]):
        def wrapper_func(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                if unpack:
                    return *value, None

                return value, None
            
            except Exception as e:
                return None, e

        return wrapper_func
    return goerr_decorator
