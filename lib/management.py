# As a user
# So I don't forget the details
# I want to keep a record of friends' names and birthdates

# As a user
# So I can make edits when I've got dates wrong
# I want to be able to update a record by passing in a name and new date

# As a user
# So I can make edits when people change their name
# I want to be able to update a record by passing in an old and a new name

# As a user
# So I can remember to send birthday cards at the right time
# I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

# As a user
# So I can buy age-appropriate birthday cards
# I want to calculate the upcoming ages for friends with birthdays

# As a user
# So I can keep track of cards sent and to be sent
# I want to be able to mark a birthday card for a year as "done"


from datetime import datetime, timedelta


class BirthdayReminder:
    def __init__(self):
        self.friends = {}

    def add_friend(self, name, birthdate):
        self.friends[name] = birthdate

    def update_birthdate(self, name, new_birthdate):
        if name in self.friends:
            self.friends[name] = new_birthdate

    def update_name(self, old_name, new_name):
        if old_name in self.friends:
            self.friends[new_name] = self.friends.pop(old_name)

    def upcoming_birthdays(self, days=7):
        today = datetime.now().date()
        upcoming = {}
        for name, birthdate in self.friends.items():
            next_birthday = birthdate.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            if (next_birthday - today).days <= days:
                upcoming[name] = next_birthday
        return upcoming

    def upcoming_ages(self):
        today = datetime.now().date()
        upcoming_ages = {}
        for name, birthdate in self.friends.items():
            next_birthday = birthdate.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            age = next_birthday.year - birthdate.year
            upcoming_ages[name] = age
        return upcoming_ages

    def mark_card_done(self, name, year):
        # Assuming the user would mark the card as done for the year of the birthday
        if name in self.friends:
            if year in self.friends[name]:
                self.friends[name][year] = "done"
            else:
                print("Year not found for the birthday.")
        else:
            print("Friend not found.")
