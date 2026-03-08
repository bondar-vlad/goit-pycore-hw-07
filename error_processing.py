from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid command format."
        except IndexError:
            return "Contact not found."
    return inner

class PhoneVerificationError(Exception):
    def __init__(self, message="Phone should contain 10 digits"):
        self.message = message
        super().__init__(self.message)

class BirthdayVerificationError(Exception):
    def __init__(self, message="Invalid date format. Use DD.MM.YYYY"):
        self.message = message
        super().__init__(self.message)