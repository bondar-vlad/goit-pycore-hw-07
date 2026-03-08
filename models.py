from collections import UserDict
from processing import PhoneVerificationError, BirthdayVerificationError
from datetime import datetime, timedelta
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value: str):
        if len(value) == 10:
            super().__init__(value)
        else:
             raise PhoneVerificationError()

class Birthday(Field):
    def __init__(self, value: str):
        if re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", value.strip()):
             birthday = datetime.strptime(value, "%d.%m.%Y").date()
             super().__init__(birthday)
        else:
            raise BirthdayVerificationError()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    # реалізація класу

    def add_phone(self, phone):
          if not self.find_phone(phone):
               self.phones.append(Phone(phone))

    def remove_phone(self, phone):
          self.phones.remove(self.find_phone(phone))

    def edit_phone(self, old_phone, new_phone):
          self.find_phone(old_phone).value = new_phone

    def find_phone(self, phone):
          phones = list(filter(lambda ph: ph.value == phone, self.phones))
          if len(phones):
               return phones[0]
          
    def add_birthday(self, birthday):
          self.birthday = birthday

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self, iterable = {}):
          super().__init__(iterable)

    # реалізація класу
          
    def add_record(self, record: Record):
          self.data[record.name.value] = record

    def find(self, name: str) -> Record:
          return self.data.get(name)
    
    def delete(self, name: str):
          self.data.pop(name)

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today().date()

        for user in self.data:
            birthday = datetime.strptime(user.birthday, "%Y.%m.%d").date()
            birthday_this_year = datetime(year=today.year, month=birthday.month, day=birthday.day).date()
            if birthday_this_year < today:
                birthday_this_year = datetime(year = today.year + 1, month = birthday.month, day = birthday.day).date()
            days_difference = (birthday_this_year - datetime.today().date()).days
            if (days_difference >= 0 and days_difference < 7):
                birthday_weekday = birthday_this_year.isoweekday()
                congratulation_date = birthday_this_year if birthday_weekday < 6 else birthday_this_year + timedelta(days=8-birthday_weekday)
                upcoming_birthdays.append({"name":user.name, "congratulation_date":congratulation_date})
        return upcoming_birthdays