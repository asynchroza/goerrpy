def goerr(func):
    def wrapper_func(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
            return value, None
        
        except Exception as e:
            return None, e
    return wrapper_func
