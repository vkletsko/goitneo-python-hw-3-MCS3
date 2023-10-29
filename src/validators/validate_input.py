def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please.")
        except IndexError:
            print("Sorry. Contact book is empty.")
        except TypeError:
            print("Invalid operation.")
        except AttributeError:
            print("Invalid operation.")

    return inner
