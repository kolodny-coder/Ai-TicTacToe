
def get_decorator(errors=(Exception,)):
    def decorator(func):

        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors:
                print('\n\nPlease choose a valid value\n\n ')
                return new_func(*args, **kwargs)

        return new_func

    return decorator


input_validator = get_decorator(ValueError)