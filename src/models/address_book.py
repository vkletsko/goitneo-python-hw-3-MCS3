from collections import UserDict, defaultdict
from datetime import datetime
import calendar


class AddressBook(UserDict):
    def add_record(self, contact):
        self.data[contact.name.value] = contact

    def find(self, key):
        res = self.data.get(key)
        return res

    def delete(self, key):
        del self.data[key]

    def set_birthday(self, name: str, date: str) -> None:
        contact = self.find(name)
        contact.add_birthday(date)

    def show_birthday(self, name: str) -> str:
        contact = self.find(name)

        if contact.birthday:
            return contact.birthday.value
        else:
            raise AttributeError(
                f"The birthday field is missing from {contact.name.value}'s contact"
            )

    def get_birthdays_per_week(self):
        birthday_dict = defaultdict(list)
        birthdays_result = ""

        current_date = datetime.today().date()

        for record in self.data.values():
            name = record.name.value.title()
            birthday = datetime.strptime(
                str(record.birthday.value), "%d %B %Y")
            birthday = birthday.date()
            birthday_current_year = birthday.replace(year=current_date.year)

            if birthday_current_year < current_date:
                birthday_current_year = birthday.replace(
                    year=current_date.year + 1)

            delta_days = (birthday_current_year - current_date).days

            if delta_days < 7:
                if birthday_current_year.weekday() >= 5:
                    birthday_dict["Monday"].append(name)
                else:
                    birthday_dict[birthday_current_year.strftime(
                        '%A')].append(name)

        for day, users_list in birthday_dict.items():
            birthdays_result += f"{day}: {', '.join(list(users_list))}\n"

        return birthdays_result
