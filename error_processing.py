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
        except Exception:
            return "Unknown error occured."
    return inner

class PhoneVerificationError(Exception):
    def __init__(self, message="Phone should contain 10 digits"):
        self.message = message
        super().__init__(self.message)

class BirthdayVerificationError(Exception):
    def __init__(self, message="Invalid date format. Use DD.MM.YYYY"):
        self.message = message
        super().__init__(self.message)

class NameVerificationError(Exception):
    def __init__(self, message="Name was not found"):
        self.message = message
        super().__init__(self.message)