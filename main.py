from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.__value)

class Name(Field):
    def __init__(self, value):
        self._Field__value = value.title()

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime (value, '%d.%m.%Y').date()
        except:
            raise ValueError ('Wrong format for birthday')

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    @Field.value.setter
    def value (self, value):
        if (len (value) != 10) or (not value.isdigit()):
            raise ValueError ('Phone number should have 10 digit.')
        else:
            super().value = value

class Record:
    def __init__(self, name, birthday=0):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday

    def add_birthday (self, b_day):
        try:
            self.birthday = Birthday (b_day)
        except:
            return print (f"Birthday '{b_day}' not added.\n")
        print (f"Birthday for '{self.name.value}' added.\n")

    def add_phone (self, phone):
        try:
            phone_checked = Phone (phone)
        except:
            return print (f"Phone number '{phone}' not added.\n")
        self.phones.append (phone_checked)
        print (f"Phone number for '{self.name.value}' added.\n")

    def remove_phone (self, phone):
        try:
            phone_checked = Phone (phone)
        except:
            return print (f"Phone number '{phone}' not removed.\n")
        print (self.phones)
        for phone_for_check in self.phones:
            if phone_checked.value == phone_for_check.value:
                self.phones.remove (phone_for_check)
            return print ("Phone number for deleted\n")

    def edit_phone (self, phone1, phone2):
        for exist_phone in self.phones:
            if phone1 == exist_phone.value:
                self.phones.remove (exist_phone)
                phone_checked = Phone (phone2)
                if phone_checked:
                    self.phones.append (phone_checked)
                    return f"Phone number for '{self.name.value}' edited\n"
        raise ValueError

    def find_phone (self, phone):
        for find_phone in self.phones:
            if phone == find_phone.value:
                return find_phone
        print (f"'{self.name.value}' don't have phone number, what you want to find\n")

    def days_to_birthday (self):
        if self.birthday == 0:
            raise ValueError
        if datetime.today().date() < self.birthday.value:
            next_birthday = self.birthday.value
            days_to_next = next_birthday - datetime.today().date()
        elif datetime.today() < datetime (datetime.today().year, \
                        self.birthday.value.month, self.birthday.value.day):
            next_birthday = datetime (datetime.today().year, \
                        self.birthday.value.month, self.birthday.value.day)
            days_to_next = next_birthday.date() - datetime.today().date()
        else:
            next_birthday = datetime (datetime.today().year + 1, \
                        self.birthday.value.month, self.birthday.value.day)
            days_to_next = next_birthday.date() - datetime.today().date()
        return days_to_next.days

    def __str__(self):
        try:
            return f"Contact name: {self.name.value}; \
phones: {', '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
        except AttributeError:
            return f"Contact name: {self.name.value}; phones: no phones added, birthday: {self.birthday}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record (self, record: Record):
        self.data.update ({record.name.value: record})
        print (f"Contact '{record.name.value}' added\n")

    def find (self, name):
        self.name = Name (name)
        return self.data.get (self.name.value)

    def delete (self, record: str):
        if self.data.get (record):
            record_deleted = self.data.pop (record)
            print (f"Contact '{record_deleted}' deleted\n")
        else:
            print (f"Contact book don't have contact '{record}'\n")

if __name__ == "__main__":
 # Створення нової адресної книги
    book = AddressBook()

# Створення запису для John
    print ('-----Створення запису для John-----')
    john_record = Record("john")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555f")
    john_record.add_birthday("10.02.2021")

# Додавання запису John до адресної книги
    print ('-----Додавання запису John до адресної книги-----')
    book.add_record(john_record)

# Створення та додавання нового запису для Jane
#    print ('-----Створення та додавання нового запису для Jane-----')
#    jane_record = Record("jane")
#    jane_record.add_phone("9876543210")
#    book.add_record(jane_record)

# Виведення всіх записів у книзі
    print ('-----Виведення всіх записів у книзі-----')
    for name, record in book.data.items():
        print(record)
        try:
            print(f"Days to next {name}'s birthday: {record.days_to_birthday()}")
        except ValueError:
            pass
        except AttributeError:
            print(f"I can't calculate days to next b-day for {record.birthday}")
    print ('')

# Знаходження та редагування телефону для John
#    print ('-----Знаходження та редагування телефону для John-----')
#    john = book.find("john")
#    john.edit_phone("1234567890", "1112223333")

#    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
#    print ('-----Пошук конкретного телефону у записі John-----')
#    found_phone = john.find_phone("5555555555")
#    print(f"{john.name}: {found_phone}\n")  # Виведення: 5555555555

    # Видалення запису Jane
#    print ('-----Видалення запису Jane-----')
#    jane11 = book.find("jane")
#    print (jane11, '- found jane11')
#    book.delete("Jane")
#    jane22 = book.find("Jane")
#    print (jane22, '- found jane22')
